from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """Register user use case interface"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Use case"""

        raise NotImplementedError()
