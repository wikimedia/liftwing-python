import json
import requests
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict

class ArticleTopic(LiftwingModel):

    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 

    def request(self, method: str = "POST", headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict
        using the language parameter and returns a JSON. 
        The language parameter is for the different wiki languages, and rev_id is for specific revisions.
        """
        url = "https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict"

        if headers is None:
            headers = {}

        data = {"text": "Some sample text in any language that we want to identify"}
        
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Unexpected error occurred: {response.status_code}")