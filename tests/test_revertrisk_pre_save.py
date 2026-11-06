import copy

import pytest
from pydantic import ValidationError

from liftwing import RevertRiskMultilingualPreSaveModel, RevertRiskPreSaveModel

MODELS_URL = "https://api.wikimedia.org/service/lw/inference/v1/models"

PAYLOAD = {
    "revision_data": {
        "id": -1,
        "lang": "en",
        "text": "I love Wikipedia. This is a lead.",
        "timestamp": "2022-02-15T04:30:00Z",
        "bytes": 2800,
        "comment": "Hello World",
        "page": {
            "id": 1008,
            "title": "this is a title",
            "first_edit_timestamp": "2018-01-01T10:02:02Z",
        },
        "parent": {
            "id": 1200,
            "lang": "en",
            "text": "This is a lead.",
            "timestamp": "2021-01-01T02:00:00Z",
            "bytes": 2600,
        },
        "user": {"id": 0},
    }
}


@pytest.mark.parametrize(
    "model_class, model_name",
    [
        (RevertRiskPreSaveModel, "revertrisk-language-agnostic-pre-save"),
        (RevertRiskMultilingualPreSaveModel, "revertrisk-multilingual-pre-save"),
    ],
)
def test_request_posts_payload(http, model_class, model_name):
    model_class().request(PAYLOAD)

    assert http.last.method == "POST"
    assert http.last.url == f"{MODELS_URL}/{model_name}:predict"
    assert http.last.kwargs["json"] == PAYLOAD


def test_request_keeps_undeclared_revision_fields(http):
    payload = copy.deepcopy(PAYLOAD)
    payload["revision_data"]["user"]["name"] = "Example"
    RevertRiskPreSaveModel().request(payload)

    assert http.last.kwargs["json"]["revision_data"]["user"]["name"] == "Example"


def test_request_rejects_missing_required_field(http):
    payload = copy.deepcopy(PAYLOAD)
    del payload["revision_data"]["parent"]["text"]

    with pytest.raises(ValidationError):
        RevertRiskPreSaveModel().request(payload)
    assert http.calls == []
