import pytest
from pydantic import ValidationError

from liftwing import ArticleTopicModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"


def test_request_posts_payload(http):
    ArticleTopicModel().request({"page_title": "Douglas_Adams", "lang": "en"})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"page_title": "Douglas_Adams", "lang": "en"}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        ArticleTopicModel().request({"lang": "en"})
    assert http.calls == []
