from typing import Optional

from pydantic import BaseModel, Field, model_validator

from .liftwing_model import LiftwingModel, ModelMetadata


class ArticleTopicPayload(BaseModel):
    page_title: Optional[str] = Field(
        default=None,
        title="A string representing the title of the Wiki article to score",
        description="Example: 'Douglas_Adams' for the Wiki page of the author "
        "Douglas Adams. Give page_title or page_id, not both.",
    )
    page_id: Optional[int] = Field(
        default=None,
        title="Page ID of the Wiki article to score",
        description="The numeric page ID. Give page_title or page_id, not both.",
        gt=0,
    )
    lang: Optional[str] = Field(
        default=None,
        title="Language code of the wiki",
        description="A string representing the language code related to the target "
        'wiki. Example: "en" for English Wikipedia. Not necessary if you give '
        "wiki_id.",
    )
    wiki_id: Optional[str] = Field(
        default=None,
        title="Database name of the wiki",
        description='Example: "enwiki". The model gets the language from this '
        "value if you do not give lang.",
    )
    revision_id: Optional[int] = Field(
        default=None,
        title="Revision ID of the article",
        description="Use the links of this revision, not of the current version "
        "of the page.",
        gt=0,
    )
    threshold: Optional[float] = Field(
        default=None,
        title="Custom threshold for evaluating scores",
        description="A float representing a custom threshold value to use when "
        "evaluating the scores. Default: 0.5.",
    )
    features_str: Optional[str] = Field(
        default="",
        title="Custom features to pass to the model",
        description="A string representing custom features to pass to the model. "
        "If you give features, the model does not get the links of the page from "
        "the MediaWiki API. Default: empty.",
    )
    debug: Optional[bool] = Field(
        default=False,
        title="Debug Output - return all scores",
        description="A boolean indicating whether or not to enable debug output to return all predicted topics and scores, equivalent to setting the threshold to 0. Default: false.",
    )

    @model_validator(mode="after")
    def check_page_and_wiki(self) -> "ArticleTopicPayload":
        if (self.page_title is None) == (self.page_id is None):
            raise ValueError("Give page_title or page_id, but not both.")
        if self.lang is None and self.wiki_id is None:
            raise ValueError("Give lang or wiki_id.")
        return self


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
        **kwargs,
    ):
        super().__init__(base_url, ArticleTopicPayload, **kwargs)
