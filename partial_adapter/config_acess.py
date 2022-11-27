from typing import Any, Protocol

from bs4 import BeautifulSoup


class Config(Protocol):
    def get(self, key: str, default: Any = None) -> Any | None:
        """Return the value associated with key."""


class XMLConfigAdpter(Config):

    def __init__(self, bs: BeautifulSoup) -> None:
        self.bs = bs

    def get(self, key: str, default: Any = None) -> Any:
        value = self.bs.find(key)
        if not value:
            return default
        return value.text
