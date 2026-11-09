from typing import List, Optional

from pydantic import BaseModel, Field, model_validator

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata


class EditCheckInstance(BaseModel):
    lang: str = Field(
        ...,
        title="Language code of the text",
        description='Example: "en" for English.',
    )
    page_title: str = Field(
        ...,
        title="Title of the page",
        description="The title of the page, or the planned title of a new page.",
    )
    check_type: str = Field(
        ...,
        title="Type of check",
        description='"tone" (peacock language), "npov" (non-neutral point of view) '
        'or "weasel" (weasel words).',
    )
    original_text: str = Field(..., title="Text before the edit")
    modified_text: str = Field(
        ...,
        title="Text after the edit",
        description="Must be different from original_text.",
    )
    return_shap_values: Optional[bool] = Field(
        default=None,
        title="Return SHAP values",
        description="Whether the response includes SHAP explanation values. "
        "Default: false.",
    )

    @model_validator(mode="after")
    def check_texts_are_different(self) -> "EditCheckInstance":
        if self.original_text == self.modified_text:
            raise ValueError("modified_text must be different from original_text.")
        return self


class EditCheckPayload(BaseModel):
    instances: List[EditCheckInstance] = Field(
        ...,
        title="Texts to check",
        description="The API accepts a maximum of 20 instances in one request.",
        min_length=1,
    )


edit_check_metadata = ModelMetadata(
    name="Edit check (tone, NPOV and weasel words)",
    classname="EditCheckModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Revision%20quality/editCheckPredict",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models/Production/Tone_Check",
)


class EditCheckModel(LiftwingModel):
    def __init__(
        self,
        base_url="https://api.wikimedia.org/service/lw/inference/v1/models/edit-check:predict",
        **kwargs,
    ):
        super().__init__(base_url, EditCheckPayload, **kwargs)
