from typing import Any, Dict
from abc import ABC, abstractmethod


class LiftwingModel(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def request(self, payload: Dict[str, Any], method: str = "POST", headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This is an abstact method that makes a request to the API endpoint.

        Args:
        - payload (Dict[str, Any]): The payload to send with the request.
        - method (str): The HTTP method to use for the request (default is "POST").
        - headers (Dict[str, str]): Optional headers to include in the request.

        Returns:
        - Dict[str, Any]: The JSON response from the API.
        """
        pass
