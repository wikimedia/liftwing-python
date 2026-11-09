from typing import Optional

from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata, StrBool


class ArticleQualityPayload(BaseModel):
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
    extended_output: Optional[StrBool] = Field(
        default=None,
        title="Extended Output - return features",
        description="Whether the response includes the features that the model "
        "uses. Default: false.",
    )


articlequality_language_agnostic_metadata = ModelMetadata(
    name="Language-agnostic article quality",
    classname="ArticleQualityModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/articleQualityLangAgnosticPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language-agnostic_Wikipedia_article_quality",
)


class ArticleQualityModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/articlequality:predict",
        **kwargs,
    ):
        super().__init__(base_url, ArticleQualityPayload, **kwargs)
