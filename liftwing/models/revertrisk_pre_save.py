from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .liftwing_model import LiftwingModel, ModelMetadata

# The README of the revert risk model server describes the revision_data input.
PRE_SAVE_DOCUMENTATION_URL = (
    "https://gerrit.wikimedia.org/r/plugins/gitiles/machinelearning/liftwing/"
    "inference-services/+/refs/heads/main/src/models/revert_risk_model/README.md"
)


# The models accept more fields than these. Thus the models below keep the
# fields that they do not declare.
class PreSaveUser(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int = Field(..., title="User ID", description="Use 0 for an anonymous user.")


class PreSavePage(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int = Field(..., title="Page ID")
    title: str = Field(..., title="Page title")
    first_edit_timestamp: str = Field(
        ...,
        title="Time of the first edit of the page",
        description='ISO 8601 format. Example: "2018-01-01T10:02:02Z".',
    )


class PreSaveParentRevision(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int = Field(..., title="Revision ID of the parent revision")
    lang: str = Field(..., title="Language code of the wiki")
    text: str = Field(..., title="Wikitext of the parent revision")
    timestamp: str = Field(
        ..., title="Time of the parent revision", description="ISO 8601 format."
    )
    bytes: int = Field(..., title="Size of the parent revision in bytes")
    comment: Optional[str] = Field(default=None, title="Edit summary")


class PreSaveRevision(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int = Field(
        ...,
        title="Revision ID",
        description="Use -1 for an edit that is not saved yet.",
    )
    lang: str = Field(
        ...,
        title="Language code of the wiki",
        description='Example: "en" for English Wikipedia.',
    )
    text: str = Field(..., title="Wikitext of the revision")
    timestamp: str = Field(
        ..., title="Time of the revision", description="ISO 8601 format."
    )
    bytes: int = Field(..., title="Size of the revision in bytes")
    comment: Optional[str] = Field(default=None, title="Edit summary")
    page: PreSavePage
    parent: PreSaveParentRevision
    user: PreSaveUser


class RevertRiskPreSavePayload(BaseModel):
    revision_data: PreSaveRevision = Field(
        ...,
        title="Data of the revision to score",
        description="The model uses this data. It does not get the revision "
        "from the MediaWiki API.",
    )


revertrisk_pre_save_metadata = ModelMetadata(
    name="Language-agnostic revert risk (pre-save)",
    classname="RevertRiskPreSaveModel",
    api_documentation_url=PRE_SAVE_DOCUMENTATION_URL,
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Language-agnostic_revert_risk",
)

revertrisk_multilingual_pre_save_metadata = ModelMetadata(
    name="Multilingual revert risk (pre-save)",
    classname="RevertRiskMultilingualPreSaveModel",
    api_documentation_url=PRE_SAVE_DOCUMENTATION_URL,
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Multilingual_revert_risk",
)


class RevertRiskPreSaveModel(LiftwingModel):
    """Score an edit with the language-agnostic revert risk model.

    The edit does not have to be saved. Send the revision data in the payload.
    """

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic-pre-save:predict",
        **kwargs,
    ):
        super().__init__(base_url, RevertRiskPreSavePayload, **kwargs)


class RevertRiskMultilingualPreSaveModel(LiftwingModel):
    """Score an edit with the multilingual revert risk model.

    The edit does not have to be saved. Send the revision data in the payload.
    """

    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-multilingual-pre-save:predict",
        **kwargs,
    ):
        super().__init__(base_url, RevertRiskPreSavePayload, **kwargs)
