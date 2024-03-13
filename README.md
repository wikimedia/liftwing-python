# liftwing-python

This project involves building a python package that can act as a model registry for the machine learning models deployed on Lift Wing. A model registry acts as the source of truth for the deployed models and their versions offering two main benefits:
* Versioning and tracking of models: this allows an easier access to model version and tracking
* Collaboration and reproducibility: in order to download a model the user only needs to interact with the registry.
Implementation Proposal A python package that allows that has different install options according to the model as each model server has different package requirements. The user, after installing the package, will be able to load a Lift Wing model and make predictions. Taking into consideration the short duration of the internship as well as the fact that we want the person to get to know the Wikimedia community, our way of working as well as get the chance to study and dive into technical topics, the package will first deal with 1-2 models in order to create a complete proof of concept for this work. Also, to avoid blocking this work by other systems/factors or permissions it will be based on our public interfaces: The python package will have a repository on GitHub with CI/CD setup using Github Actions that will automatically upload the python package to the PyPI repository. Models for the packages will be fetched by the public analytics repository https://analytics.wikimedia.org/published/wmf-ml-models/
There will be two modes of operation for each model:
* Offline: the user can download and load the model and start making predictions with it. This is particularly useful for experimentation or in the case when someone wants to make a big number of batch requests that would otherwise fail due to rate limiting.
* Online: The user can make requests to the public APIs (Lift Wing API Gateway) using the package as a client.
Notes/Considerations:
* We would have to figure out a (nice) way to integrate this with the deployment charts repo in order to get the model version we need to deploy.
* Model’s python dependencies: Each model has been developed separately and may require different python libraries and versions. This means that the python package should have different installation options which will reflect the dependencies of a specific model.
