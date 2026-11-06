import pytest
from pydantic import ValidationError

from liftwing import LLMChatModel
from liftwing.models.llm import LLM_TIMEOUT

URL = "https://api.wikimedia.org/service/lw/inference/v1/models/llm-qwen3-14b/openai/v1/chat/completions"
MESSAGES = [{"role": "user", "content": "What is the Wikimedia Foundation?"}]


def test_chat_posts_completion_request(http):
    LLMChatModel("llm-qwen3-14b").chat(MESSAGES, max_completion_tokens=100)

    assert http.last.method == "POST"
    assert http.last.url == URL
    assert http.last.kwargs["json"] == {
        "model": "llm-qwen3-14b",
        "messages": MESSAGES,
        "max_completion_tokens": 100,
    }
    assert http.last.kwargs["timeout"] == LLM_TIMEOUT


def test_chat_returns_completion(http):
    http.body = {"choices": [{"message": {"role": "assistant", "content": "Hi"}}]}

    result = LLMChatModel("llm-qwen3-14b").chat(MESSAGES)

    assert result["choices"][0]["message"]["content"] == "Hi"


def test_chat_rejects_streaming(http):
    with pytest.raises(ValidationError, match="streaming"):
        LLMChatModel("llm-qwen3-14b").chat(MESSAGES, stream=True)
    assert http.calls == []


def test_chat_rejects_empty_messages(http):
    with pytest.raises(ValidationError):
        LLMChatModel("llm-qwen3-14b").chat([])
    assert http.calls == []
