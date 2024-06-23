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
