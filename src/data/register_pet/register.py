from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.domain.models import Users, Pets


class RegisterPet(RegisterPetInterface):
    """Register pet use case definition"""

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Register pet
        :param - name: pet name
               - specie: specie type
               - age: pet's age
               - user_information: dictionary with user_id and/or user_name
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name, specie, age, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user info and select user
        :param - user_information: dictionary with user_id and/or user_name
        :return - dictionary with the response of find_user use case
        """

        user_found = None
        user_params = user_information.keys()
        if "user_id" in user_params and "user_name" in user_params:
            user_found = self.find_user.by_id_and_name(
                user_id=user_information["user_id"], name=user_information["user_name"]
            )
        elif "user_id" not in user_params and "user_name" in user_params:
            user_found = self.find_user.by_name(name=user_information["user_name"])
        elif "user_id" in user_params and "user_name" not in user_params:
            user_found = self.find_user.by_id(user_id=user_information["user_id"])
        else:
            return {"Success": False, "Data": None}
        return user_found
