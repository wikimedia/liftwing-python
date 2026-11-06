from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


class ArticleCountryPayload(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )
    title: str = Field(
        ...,
        title="Title of the Wikipedia article",
        description='Example: "Eiffel Tower".',
    )


article_country_metadata = ModelMetadata(
    name="Article country",
    classname="ArticleCountryModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Countries%2C%20language%2C%20and%20translation/articleCountryPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Article_country",
)


class ArticleCountryModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/article-country:predict",
        **kwargs,
    ):
        super().__init__(base_url, ArticleCountryPayload, **kwargs)
