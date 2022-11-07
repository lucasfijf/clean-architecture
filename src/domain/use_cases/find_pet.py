from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to find user use case"""

    @abstractmethod
    def by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""

        raise NotImplementedError()

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""

        raise NotImplementedError()

    @abstractmethod
    def by_id_and_user_id(self, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""

        raise NotImplementedError()
