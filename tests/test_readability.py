import pytest
from pydantic import ValidationError

from liftwing import ReadabilityModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/readability:predict"


def test_request_posts_payload(http):
    ReadabilityModel().request({"lang": "en", "rev_id": 123456})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 123456}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        ReadabilityModel().request({"lang": "en"})
    assert http.calls == []
