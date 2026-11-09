# Liftwing Python Package
## Make request to machine learning models hosted on [Lift Wing](https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing) - the Wikimedia Foundation's ML model serving platform


The LiftWing python package works as a client for developers making API requests. With this package developers will be able to import their desired API and make requests to it.

## Installation

Install the python package named `liftwing` using pip:

```sh
pip install liftwing
```

After installing the package you can list the available models, with links to their API documentation and model cards:

```sh
python -m liftwing
```

## Available models

The client supports the models that the Lift Wing API makes public at `https://api.wikimedia.org/service/lw/`.

| Class | Lift Wing endpoint | Input |
|-------|--------------------|-------|
| `RevertRiskAPIModel` | `revertrisk-language-agnostic` | `lang`, `rev_id`, or a batch of `instances` |
| `RevertRiskMultilingualModel` | `revertrisk-multilingual` | `lang`, `rev_id` |
| `RevertRiskWikidataModel` | `revertrisk-wikidata` | `rev_id` |
| `RevertRiskPreSaveModel` | `revertrisk-language-agnostic-pre-save` | `revision_data` |
| `RevertRiskMultilingualPreSaveModel` | `revertrisk-multilingual-pre-save` | `revision_data` |
| `ReadabilityModel` | `readability` | `lang`, `rev_id` |
| `ArticleQualityModel` | `articlequality` | `lang`, `rev_id` |
| `ArticleTopicModel` | `outlink-topic-model` | `page_title` or `page_id`, `lang` or `wiki_id` |
| `ArticleCountryModel` | `article-country` | `lang`, `title` |
| `ReferenceNeedModel` | `reference-need` | `lang`, `rev_id` |
| `ReferenceRiskModel` | `reference-risk` | `lang`, `rev_id` or `domain` |
| `EditCheckModel` | `edit-check` | `instances` |
| `LanguageIdModel` | `langid` | `text` |
| `RevscoringModel` | `{wiki}-{model_type}`, for example `enwiki-damaging` | `rev_id` |
| `LLMChatModel` | `llm-*`, for example `llm-qwen3-14b` | OpenAI Chat Completions request |
| `TranslationRecommendationModel` | `recommendation/api/v1/translation` | `source`, `target` |
| `SectionTranslationRecommendationModel` | `recommendation/api/v1/translation/sections` | `source`, `target` |
| `PageCollectionsModel` | `recommendation/api/v1/translation/page-collections` | none |
| `PageCollectionGroupsModel` | `recommendation/api/v1/translation/page-collection-groups` | none |
| `PageCollectionMembershipModel` | `recommendation/api/v1/translation/page-collection-membership` | `collection`, and `language` with `titles`, or `qids` |

The [Lift Wing API reference](https://wikitech.wikimedia.org/w/index.php?title=Special:RestSandbox&api=lift-wing/v1) gives all input fields and the response format of each model. The client validates the input before it sends the request.

## Usage

### Make a request

```python
from liftwing import RevertRiskAPIModel

client = RevertRiskAPIModel(user_agent="MyTool/1.0 (https://example.org/MyTool; me@example.org)")
result = client.request(payload={"lang": "en", "rev_id": 123456})

print(result)
```

Result:

```
{
   "model_name":"revertrisk-language-agnostic",
   "model_version":"3",
   "wiki_db":"enwiki",
   "revision_id":"123456",
   "output":{
      "prediction":false,
      "probabilities":{
         "true":0.25512129068374634,
         "false":0.7448787093162537
      }
   }
}
```

### Identify your tool

The [Wikimedia User-Agent policy](https://meta.wikimedia.org/wiki/User-Agent_policy) requires that clients identify themselves. Give the name of your tool and contact information with the `user_agent` argument. The client adds its own name and version, for example:

```
MyTool/1.0 (https://example.org/MyTool; me@example.org) liftwing-python/0.1.1 (https://github.com/wikimedia/liftwing-python)
```

### Authenticate

Authenticated clients get a higher rate limit. Give an OAuth 2.0 access token with the `access_token` argument. See [Wikimedia APIs/Authentication](https://www.mediawiki.org/wiki/Wikimedia_APIs/Authentication) to get a token.

```python
client = RevertRiskAPIModel(user_agent="MyTool/1.0 (...)", access_token="...")
```

All model classes accept the `user_agent`, `access_token` and `timeout` arguments.

### Errors and timeouts

If the API returns an HTTP error, the client raises `LiftWingError`. The error gives the status code, the URL and the response body.

```python
from liftwing import LiftWingError, RevertRiskAPIModel

try:
    RevertRiskAPIModel().request({"lang": "en", "rev_id": 123456})
except LiftWingError as error:
    print(error.status_code, error.body)
```

If the input is not valid, the client raises a `pydantic.ValidationError` and does not send the request.

The default timeout is 60 seconds (120 seconds for `LLMChatModel`). Use the `timeout` argument to change it.

### Revscoring models

The revscoring models exist for specific wikis. Give the model type and the wiki database name:

```python
from liftwing import RevscoringModel

client = RevscoringModel("damaging", "enwiki")
client.request({"rev_id": 123456})
```

The model types are `articlequality`, `articletopic`, `damaging`, `draftquality`, `drafttopic`, `goodfaith`, `itemquality`, `itemtopic` and `reverted`. See [Current Inference Services](https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing#Current_Inference_Services) for the wikis of each model type.

### Batch requests

`RevertRiskAPIModel` accepts a batch of revisions in the same language:

```python
RevertRiskAPIModel().request(
    {"instances": [{"lang": "en", "rev_id": 123456}, {"lang": "en", "rev_id": 123457}]}
)
```

### Large language models

`LLMChatModel` uses the OpenAI Chat Completions API of the public `llm-*` models:

```python
from liftwing import LLMChatModel

client = LLMChatModel("llm-qwen3-14b", user_agent="MyTool/1.0 (...)")
result = client.chat(
    [{"role": "user", "content": "In two sentences, what is the Wikimedia Foundation?"}],
    max_completion_tokens=200,
)
print(result["choices"][0]["message"]["content"])
```

The client does not support streaming. To stream the response, use an OpenAI client library with `base_url` set to `https://api.wikimedia.org/service/lw/inference/v1/models/<model>/openai/v1`. See [Large Language Models on Wikitech](https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing/Large_Language_Models).

### Translation recommendations

The recommendation endpoints use GET requests. The client sends the payload as query parameters:

```python
from liftwing import TranslationRecommendationModel

TranslationRecommendationModel().request({"source": "en", "target": "el", "count": 5})
```

## Rate limits

The API gateway applies rate limits for each client. For the current limits, see [Lift Wing external usage](https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing/API/External_usage). Note:

- `edit-check` uses the default rate limit of the gateway, not the higher Lift Wing rate limit.
- All `llm-*` models share one rate limit for each client.

## Development

```sh
pip install -e ".[test]"
python -m pytest
pre-commit run --all-files
```

The tests do not send requests to the Lift Wing API.
