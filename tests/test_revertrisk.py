import pytest
from pydantic import ValidationError

from liftwing import RevertRiskAPIModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-language-agnostic:predict"


def test_request_posts_payload(http):
    result = RevertRiskAPIModel().request({"lang": "en", "rev_id": 123456})

    assert result == http.body
    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 123456}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        RevertRiskAPIModel().request({"lang": "en", "rev_id": 0})
    assert http.calls == []


def test_request_posts_batch_payload(http):
    payload = {
        "instances": [{"lang": "en", "rev_id": 123456}, {"lang": "en", "rev_id": 2}]
    }
    RevertRiskAPIModel().request(payload)

    assert http.last.kwargs["json"] == payload


@pytest.mark.parametrize(
    "payload",
    [
        {"instances": []},
        {"instances": [{"lang": "en", "rev_id": 1}, {"lang": "de", "rev_id": 2}]},
    ],
)
def test_request_rejects_invalid_batch_payload(http, payload):
    with pytest.raises(ValidationError):
        RevertRiskAPIModel().request(payload)
    assert http.calls == []
