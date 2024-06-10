import requests
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict
import json

class LanguageAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict"):
        super().__init__(base_url)

    def request(self, text: str, headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict
        using the provided text parameter and returns a JSON.
        """
        if headers is None:
            headers = {}

        data = {"text": text}
        
        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
            
lang = LanguageAPIModel()

jsonresponse = lang.request("Some sample text in any language that we want to identify")

print(jsonresponse)