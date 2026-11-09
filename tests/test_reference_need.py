import pytest
from pydantic import ValidationError

from liftwing import ReferenceNeedModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/reference-need:predict"


def test_request_posts_payload(http):
    ReferenceNeedModel().request({"lang": "en", "rev_id": 123456789})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 123456789}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        ReferenceNeedModel().request({"lang": "en"})
    assert http.calls == []
