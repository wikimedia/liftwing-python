import pytest
from pydantic import ValidationError

from liftwing import ReferenceRiskModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/reference-risk:predict"


@pytest.mark.parametrize(
    "payload",
    [
        {"lang": "en", "rev_id": 123456789},
        {"lang": "en", "domain": "nytimes.com"},
    ],
)
def test_request_posts_payload(http, payload):
    ReferenceRiskModel().request(payload)

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == payload


def test_request_sends_extended_output_as_string(http):
    # The model server reads extended_output as a string.
    ReferenceRiskModel().request(
        {"lang": "en", "rev_id": 123456789, "extended_output": True}
    )

    assert http.last.kwargs["json"]["extended_output"] == "true"


@pytest.mark.parametrize(
    "payload",
    [
        {"lang": "en"},
        {"lang": "en", "rev_id": 123456789, "domain": "nytimes.com"},
        {"rev_id": 123456789},
    ],
)
def test_request_rejects_invalid_payload(http, payload):
    with pytest.raises(ValidationError):
        ReferenceRiskModel().request(payload)
    assert http.calls == []
