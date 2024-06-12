from .liftwing_model import LiftwingModel


class ArticleQualityModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-articlequality:predict"):
        super().__init__(base_url)