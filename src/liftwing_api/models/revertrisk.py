import requests
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict

class RevertRiskAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict"):
        super().__init__(base_url)

    def request(self, payload: Dict[str, Any], method: str = "POST", headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict
        using the language parameter and returns a JSON
        language is for the different wiki languages, rev_id is the specific revisions
        """
        language = payload.get("lang")
        if language is None:
            raise ValueError("'lang' parameter is required in the payload.")
        rev_id = payload.get("rev_id")
        if rev_id is None:
            raise ValueError("rev_id is none, add revision id to continue")

        if headers is None:
            headers = {}

        response = requests.post(self.base_url, json=payload, headers=headers)

        return response.json()
