from typing import Optional

from pydantic import BaseModel, Field, model_validator

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata, StrBool


class ReferenceRiskPayload(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )
    rev_id: Optional[int] = Field(
        default=None,
        title="Revision ID of the article",
        description="The model scores every reference in this revision. Give "
        "rev_id or domain, not both.",
        gt=0,
    )
    domain: Optional[str] = Field(
        default=None,
        title="Domain to evaluate",
        description='A domain or a full URL, for example "nytimes.com". The '
        "response gives the data of this domain on the wiki. Give rev_id or "
        "domain, not both.",
    )
    extended_output: Optional[StrBool] = Field(
        default=None,
        title="Extended Output - return all references",
        description="Whether the response includes the list of references. The "
        "API ignores this field for a domain request. Default: false.",
    )

    @model_validator(mode="after")
    def check_rev_id_or_domain(self) -> "ReferenceRiskPayload":
        if (self.rev_id is None) == (self.domain is None):
            raise ValueError("Give rev_id or domain, but not both.")
        return self


reference_risk_metadata = ModelMetadata(
    name="Language-agnostic reference risk",
    classname="ReferenceRiskModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/referenceRiskPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language-agnostic_reference_risk",
)


class ReferenceRiskModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/reference-risk:predict",
        **kwargs,
    ):
        super().__init__(base_url, ReferenceRiskPayload, **kwargs)
