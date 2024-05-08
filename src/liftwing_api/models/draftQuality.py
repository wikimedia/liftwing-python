from liftwing_model import LiftwingModel

class DraftQuality(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-draftquality:predict"):
        super().__init__(base_url)

    def request_to_draftQualityAPI(self, revision_id: int):
        endpoint_url = f"{self.base_url}"
        return self.request(endpoint_url, revision_id)

rev = DraftQuality()
jsonresponse = rev.request_to_draftQualityAPI(revision_id=12345)
print(jsonresponse)