from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel, ModelMetadata


class RevertRiskPayload(BaseModel):
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


revertrisk_metadata = ModelMetadata(
    name="Language-agnostic revert risk",
    classname="RevertRiskAPIModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_reverted_risk_language_agnostic_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Proposed/Language-agnostic_revert_risk",
)


class RevertRiskAPIModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict",
    ):
        super().__init__(base_url, RevertRiskPayload)
