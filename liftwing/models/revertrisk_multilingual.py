from typing import Any, Dict

import requests
from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel


class RevertRiskMultilingualPayload(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )
    rev_id: int = Field(
        ...,
        title="Revision ID of the edit",
        description="The revision id for the wiki",
        gt=0,
    )

class RevertRiskMultilingualModel(LiftwingModel):
    def __init__(
        self,
        base_url: str = "https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-multilingual:predict",
    ):
        super().__init__(base_url, RevertRiskMultilingualPayload)

    def request(
        self,
        payload: Dict[str, Any],
        method: str = "POST",
        headers: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        This is an function for making requests to the revscoring models on Lift Wing.
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

