from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


class LanguageIdPayload(BaseModel):
    text: str = Field(
        ...,
        title="Text for language",
        description="A string that contains the text which we want to identify the language it is written in",
    )


langid_metadata = ModelMetadata(
    name="Language Identification",
    classname="LanguageIdModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Countries%2C%20language%2C%20and%20translation/langidPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language_Identification",
)


class LanguageIdModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict",
        **kwargs,
    ):
        super().__init__(base_url, LanguageIdPayload, **kwargs)
