from typing import Type, Dict, List
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """Class to define find pet use case"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by id
        :param - pet_id: pet's id
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)
        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: str) -> Dict[bool, List[Pets]]:
        """Select pet by user id
        :param - user_id: user's id
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)
        return {"Success": validate_entry, "Data": response}

    def by_id_and_user_id(self, user_id: int, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by pet id and user id
        :param - user_id: user's id
        :param - pet_id: pet's id
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)
        return {"Success": validate_entry, "Data": response}
