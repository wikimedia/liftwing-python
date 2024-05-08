import json
import requests
from liftwing_model import LiftwingModel

class ArticleTopic(LiftwingModel):

    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 

    def request_to_articleTopicAPI(self, language: str, revision_id: int):
        """
        This function makes a POST request to https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict
        using the language parameter and returns a JSON
        """
        if language is None or revision_id is None:
            raise ValueError("Both 'language' and 'revision_id' parameters are required.")

        use_auth = False
        inference_url = f"https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"

        if use_auth:
            headers: {
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
                'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)',
                'Content-type': 'application/json'
            }
        else:
            headers = {}
        data = {"page_title": "Douglas_Adams", "lang": "en"}
        response = requests.post(inference_url, headers=headers, data=json.dumps(data))


        if response.status_code == 200:
            return response.json()
        else:
            response.status_code == 400
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
            
