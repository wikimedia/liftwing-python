from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


class RevertRiskWikidataPayload(BaseModel):
    rev_id: int = Field(
        ...,
        title="Revision ID of the Wikidata edit",
        description="The revision id of the edit on Wikidata.",
        gt=0,
    )


revertrisk_wikidata_metadata = ModelMetadata(
    name="Wikidata revert risk",
    classname="RevertRiskWikidataModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/revertriskWikidataPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/RevertRisk_Wikidata",
)


class RevertRiskWikidataModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-wikidata:predict",
        **kwargs,
    ):
        super().__init__(base_url, RevertRiskWikidataPayload, **kwargs)
