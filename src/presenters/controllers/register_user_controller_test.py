from faker import Faker
from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_user_controller import RegisterUserController

faker = Faker()


def test_handle():
    """Testing handle method"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserController(register_user_use_case)

    attributes = {"name": faker.name(), "password": faker.word()}
    response = register_user_controller.handle(HttpRequest(body=attributes))

    assert register_user_use_case.register_param["name"] == attributes["name"]
    assert register_user_use_case.register_param["password"] == attributes["password"]
    assert response.status_code == 200
    assert "error" not in response.body
