import pytest
from pydantic import ValidationError

from liftwing import RevscoringModel

MODELS_URL = "https://api.wikimedia.org/service/lw/inference/v1/models"


def test_request_posts_to_model_url(http):
    RevscoringModel("damaging", "enwiki").request({"rev_id": 123456})

    assert http.last.method == "POST"
    assert http.last.url == f"{MODELS_URL}/enwiki-damaging:predict"
    assert http.last.kwargs["json"] == {"rev_id": 123456}


def test_request_supports_wikidata_models(http):
    RevscoringModel("itemquality", "wikidatawiki").request({"rev_id": 123456})

    assert http.last.url == f"{MODELS_URL}/wikidatawiki-itemquality:predict"


def test_request_accepts_extended_output(http):
    payload = {"rev_id": 123456, "extended_output": True}
    RevscoringModel("goodfaith", "enwiki").request(payload)

    assert http.last.kwargs["json"] == payload


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        RevscoringModel("damaging", "enwiki").request({"rev_id": -1})
    assert http.calls == []


def test_unknown_model_type_is_an_error():
    with pytest.raises(ValueError, match="edit-quality"):
        RevscoringModel("edit-quality", "enwiki")
