from .models.article_country import ArticleCountryModel, article_country_metadata
from .models.article_quality import (
    ArticleQualityModel,
    articlequality_language_agnostic_metadata,
)
from .models.article_topic import ArticleTopicModel, outlink_articletopic_metadata
from .models.edit_check import EditCheckModel, edit_check_metadata
from .models.language_id import LanguageIdModel, langid_metadata
from .models.liftwing_model import LiftWingError
from .models.readability import ReadabilityModel, readability_metadata
from .models.reference_need import ReferenceNeedModel, reference_need_metadata
from .models.reference_risk import ReferenceRiskModel, reference_risk_metadata
from .models.revertrisk import RevertRiskAPIModel, revertrisk_metadata
from .models.revertrisk_multilingual import (
    RevertRiskMultilingualModel,
    revertrisk_multilingual_metadata,
)
from .models.revertrisk_pre_save import (
    RevertRiskMultilingualPreSaveModel,
    RevertRiskPreSaveModel,
    revertrisk_multilingual_pre_save_metadata,
    revertrisk_pre_save_metadata,
)
from .models.revertrisk_wikidata import (
    RevertRiskWikidataModel,
    revertrisk_wikidata_metadata,
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
    itemquality_metadata,
    itemtopic_metadata,
)

__metadata__ = [
    article_country_metadata,
    articlequality_language_agnostic_metadata,
    articlequality_metadata,
    articletopic_metadata,
    damaging_metadata,
    draftquality_metadata,
    drafttopic_metadata,
    edit_check_metadata,
    goodfaith_metadata,
    itemquality_metadata,
    itemtopic_metadata,
    langid_metadata,
    outlink_articletopic_metadata,
    readability_metadata,
    reference_need_metadata,
    reference_risk_metadata,
    reverted_metadata,
    revertrisk_metadata,
    revertrisk_multilingual_metadata,
    revertrisk_multilingual_pre_save_metadata,
    revertrisk_pre_save_metadata,
    revertrisk_wikidata_metadata,
]
__all__ = [
    "ArticleCountryModel",
    "ArticleQualityModel",
    "ArticleTopicModel",
    "EditCheckModel",
    "LanguageIdModel",
    "LiftWingError",
    "ReadabilityModel",
    "ReferenceNeedModel",
    "ReferenceRiskModel",
    "RevertRiskAPIModel",
    "RevertRiskMultilingualModel",
    "RevertRiskMultilingualPreSaveModel",
    "RevertRiskPreSaveModel",
    "RevertRiskWikidataModel",
    "RevscoringModel",
]
