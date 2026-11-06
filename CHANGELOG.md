# Changelog

## 0.2.0

### Breaking changes

- Python 3.11 or later is necessary.
- An HTTP error response causes a `LiftWingError`. Before, `request()` returned the error body as if it were a prediction.
- `RevscoringModel`:
  - `base_url` is now the full model URL.
  - `revscoring_url` and `get_revscoring_url()` are removed.
  - An unknown `model_type` causes a `ValueError`.
  - The client validates the payload. An invalid payload causes a `pydantic.ValidationError`.
- `request()` sends the validated payload. For example, a `rev_id` that you give as a string is sent as an integer.

### New models

- `RevertRiskWikidataModel` (`revertrisk-wikidata`)
- `RevertRiskPreSaveModel` and `RevertRiskMultilingualPreSaveModel` (`revertrisk-language-agnostic-pre-save`, `revertrisk-multilingual-pre-save`)
- `ArticleQualityModel` (language-agnostic `articlequality`)
- `ArticleCountryModel` (`article-country`)
- `ReferenceNeedModel` (`reference-need`)
- `ReferenceRiskModel` (`reference-risk`)
- `EditCheckModel` (`edit-check`)
- `LLMChatModel` (public `llm-*` models, OpenAI Chat Completions API)
- `TranslationRecommendationModel` and `SectionTranslationRecommendationModel`
- `PageCollectionsModel`, `PageCollectionGroupsModel` and `PageCollectionMembershipModel`
- Metadata for the `wikidatawiki-itemquality` and `wikidatawiki-itemtopic` revscoring models

### Other changes

- All model classes accept `timeout`, `user_agent` and `access_token` arguments.
- The client sends a User-Agent header that identifies the library.
- Requests have a timeout. The default is 60 seconds, or 120 seconds for `LLMChatModel`.
- `ArticleTopicModel` accepts `page_id`, `wiki_id` and `revision_id`.
- `RevertRiskAPIModel` accepts a batch of revisions in `instances`.
- `request()` uses its `method` argument. A GET request sends the payload as query parameters.
- `from liftwing import *` works.
- The API documentation and model card links point to the current pages.
- The package is published to PyPI when a GitHub release is published.
