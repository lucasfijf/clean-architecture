from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Routes interface"""

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Route definition"""

        raise NotImplementedError()
