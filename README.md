# LiftWing Python Module
## _Make request to machine learning models_

[![Build Status]

The LiftWing python module works as a middle man for developers making API requests. With this module developers will be able to import their desired API and make requests to it

## Features

- Users can pip install liftwing
- Make requests to ML models
- Automatic publishing to PyPI with Github ActionsF

## Installation

Install the dependencies for liftwing.

```sh
cd project
```
```sh
pip3 install -i https://test.pypi.org/simple/ liftwing
```

Second Tab:
Now Liftwing should be in your project

(optional):

```sh
pip -list liftwing
```

#### Making a request in .py file

Open new .py file

```sh
from liftwing.models import RevertRiskAPIModel

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
