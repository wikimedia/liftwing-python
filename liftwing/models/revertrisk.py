from pydantic import BaseModel, Field, model_validator
from .liftwing_model import LiftwingModel
from ..utils.validator import validate_payload, check_required_fields
from typing import Any, Dict


class RevertRiskPayload(BaseModel):
    lang: str = Field(...,
                      title="Language code of the wiki",
                      description='A string representing the language code related to the target '
                                  'wiki. Example: "en" for English Wikipedia.',)
    rev_id: int = Field(...,
                        title="Revision ID of the edit",
                        description="The revision id for the wiki identified by the lang parameter.",
                        gt=0)


class RevertRiskAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict"):
        super().__init__(base_url)

    @validate_payload(RevertRiskPayload)
    def request(self, payload:  Dict[str, Any], method: str = "POST",
                headers: Dict[str, str] = None) -> Dict[str, Any]:
        return super().request(payload=payload, method=method, headers=headers)
