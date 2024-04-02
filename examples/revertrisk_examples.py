import json
import requests

def revert_risk_api_request(language: str, revision_id: int):
    use_auth = False
    inference_url = f"https://api.wikimedia.org/service/lw/inference/v1/models/{language}-reverted:predict"
    if use_auth:

        headers = {
            'Authorization': f'Bearer {access_token}',
            'User-Agent': user_agent,
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


language = "viwiki"
revision_id = 12345

response = revert_risk_api_request(language, revision_id)


print(response)


