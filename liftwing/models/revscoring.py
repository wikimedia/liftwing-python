from typing import Literal, get_args

from pydantic import BaseModel, Field

from .liftwing_model import LiftwingModel, ModelMetadata

RevscoringModelType = Literal[
    "articlequality",
    "articletopic",
    "damaging",
    "draftquality",
    "drafttopic",
    "goodfaith",
    "itemquality",
    "itemtopic",
    "reverted",
]


class RevscoringPayload(BaseModel):
    rev_id: int = Field(
        ...,
        title="Revision ID of the edit",
        description="The revision id for the wiki",
        gt=0,
    )
    extended_output: bool = Field(
        default=False,
        title="Extended Output - return features",
        description="Whether or not the response should include the extended output of the model (like the list of features used etc..). Either true or false. Default: false",
    )


damaging_metadata = ModelMetadata(
    name="Revscoring Edit quality damaging model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_damaging_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

goodfaith_metadata = ModelMetadata(
    name="Revscoring Edit quality goodfaith model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_goodfaith_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


reverted_metadata = ModelMetadata(
    name="Revscoring Edit quality reverted model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_reverted_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


articlequality_metadata = ModelMetadata(
    name="Revscoring Article Quality model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_articlequality_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


articletopic_metadata = ModelMetadata(
    name="Revscoring Article Topic model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_articletopic_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

draftquality_metadata = ModelMetadata(
    name="Revscoring Draft Quality model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_draftquality_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)

drafttopic_metadata = ModelMetadata(
    name="Revscoring Draft Topic model",
    classname="RevscoringModel",
    api_documentation_url="https://api.wikimedia.org/wiki/Lift_Wing_API/Reference/Get_revscoring_drafttopic_prediction",
    wmf_model_card_url="https://meta.wikimedia.org/wiki/Machine_learning_models",
)


class RevscoringModel(LiftwingModel):
    """A client for the revscoring models, for example "enwiki-damaging".

    Args:
    - model_type (str): The type of model, for example "damaging".
    - wikicode (str): The wiki database name, for example "enwiki".
    - base_url (str): The URL prefix of the Lift Wing models.
    """

    def __init__(
        self,
        model_type: RevscoringModelType,
        wikicode: str,
        base_url: str = "https://api.wikimedia.org/service/lw/inference/v1/models",
        **kwargs,
    ):
        if model_type not in get_args(RevscoringModelType):
            raise ValueError(f"Unknown revscoring model type: {model_type!r}")
        super().__init__(
            f"{base_url}/{wikicode}-{model_type}:predict", RevscoringPayload, **kwargs
        )
