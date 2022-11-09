from typing import Dict
from src.domain.models import Users


class RegisterUserSpy:
    """Register user use case definition"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.register_param = {}

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case"""

        self.register_param["name"] = name
        self.register_param["password"] = password

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
