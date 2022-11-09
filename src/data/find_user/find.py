from typing import Type, Dict, List
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class FindUser(FindUserInterface):
    """Class to define find user use case"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select user by id
        :param - user_id: user's id
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)
        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select user by id
        :param - name: user's name
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)
        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select user by id
        :param - user_id: user's id
        :param - name: user's name
        :return - dictionary with process information
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)
        return {"Success": validate_entry, "Data": response}
