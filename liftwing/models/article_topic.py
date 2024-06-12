from .liftwing_model import LiftwingModel


class ArticleTopicModel(LiftwingModel):
    def __init__(self, base_url="https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"):
        super().__init__(base_url)
