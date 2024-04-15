from .base_api_model import BaseAPIModel
from examples.revertrisk_examples import revert_risk_api_request
from models.base_api_model import BaseAPIModel

class RevertRiskAPIModel(BaseAPIModel):
    def __init__(self, language, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/"):
        super().__init__(base_url)
        # base url is super because every class that inherits this from the base model will be using it 
        self.language = language
        # language is the language that the post request is retrieving 

    def predict_revert_risk(self, revision_id):
        method="POST"
        # since we have instances that change we are making a post request
        endpoint = f"{self.language}-reverted:predict"
        # figure out how did this get there and be able to exoplain why it ends in -reverted:predict
        data = {"rev_id": revision_id}
        # revID is pretty much the revision id that is needed to complete the post requests 
        return self.request(endpoint, method, data=data)