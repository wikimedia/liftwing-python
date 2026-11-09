import pytest
from pydantic import ValidationError

from liftwing import EditCheckModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/edit-check:predict"

INSTANCE = {
    "lang": "en",
    "page_title": "Albert Einstein",
    "check_type": "tone",
    "original_text": "Einstein was a scientist.",
    "modified_text": "Einstein was the most brilliant genius who ever lived.",
}


def test_request_posts_payload(http):
    EditCheckModel().request({"instances": [INSTANCE]})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"instances": [INSTANCE]}


@pytest.mark.parametrize(
    "payload",
    [
        {"instances": []},
        {"instances": [{**INSTANCE, "modified_text": INSTANCE["original_text"]}]},
        {"instances": [{**INSTANCE, "check_type": None}]},
    ],
)
def test_request_rejects_invalid_payload(http, payload):
    with pytest.raises(ValidationError):
        EditCheckModel().request(payload)
    assert http.calls == []
