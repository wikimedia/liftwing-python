# liftwing-python

This is a Python package that acts as a client and allows users to make requests to the LiftWing API.
Its purpose is to allow users to interact with the API by writing python code instead of manipulating HTTP requests.

Below is an example of how to make a request. This specific request is being made to the revert_risk API

import json
import requests

def revert_risk_api_request(language: str, revision_id: int):
    """
    This function makes a request to the RevertRisk API. It takes in two parameters, language and revision_id. Language is the language of the wiki article.
    revision_id is the specific version of the article.
    """
    if language is None or revision_id is None:
            raise ValueError("Both 'language' and 'revision_id' parameters are required.") # this checks if there is a language and rev_id, if not an error is thrown
    

    use_auth = False
    inference_url = f"https://api.wikimedia.org/service/lw/inference/v1/models/{language}-reverted:predict" # this is the API endpoint
    if use_auth:
        headers = {
            'Authorization': f'Bearer {access_token}', 
            'User-Agent': user_agent,
            'Content-type': 'application/json'
        } # headers is a dictionary used to make a HTTP request
    else:
        headers = {}

    data = {"rev_id": revision_id}
    response = requests.post(inference_url, headers=headers, data=json.dumps(data)) # POST request is being made 
    if response.status_code == 200:
        return response.json() # request was successful so return the response
    else:
        response.status_code == 400
        raise ValueError(f"Unexpected error occurred: {response.status_code}")


language = "viwiki" # language has to be in this format, enwiki, arwiki etc...
revision_id = 12345 # rev_id has to be a valid integer, different rev_id gives different response

response = revert_risk_api_request(language, revision_id)

print(response)