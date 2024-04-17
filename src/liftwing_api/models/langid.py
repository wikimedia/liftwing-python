# Python 3

import json
import requests

use_auth = False
inference_url = 'https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict'

if use_auth:
  headers: {
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
      'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)',
      'Content-type': 'application/json'
  }
else:
  headers = {}
data = {"text": "Some sample text in any language that we want to identify"}
response = requests.post(inference_url, headers=headers, data=json.dumps(data))
print(response.json())

import json
import requests
from liftwing_model import LiftwingModel

class Revscoring(LiftwingModel):

    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/{language}-reverted:predict"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 

    def request_to_revScoringAPI(self, language: str, revision_id: int):
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/{language}-goodfaith:predict
        using the language parameter and returns a JSON
        """
        if language is None or revision_id is None:
            raise ValueError("Both 'language' and 'revision_id' parameters are required.")

        use_auth = False
        inference_url = f"https://api.wikimedia.org/service/lw/inference/v1/models/{language}-goodfaith:predict"

        if use_auth:
            headers = {
                'Authorization': f'Bearer {self.access_token}',  # Assuming access_token is an attribute of class
                'User-Agent': self.user_agent,  # Assuming user_agent is an attribute of class
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
            
rev = Revscoring()

jsonresponse = rev.request_to_revScoringAPI(language="arwiki", revision_id=12345)

print(jsonresponse)