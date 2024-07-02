from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel, ModelMetadata


class ReadabilityPayload(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )
    rev_id: int = Field(
        ...,
        title="Revision ID of the edit",
        description="The revision id for the wiki identified by the lang parameter.",
        gt=0,
    )


readability_metadata = ModelMetadata(
    name="Multilingual readability",
    classname="ReadabilityModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_readability_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Proposed/Multilingual_readability_model_card",
)


class ReadabilityModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/readability:predict",
    ):
        super().__init__(base_url, ReadabilityPayload)
