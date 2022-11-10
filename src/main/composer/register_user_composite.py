from src.main.interfaces import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repositories.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """Composing register user route
    :param - None
    :return - object with register user route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
