from liftwing import RevscoringModel

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-damaging:predict"


def test_request_posts_to_model_url(http):
    RevscoringModel("damaging", "enwiki").request({"rev_id": 123456})

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {"rev_id": 123456}
