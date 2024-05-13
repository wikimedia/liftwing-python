import requests
import json
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Dict

class RevertRiskAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-{language}-agnostic:predict"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 

    def request(self, payload: Dict[str, int], method: str = "POST", headers: Dict[str, str] = None) -> Dict[str, int]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict
        using the language parameter and returns a JSON
        language is for the different wiki languages, rev_id is the specific revisions
        """
        language = payload.get("language")
        if language is None:
            raise ValueError("'language' parameter is required in the payload.")
        rev_id = payload.get("revision_id")
        if rev_id is None:
            raise ValueError("revision id is none, add revision id to continue")
        
        url = self.base_url.format(language=language)

        if headers is None:
            headers = {}
        headers['Content-Type'] = 'application/json'

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.status_code == 400
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
        

rev = RevertRiskAPIModel()
payload_without_language = {"revision_id": 123456}
result = rev.request(payload_without_language)
