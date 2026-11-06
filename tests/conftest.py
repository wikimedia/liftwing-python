import json
from dataclasses import dataclass, field
from typing import Any, Dict, List

import pytest
import requests


@dataclass
class Call:
    method: str
    url: str
    kwargs: Dict[str, Any]


@dataclass
class FakeHTTP:
    """Record HTTP calls and return a fixed response."""

    status_code: int = 200
    body: Any = field(default_factory=lambda: {"output": "test"})
    calls: List[Call] = field(default_factory=list)

    @property
    def last(self) -> Call:
        return self.calls[-1]

    def handle(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        self.calls.append(Call(method.upper(), url, kwargs))
        response = requests.Response()
        response.status_code = self.status_code
        response.url = url
        if isinstance(self.body, str):
            response._content = self.body.encode()
        else:
            response._content = json.dumps(self.body).encode()
            response.headers["Content-Type"] = "application/json"
        return response


@pytest.fixture
def http(monkeypatch: pytest.MonkeyPatch) -> FakeHTTP:
    """Replace all HTTP calls with a fake. No test sends a real request."""
    fake = FakeHTTP()

    def request(session, method, url, **kwargs):
        return fake.handle(method, url, **kwargs)

    monkeypatch.setattr(requests.Session, "request", request)
    return fake
