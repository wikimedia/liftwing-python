from typing import Optional

from pydantic import BaseModel, Field, model_validator

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata

# The OpenAPI documentation of the recommendation API.
RECOMMENDATION_DOCUMENTATION_URL = (
    "https://api.wikimedia.org/service/lw/recommendation/api/docs"
)


class TranslationRecommendationPayload(BaseModel):
    source: str = Field(
        ...,
        title="Source language",
        description='Language code of the wiki to translate from. Example: "en".',
    )
    target: str = Field(
        ...,
        title="Target language",
        description='Language code of the wiki to translate to. Example: "el". '
        "Must be different from source.",
    )
    count: Optional[int] = Field(
        default=None,
        title="Number of recommendations",
        description="Default: 12.",
        gt=0,
    )
    seed: Optional[str] = Field(
        default=None,
        title="Seed articles",
        description="One or more article titles for personalized recommendations, "
        "separated by |.",
    )
    topic: Optional[str] = Field(
        default=None,
        title="Article topics",
        description="One or more article topics for personalized recommendations, "
        'for example "Music+South Africa" or "Southern Africa|Western Africa". See '
        "https://www.mediawiki.org/wiki/ORES/Articletopic#Taxonomy",
    )
    country: Optional[str] = Field(
        default=None,
        title="Article countries",
        description="ISO 3166 alpha-3 country codes for personalized "
        'recommendations, for example "can+usa" or "prk|kor".',
    )
    featured_collection: Optional[str] = Field(
        default=None,
        title="Featured collection",
        description="A featured collection to filter the recommendations, for "
        'example "Essential Articles".',
    )
    collections: Optional[bool] = Field(
        default=None,
        title="Use page collections",
        description="Whether to get the recommendations from page collections. "
        "Default: false.",
    )
    lead_section: Optional[bool] = Field(
        default=None,
        title="Lead section only",
        description="Whether the size filters use only the lead section. "
        "Default: false.",
    )
    include_pageviews: Optional[bool] = Field(
        default=None,
        title="Include pageviews",
        description="Whether the response includes pageview counts. Default: false.",
    )
    search_algorithm: Optional[str] = Field(
        default=None,
        title="Search algorithm",
        description='"morelike" or "mostpopular". The API uses it if you give '
        'seed. Default: "morelike".',
    )
    rank_method: Optional[str] = Field(
        default=None,
        title="Rank method",
        description='"default" or "sitelinks". Default: "default".',
    )
    min_size: Optional[int] = Field(
        default=None,
        title="Minimum size",
        description="Minimum article or section size in bytes.",
    )
    max_size: Optional[int] = Field(
        default=None,
        title="Maximum size",
        description="Maximum article or section size in bytes.",
    )
    continue_offset: Optional[int] = Field(
        default=None,
        title="Continue offset",
        description="The continue_offset value of the previous response. Use it "
        "to get the next recommendations.",
    )
    continue_seed: Optional[int] = Field(
        default=None,
        title="Continue seed",
        description="The continue_seed value of the previous response. Use it to "
        "get the next recommendations.",
    )


class PageCollectionMembershipPayload(BaseModel):
    collection: str = Field(
        ...,
        title="Name of the page collection",
    )
    language: Optional[str] = Field(
        default=None,
        title="Language code of the titles",
        description="Give language and titles, or give qids.",
    )
    titles: Optional[str] = Field(
        default=None,
        title="Article titles to check",
        description="Article titles, separated by |. Give language and titles, "
        "or give qids.",
    )
    qids: Optional[str] = Field(
        default=None,
        title="Wikidata QIDs to check",
        description='Wikidata QIDs, separated by |, for example "Q123|Q456". Give '
        "language and titles, or give qids.",
    )

    @model_validator(mode="after")
    def check_titles_or_qids(self) -> "PageCollectionMembershipPayload":
        has_titles = self.language is not None and self.titles is not None
        if has_titles == (self.qids is not None):
            raise ValueError("Give language and titles, or give qids, but not both.")
        return self


translation_recommendation_metadata = ModelMetadata(
    name="Content translation recommendations (articles)",
    classname="TranslationRecommendationModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Countries%2C%20language%2C%20and%20translation/translation",
)

section_translation_recommendation_metadata = ModelMetadata(
    name="Content translation recommendations (sections)",
    classname="SectionTranslationRecommendationModel",
    api_documentation_url=RECOMMENDATION_DOCUMENTATION_URL,
)

page_collections_metadata = ModelMetadata(
    name="Content translation page collections",
    classname="PageCollectionsModel",
    api_documentation_url=RECOMMENDATION_DOCUMENTATION_URL,
)

page_collection_groups_metadata = ModelMetadata(
    name="Content translation page collection groups",
    classname="PageCollectionGroupsModel",
    api_documentation_url=RECOMMENDATION_DOCUMENTATION_URL,
)

page_collection_membership_metadata = ModelMetadata(
    name="Content translation page collection membership",
    classname="PageCollectionMembershipModel",
    api_documentation_url=RECOMMENDATION_DOCUMENTATION_URL,
)


class TranslationRecommendationModel(LiftwingModel):
    """Get articles to translate from the source wiki to the target wiki."""

    http_method = "GET"

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/recommendation/api/v1/translation",
        **kwargs,
    ):
        super().__init__(base_url, TranslationRecommendationPayload, **kwargs)


class SectionTranslationRecommendationModel(LiftwingModel):
    """Get article sections to translate from the source wiki to the target wiki."""

    http_method = "GET"

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/recommendation/api/v1/translation/sections",
        **kwargs,
    ):
        super().__init__(base_url, TranslationRecommendationPayload, **kwargs)


class PageCollectionsModel(LiftwingModel):
    """Get the metadata of the page collections. This endpoint has no payload."""

    http_method = "GET"

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/recommendation/api/v1/translation/page-collections",
        **kwargs,
    ):
        super().__init__(base_url, **kwargs)


class PageCollectionGroupsModel(LiftwingModel):
    """Get the page collections in groups. This endpoint has no payload."""

    http_method = "GET"

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/recommendation/api/v1/translation/page-collection-groups",
        **kwargs,
    ):
        super().__init__(base_url, **kwargs)


class PageCollectionMembershipModel(LiftwingModel):
    """Find which articles or Wikidata items are in a page collection."""

    http_method = "GET"

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/recommendation/api/v1/translation/page-collection-membership",
        **kwargs,
    ):
        super().__init__(base_url, PageCollectionMembershipPayload, **kwargs)
