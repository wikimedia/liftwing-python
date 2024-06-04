import requests
from liftwing_model import LiftwingModel
from typing import Any, Dict
import json

class ReadabilityAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict"):
        super().__init__(base_url)

    def request(self, method: str = "POST", headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict
        using the language parameter and returns a JSON
        language is for the different wiki languages, rev_id is the specific revisions
        """
        url = "https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict"

        data = {"text": "Some sample text in any language that we want to identify"}

        
        if headers is None:
            headers = {}

        response = requests.post(url, headers=headers, data=json.dumps(data))

        return response.json()