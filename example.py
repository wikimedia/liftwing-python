import json
import requests

def revert_risk_api_request(language, revision_id):

    use_auth = False
    inference_url = 'https://api.wikimedia.org/service/lw/inference/v1/models/' + language + '-reverted:predict'

    if use_auth:

        headers = {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)',
            'Content-type': 'application/json'
        }
    else:
        headers = {}

    data = {"rev_id": revision_id}
    response = requests.post(inference_url, headers=headers, data=json.dumps(data))
    return response.json()


language = "viwiki"
revision_id = 12345
response = revert_risk_api_request(language, revision_id)

print(response)
