from abc import ABC
from typing import Any, Dict, Type

import requests
from pydantic import BaseModel


class LiftwingModel(ABC):
    def __init__(self, base_url: str = None, payload_model: Type[BaseModel] = None):
        self.base_url = base_url
        self.payload_model = payload_model

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
        """
        if self.payload_model:
            _ = self.payload_model(**payload)

        if headers is None:
            headers = {}

        response = requests.post(self.base_url, json=payload, headers=headers)

        return response.json()


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
