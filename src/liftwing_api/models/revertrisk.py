import requests
import json
from liftwing_model import LiftwingModel

class RevertRiskAPIModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/{language}-reverted:predict"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 

    def request_to_revertRiskAPI(self, language: str, revision_id: int):
        use_auth = False
        inference_url = f"https://api.wikimedia.org/service/lw/inference/v1/models/{language}-reverted:predict"

        if use_auth:
            headers = {
                'Authorization': f'Bearer {self.access_token}',  # Assuming access_token is an attribute of your class
                'User-Agent': self.user_agent,  # Assuming user_agent is an attribute of your class
                'Content-type': 'application/json'
            }
        else:
            headers = {}

        data = {"rev_id": revision_id}
        response = requests.post(inference_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            response.status_code == 400
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
        
revertRisk = RevertRiskAPIModel()

jsonresponse = revertRisk.request_to_revertRiskAPI(language="en", revision_id=12345)

print(jsonresponse)