import pytest
from pydantic import ValidationError

from liftwing import RevertRiskMultilingualModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-multilingual:predict"


def test_request_posts_payload(http):
    RevertRiskMultilingualModel().request({"lang": "en", "rev_id": 123456})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 123456}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        RevertRiskMultilingualModel().request({"rev_id": 123456})
    assert http.calls == []
