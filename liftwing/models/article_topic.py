from pydantic import BaseModel, Field
from .liftwing_model import LiftwingModel, ModelMetadata


class ArticleTopicPayload(BaseModel):
    page_title: str = Field(
        ...,
        title="A string representing the title of the Wiki article to score",
        description="Example: 'Douglas_Adams' for the Wiki page of the author Douglas Adams.",
    )
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia.',
    )


outlink_articletopic_metadata = ModelMetadata(
    name="Language agnostic link-based article topic",
    classname="ArticleTopicModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_articletopic_outlink_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language_agnostic_link-based_article_topic",
)


class ArticleTopicModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict",
    ):
        super().__init__(base_url, ArticleTopicPayload)
