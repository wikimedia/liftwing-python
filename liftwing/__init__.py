from .models.revertrisk import RevertRiskAPIModel, revertrisk_metadata
from .models.revscoring import RevscoringModel, damaging_metadata, goodfaith_metadata, \
    reverted_metadata, articlequality_metadata, articletopic_metadata, draftquality_metadata, \
    drafttopic_metadata

__metadata__ = [
    revertrisk_metadata, damaging_metadata, goodfaith_metadata, reverted_metadata,
    articlequality_metadata, articletopic_metadata, draftquality_metadata, drafttopic_metadata
]
__all__ = [RevertRiskAPIModel, RevscoringModel]
