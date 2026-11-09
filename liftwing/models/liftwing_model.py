from abc import ABC
from importlib.metadata import PackageNotFoundError, version
from typing import Annotated, Any, Dict, Optional

import requests
from pydantic import BaseModel, PlainSerializer, TypeAdapter

# The API gateway stops a request after 30 seconds. This default is longer,
# so that the client gets the error response from the gateway.
DEFAULT_TIMEOUT = 60.0


# The Lift Wing API reference on Wikitech. Append "#/<tag>/<operationId>" to
# link to one endpoint.
API_REFERENCE_URL = (
    "https://wikitech.wikimedia.org/w/index.php"
    "?title=Special:RestSandbox&api=lift-wing/v1"
)


# Some model servers read boolean inputs as strings, for example "true".
# A field of this type accepts a boolean and sends "true" or "false".
StrBool = Annotated[
    bool,
    PlainSerializer(
        lambda value: str(value).lower(), return_type=str, when_used="json"
    ),
]


def _library_user_agent() -> str:
    """Return the User-Agent part that identifies this library."""
    try:
        library_version = version("liftwing")
    except PackageNotFoundError:
        library_version = "unknown"
    return (
        f"liftwing-python/{library_version}"
        " (https://github.com/wikimedia/liftwing-python)"
    )


LIBRARY_USER_AGENT = _library_user_agent()


class LiftWingError(Exception):
    """The Lift Wing API returns an HTTP error status.

    Attributes:
    - status_code (int): The HTTP status code.
    - body (Any): The response body. It is JSON data if possible, else text.
    - url (str): The URL of the request.
    """

    def __init__(self, status_code: int, body: Any, url: str):
        self.status_code = status_code
        self.body = body
        self.url = url
        super().__init__(f"HTTP {status_code} from {url}: {body}")


class LiftwingModel(ABC):
    """The base class of the Lift Wing model clients.

    All model classes accept these keyword arguments:
    - timeout (float): The time in seconds to wait for a response.
    - user_agent (str): Identifies your tool and gives contact information,
      for example "MyTool/1.0 (https://example.org/MyTool; me@example.org)".
      The client adds its own name and version. The Wikimedia User-Agent
      policy requires this information:
      https://meta.wikimedia.org/wiki/User-Agent_policy
    - access_token (str): An OAuth 2.0 access token. Authenticated clients
      get a higher rate limit. See
      https://www.mediawiki.org/wiki/Wikimedia_APIs/Authentication
    """

    def __init__(
        self,
        base_url: str = None,
        payload_model: Any = None,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        user_agent: Optional[str] = None,
        access_token: Optional[str] = None,
    ):
        self.base_url = base_url
        self.payload_model = payload_model
        self.timeout = timeout
        self.user_agent = (
            f"{user_agent} {LIBRARY_USER_AGENT}" if user_agent else LIBRARY_USER_AGENT
        )
        self.access_token = access_token
        self._payload_adapter = TypeAdapter(payload_model) if payload_model else None

    def request(
        self,
        payload: Dict[str, Any],
        method: str = "POST",
        headers: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        This is function that makes a request to the API endpoint.

        Args:
        - payload (Dict[str, Any]): The payload to send with the request.
        - method (str): The HTTP method to use for the request (default is "POST").
        - headers (Dict[str, str]): Optional headers to include in the request.

        Returns:
        - Dict[str, Any]: The JSON response from the API.

        Raises:
        - LiftWingError: The API returns an HTTP error status.
        - requests.Timeout: The API does not respond before the timeout.
        """
        payload = self._prepare_payload(payload)

        headers = self._headers(headers)

        response = requests.post(
            self.base_url, json=payload, headers=headers, timeout=self.timeout
        )
        if not response.ok:
            raise LiftWingError(
                response.status_code, _response_body(response), self.base_url
            )

        return response.json()

    def _headers(self, headers: Optional[Dict[str, str]]) -> Dict[str, str]:
        """Return the default headers, updated with the headers of the caller."""
        result = {"User-Agent": self.user_agent}
        if self.access_token:
            result["Authorization"] = f"Bearer {self.access_token}"
        result.update(headers or {})
        return result

    def _prepare_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the payload and return the data to send.

        The validation changes values to the declared types, for example the
        string "123" to the integer 123. The result keeps the keys that the
        payload model does not declare. The result does not include default
        values for fields that the caller did not set.
        """
        if self._payload_adapter is None:
            return payload
        validated = self._payload_adapter.validate_python(payload)
        data = self._payload_adapter.dump_python(
            validated, mode="json", exclude_unset=True
        )
        return {**payload, **data}


def _response_body(response: requests.Response) -> Any:
    """Return the response body as JSON data, or as text if it is not JSON."""
    try:
        return response.json()
    except ValueError:
        return response.text


class ModelMetadata(BaseModel):
    name: str
    classname: str
    api_documentation_url: str
    wmf_model_card_url: str

    def __repr__(self):
        return (
            f"(\n"
            f"    name={self.name},\n"
            f"    classname={self.classname},\n"
            f"    api_documentation_url={self.api_documentation_url},\n"
            f"    wmf_model_card_url={self.wmf_model_card_url}\n"
            f")"
        )
