import pytest
from pydantic import ValidationError

from liftwing import ArticleTopicModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/outlink-topic-model:predict"


def test_request_posts_payload(http):
    ArticleTopicModel().request({"page_title": "Douglas_Adams", "lang": "en"})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"page_title": "Douglas_Adams", "lang": "en"}


def test_request_accepts_page_id_and_wiki_id(http):
    payload = {"page_id": 60520815, "wiki_id": "enwiki", "revision_id": 123456}
    ArticleTopicModel().request(payload)

    assert http.last.kwargs["json"] == payload


def test_request_sends_threshold_as_float(http):
    # The model server rejects a threshold that is not a float.
    ArticleTopicModel().request({"page_id": 1, "lang": "en", "threshold": 1})

    assert http.last.kwargs["json"]["threshold"] == 1.0
    assert isinstance(http.last.kwargs["json"]["threshold"], float)


@pytest.mark.parametrize(
    "payload",
    [
        {"lang": "en"},
        {"page_title": "Douglas_Adams", "page_id": 1, "lang": "en"},
        {"page_title": "Douglas_Adams"},
    ],
)
def test_request_rejects_invalid_payload(http, payload):
    with pytest.raises(ValidationError):
        ArticleTopicModel().request(payload)
    assert http.calls == []
