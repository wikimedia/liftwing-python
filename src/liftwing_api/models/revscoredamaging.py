from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict
import json
import requests

class RevScoreDamaging(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-damaging:predict"):
        super().__init__(base_url)

    def request(self, revision_id: int, headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-damaging:predict
        using the provided revision_id parameter and returns a JSON.

        Example:

        rev_score_damaging = RevScoreDamaging()
        json_response = rev_score_damaging.request(revision_id=12345)
        print(json_response)

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
        