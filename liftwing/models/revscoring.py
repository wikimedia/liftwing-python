from typing import Literal, get_args

from pydantic import BaseModel, Field

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata

REVSCORING_API_REFERENCE_URL = f"{API_REFERENCE_URL}#/Revscoring%20(formerly%20ORES)"
REVSCORING_MODEL_CARD_URL = (
    "https://meta.wikimedia.org/wiki/Machine_learning_models#Revscoring_models"
)

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
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/damagingPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)

goodfaith_metadata = ModelMetadata(
    name="Revscoring Edit quality goodfaith model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/goodfaithPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)


reverted_metadata = ModelMetadata(
    name="Revscoring Edit quality reverted model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/revertPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)


articlequality_metadata = ModelMetadata(
    name="Revscoring Article Quality model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/articleQualityPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)


articletopic_metadata = ModelMetadata(
    name="Revscoring Article Topic model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/articleTopicPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)

draftquality_metadata = ModelMetadata(
    name="Revscoring Draft Quality model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/draftQualityPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)

drafttopic_metadata = ModelMetadata(
    name="Revscoring Draft Topic model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/draftTopicPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)

itemquality_metadata = ModelMetadata(
    name="Revscoring Wikidata Item Quality model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/itemQualityPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
)

itemtopic_metadata = ModelMetadata(
    name="Revscoring Wikidata Item Topic model",
    classname="RevscoringModel",
    api_documentation_url=f"{REVSCORING_API_REFERENCE_URL}/itemTopicPredict",
    wmf_model_card_url=REVSCORING_MODEL_CARD_URL,
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
