from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .liftwing_model import API_REFERENCE_URL, LiftwingModel, ModelMetadata

# The API gateway stops LLM requests after 60 seconds. This default is longer,
# so that the client gets the error response from the gateway.
LLM_TIMEOUT = 120.0


class ChatCompletionPayload(BaseModel):
    """A request to the OpenAI Chat Completions API.

    The API accepts more fields, for example max_completion_tokens and
    temperature. The payload keeps the fields that it does not declare.
    """

    model_config = ConfigDict(extra="allow")

    model: str = Field(
        ...,
        title="Model name",
        description="Must be the same as the model name in the URL.",
    )
    messages: List[Dict[str, Any]] = Field(
        ...,
        title="Messages of the conversation",
        description='Example: [{"role": "user", "content": "Hello"}].',
        min_length=1,
    )
    stream: Optional[bool] = Field(
        default=None,
        title="Stream the response",
        description="This client does not support streaming. Use an OpenAI client "
        "library to stream the response.",
    )

    @field_validator("stream")
    @classmethod
    def check_no_streaming(cls, value: Optional[bool]) -> Optional[bool]:
        if value:
            raise ValueError("This client does not support streaming.")
        return value


llm_chat_metadata = ModelMetadata(
    name="Large language models (chat completions)",
    classname="LLMChatModel",
    api_documentation_url=f"{API_REFERENCE_URL}#/Large%20language%20models/llmChatCompletions",
    wmf_model_card_url="https://wikitech.wikimedia.org/wiki/Machine_Learning/LiftWing/Large_Language_Models",
)


class LLMChatModel(LiftwingModel):
    """A client for the public Lift Wing large language models.

    The models use the OpenAI Chat Completions API. The client sends one
    request and returns the full response. It does not support streaming.

    Args:
    - model_name (str): The name of the model, for example "llm-qwen3-14b".
    - base_url (str): The URL prefix of the Lift Wing models.
    """

    def __init__(
        self,
        model_name: str,
        base_url: str = "https://api.wikimedia.org/service/lw/inference/v1/models",
        timeout: float = LLM_TIMEOUT,
        **kwargs,
    ):
        super().__init__(
            f"{base_url}/{model_name}/openai/v1/chat/completions",
            ChatCompletionPayload,
            timeout=timeout,
            **kwargs,
        )
        self.model_name = model_name

    def chat(self, messages: List[Dict[str, Any]], **params: Any) -> Dict[str, Any]:
        """Send the messages and return the chat completion.

        Args:
        - messages (List[Dict[str, Any]]): The conversation, for example
          [{"role": "user", "content": "Hello"}].
        - params: Other Chat Completions parameters, for example
          max_completion_tokens.

        Returns:
        - Dict[str, Any]: The chat completion. The answer is in
          result["choices"][0]["message"]["content"].
        """
        return self.request({"model": self.model_name, "messages": messages, **params})
