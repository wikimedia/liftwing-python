import pytest
from pydantic import ValidationError

from liftwing import ArticleQualityModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/articlequality:predict"


def test_request_posts_payload(http):
    ArticleQualityModel().request({"lang": "en", "rev_id": 12345})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"lang": "en", "rev_id": 12345}


@pytest.mark.parametrize("value, sent", [(True, "true"), (False, "false")])
def test_request_sends_extended_output_as_string(http, value, sent):
    # The model server reads extended_output as a string.
    ArticleQualityModel().request(
        {"lang": "en", "rev_id": 12345, "extended_output": value}
    )

    assert http.last.kwargs["json"]["extended_output"] == sent


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        ArticleQualityModel().request({"rev_id": 12345})
    assert http.calls == []
