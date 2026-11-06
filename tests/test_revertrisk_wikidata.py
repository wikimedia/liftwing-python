import pytest
from pydantic import ValidationError

from liftwing import RevertRiskWikidataModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/revertrisk-wikidata:predict"


def test_request_posts_payload(http):
    RevertRiskWikidataModel().request({"rev_id": 1799693453})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"rev_id": 1799693453}


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        RevertRiskWikidataModel().request({"rev_id": 0})
    assert http.calls == []
