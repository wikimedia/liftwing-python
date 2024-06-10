import json
import requests
from liftwing_api.models.liftwing_model import LiftwingModel
from typing import Any, Dict

class RevertRiskMultilingual(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-multilingual:predict"):
        super().__init__(base_url)

    def request(self, text: str, headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-multilingual:predict
        using the provided text parameter and returns a JSON.
        """
        if not text:
            raise ValueError("'text' parameter required.")

        if headers is None:
            headers = {}

        data = {"text": text}
        
        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            # Print the response content for debugging
            print(f"Error response content: {response.content.decode('utf-8')}")
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
        
revert_risk_multilingual = RevertRiskMultilingual()
json_response = revert_risk_multilingual.request(text="Some sample text in any language that we want to analyze for revert risk.")
print(json_response)