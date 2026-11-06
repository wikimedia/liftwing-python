import pytest
from pydantic import ValidationError

from liftwing import LanguageIdModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/langid:predict"


def test_request_posts_payload(http):
    LanguageIdModel().request({"text": "Some text"})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"text": "Some text"}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        LanguageIdModel().request({})
    assert http.calls == []
