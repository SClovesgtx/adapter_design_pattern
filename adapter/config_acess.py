from typing import Any, Protocol

from bs4 import BeautifulSoup


class Config(Protocol):
    def get(self, key: str, default: Any = None) -> Any:
        """Return the value associated with key."""


class XMLConfigAdpter(BeautifulSoup):
    def get(self, key: str, default: Any = None) -> Any:
        value = self.find(key)
        if not value:
            return default
        return value.text
