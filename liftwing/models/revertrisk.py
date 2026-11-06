from typing import List, Union

from pydantic import BaseModel, Field, model_validator

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


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


class RevertRiskBatchPayload(BaseModel):
    instances: List[RevertRiskPayload] = Field(
        ...,
        title="Revisions to score",
        description="A list of revisions, all in the same language. The API "
        "accepts a maximum of 20 revisions in one request.",
        min_length=1,
    )

    @model_validator(mode="after")
    def check_same_language(self) -> "RevertRiskBatchPayload":
        if len({instance.lang for instance in self.instances}) > 1:
            raise ValueError("All instances must have the same lang.")
        return self


revertrisk_metadata = ModelMetadata(
    name="Language-agnostic revert risk",
    classname="RevertRiskAPIModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/revertriskLanguageAgnosticPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language-agnostic_revert_risk",
)


class RevertRiskAPIModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict",
        **kwargs,
    ):
        super().__init__(
            base_url, Union[RevertRiskPayload, RevertRiskBatchPayload], **kwargs
        )
