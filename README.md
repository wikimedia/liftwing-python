# Liftwing Python Package
## Make request to machine learning models hosted on [Lift Wing](https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing) - the Wikimedia Foundation's ML model serving platform


The LiftWing python package works as a client for developers making API requests. With this package developers will be able to import their desired API and make requests to it.

## Installation

Install the python package named `liftwing` using pip:

```sh
pip install liftwing
```

After installing the package you can list the available models

```sh
python -m liftwing
```

#### Using the package

We can make requests to a model server:
```sh
from liftwing import RevertRiskAPIModel

client = RevertRiskAPIModel()
result = client.request(payload={"lang": "en", "rev_id": "123456"})

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
