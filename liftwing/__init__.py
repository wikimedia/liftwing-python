from .models.article_topic import ArticleTopicModel, outlink_articletopic_metadata
from .models.language_id import LanguageIdModel, langid_metadata
from .models.readability import ReadabilityModel, readability_metadata
from .models.revertrisk import RevertRiskAPIModel, revertrisk_metadata
from .models.revertrisk_multilingual import (
    RevertRiskMultilingualModel,
    revertrisk_multilingual_metadata,
)
from .models.revscoring import (
    RevscoringModel,
    damaging_metadata,
    goodfaith_metadata,
    reverted_metadata,
    articlequality_metadata,
    articletopic_metadata,
    draftquality_metadata,
    drafttopic_metadata,
)

__metadata__ = [
    articlequality_metadata,
    articletopic_metadata,
    damaging_metadata,
    draftquality_metadata,
    drafttopic_metadata,
    goodfaith_metadata,
    langid_metadata,
    outlink_articletopic_metadata,
    readability_metadata,
    reverted_metadata,
    revertrisk_metadata,
    revertrisk_multilingual_metadata,
]
__all__ = [
    ArticleTopicModel,
    LanguageIdModel,
    ReadabilityModel,
    RevertRiskAPIModel,
    RevertRiskMultilingualModel,
    RevscoringModel,
]
