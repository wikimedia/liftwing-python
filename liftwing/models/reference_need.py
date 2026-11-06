from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


class ReferenceNeedPayload(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )
    rev_id: int = Field(
        ...,
        title="Revision ID of the article",
        description="The revision id for the wiki identified by the lang parameter.",
        gt=0,
    )


reference_need_metadata = ModelMetadata(
    name="Multilingual reference need",
    classname="ReferenceNeedModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/referenceNeedPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Multilingual_reference_need",
)


class ReferenceNeedModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/reference-need:predict",
        **kwargs,
    ):
        super().__init__(base_url, ReferenceNeedPayload, **kwargs)
