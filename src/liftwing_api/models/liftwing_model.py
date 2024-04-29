import requests
import json

class LiftwingModel:
    def __init__(self, base_url):
        self.base_url = base_url
        # bare url

    def request(self, endpoint_url: str, revision_id: int):
        """
        Makes a POST request to the specified endpoint URL using the given revision ID.
        """
        if revision_id is None:
            raise ValueError("revision_id parameter required.")
    
        use_auth = False  

        if use_auth:
            headers = {
                'Authorization': f'Bearer {self.access_token}',
                'User-Agent': self.user_agent,
                'Content-type': 'application/json'
            }
        else:
            headers = {}

        data = {"rev_id": revision_id}
        response = requests.post(endpoint_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            try:
                json_response = response.json()
            except json.JSONDecodeError:
                raise ValueError("Response content is not in JSON format.")
                
            return json_response
        else:
            raise ValueError(f"Unexpected error occurred: {response.status_code}")
