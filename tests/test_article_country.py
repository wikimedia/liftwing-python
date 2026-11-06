import pytest
from pydantic import ValidationError

from liftwing import ArticleCountryModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/article-country:predict"


def test_request_posts_payload(http):
    ArticleCountryModel().request({"lang": "en", "title": "Eiffel Tower"})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "title": "Eiffel Tower"}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        ArticleCountryModel().request({"lang": "en", "page_title": "Eiffel Tower"})
    assert http.calls == []
