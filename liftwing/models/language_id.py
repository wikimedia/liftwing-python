from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel


class LanguageIdPayload(BaseModel):
    text: str = Field(
        ...,
        title="Text for language",
        description="A string that contains the text which we want to identify the language it is written in",
    )

class LanguageIdAPIModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict",
    ):
        super().__init__(base_url, LanguageIdPayload)
