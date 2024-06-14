from typing import Any, Dict

import requests
from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel, ModelMetadata


class RevscoringPayload(BaseModel):
    rev_id: int = Field(
        ...,
        title="Revision ID of the edit",
        description="The revision id for the wiki",
        gt=0,
    )
    extended_output: bool = Field(
        title="Extended Output - return features",
        description="Whether or not the response should include the extended output of the model (like the list of features used etc..). Either true or false. Default: false",
    )


damaging_metadata = ModelMetadata(
    name="Revscoring Edit quality damaging model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_damaging_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

goodfaith_metadata = ModelMetadata(
    name="Revscoring Edit quality goodfaith model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_goodfaith_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


reverted_metadata = ModelMetadata(
    name="Revscoring Edit quality reverted model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_reverted_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


articlequality_metadata = ModelMetadata(
    name="Revscoring Article Quality model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_articlequality_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


articletopic_metadata = ModelMetadata(
    name="Revscoring Article Topic model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_articletopic_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

draftquality_metadata = ModelMetadata(
    name="Revscoring Draft Quality model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_draftquality_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

drafttopic_metadata = ModelMetadata(
    name="Revscoring Draft Topic model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_drafttopic_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


class RevscoringModel(LiftwingModel):
    def __init__(
        self,
        model_type: str,
        wikicode: str,
        base_url: str = "https://api.wikimedia.org/service/lw/inference/v1/models",
    ):
        super().__init__(base_url)
        self.revscoring_url = self.get_revscoring_url(model_type, wikicode)

    def get_revscoring_url(self, model_type: str, wikicode: str) -> str:
        return f"{self.base_url}/{wikicode}-{model_type}:predict"

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

        response = requests.post(self.revscoring_url, json=payload, headers=headers)

        return response.json()
