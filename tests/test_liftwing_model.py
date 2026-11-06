import pytest

from liftwing import (
    ArticleTopicModel,
    LiftWingError,
    RevertRiskAPIModel,
    RevscoringModel,
)
from liftwing.models.liftwing_model import DEFAULT_TIMEOUT, LiftwingModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/test:predict"


def test_request_returns_json_response(http):
    http.body = {"prediction": True}

    assert LiftwingModel(URL).request({"rev_id": 1}) == {"prediction": True}


def test_http_error_raises_liftwing_error_with_json_body(http):
    http.status_code = 400
    http.body = {"error": "The rev_id parameter is missing."}

    with pytest.raises(LiftWingError) as error:
        LiftwingModel(URL).request({})

    assert error.value.status_code == 400
    assert error.value.body == {"error": "The rev_id parameter is missing."}
    assert error.value.url == URL


def test_http_error_with_html_body_keeps_the_text(http):
    http.status_code = 502
    http.body = "<html>Bad Gateway</html>"

    with pytest.raises(LiftWingError) as error:
        LiftwingModel(URL).request({})

    assert error.value.status_code == 502
    assert error.value.body == "<html>Bad Gateway</html>"


def test_request_uses_default_timeout(http):
    LiftwingModel(URL).request({})

    assert http.last.kwargs["timeout"] == DEFAULT_TIMEOUT


def test_models_accept_a_custom_timeout(http):
    RevertRiskAPIModel(timeout=5).request({"lang": "en", "rev_id": 1})
    RevscoringModel("damaging", "enwiki", timeout=5).request({"rev_id": 1})

    assert [call.kwargs["timeout"] for call in http.calls] == [5, 5]


def test_request_sends_validated_values(http):
    RevertRiskAPIModel().request({"lang": "en", "rev_id": "123456"})

    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 123456}


def test_request_keeps_undeclared_keys(http):
    RevertRiskAPIModel().request({"lang": "en", "rev_id": 1, "new_option": "x"})

    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 1, "new_option": "x"}


def test_request_does_not_add_default_values(http):
    ArticleTopicModel().request({"page_title": "Douglas_Adams", "lang": "en"})

    assert http.last.kwargs["json"] == {"page_title": "Douglas_Adams", "lang": "en"}
