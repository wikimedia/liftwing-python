import json
import requests
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict

class Revscoring(LiftwingModel):
    def __init__(self, language: str, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-reverted:predict"):
        super().__init__(base_url.format(language=language))
        self.language = language

    def request(self, revision_id: int, headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/{language}-goodfaith:predict
        using the provided revision_id parameter and returns a JSON.
        """
        if revision_id is None:
            raise ValueError("'revision_id' parameter required.")

        if headers is None:
            headers = {}

        data = {"rev_id": revision_id}
        
        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
            
rev = Revscoring(language="enwiki")

jsonresponse = rev.request(revision_id=12345)

print(jsonresponse)