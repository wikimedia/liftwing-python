import pytest
from pydantic import ValidationError

from liftwing import (
    PageCollectionGroupsModel,
    PageCollectionMembershipModel,
    PageCollectionsModel,
    SectionTranslationRecommendationModel,
    TranslationRecommendationModel,
)

URL = "https://api.wikimedia.org/service/lw/recommendation/api/v1/translation"


@pytest.mark.parametrize(
    "model_class, url",
    [
        (TranslationRecommendationModel, URL),
        (SectionTranslationRecommendationModel, f"{URL}/sections"),
    ],
)
def test_request_gets_recommendations(http, model_class, url):
    model_class().request({"source": "en", "target": "el", "count": 3})

    assert http.last.method == "GET"
    assert http.last.url == url
    assert http.last.kwargs["params"] == {"source": "en", "target": "el", "count": 3}


def test_request_sends_booleans_as_lowercase_strings(http):
    TranslationRecommendationModel().request(
        {"source": "en", "target": "el", "include_pageviews": True}
    )

    assert http.last.kwargs["params"]["include_pageviews"] == "true"


def test_request_rejects_invalid_payload(http):
    with pytest.raises(ValidationError):
        TranslationRecommendationModel().request({"source": "en"})
    assert http.calls == []


@pytest.mark.parametrize(
    "model_class, url",
    [
        (PageCollectionsModel, f"{URL}/page-collections"),
        (PageCollectionGroupsModel, f"{URL}/page-collection-groups"),
    ],
)
def test_request_without_payload(http, model_class, url):
    model_class().request()

    assert http.last.method == "GET"
    assert http.last.url == url
    assert http.last.kwargs["params"] == {}


@pytest.mark.parametrize(
    "payload",
    [
        {"collection": "Essential Articles", "language": "en", "titles": "A|B"},
        {"collection": "Essential Articles", "qids": "Q123|Q456"},
    ],
)
def test_page_collection_membership(http, payload):
    PageCollectionMembershipModel().request(payload)

    assert http.last.method == "GET"
    assert http.last.url == f"{URL}/page-collection-membership"
    assert http.last.kwargs["params"] == payload


@pytest.mark.parametrize(
    "payload",
    [
        {"collection": "Essential Articles"},
        {"collection": "Essential Articles", "titles": "A|B"},
        {
            "collection": "Essential Articles",
            "language": "en",
            "titles": "A",
            "qids": "Q1",
        },
    ],
)
def test_page_collection_membership_rejects_invalid_payload(http, payload):
    with pytest.raises(ValidationError):
        PageCollectionMembershipModel().request(payload)
    assert http.calls == []
