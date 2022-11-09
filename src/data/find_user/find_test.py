from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser

faker = Faker()


def test_by_id():
    """Should select user by id"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])

    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert response["Success"] is True
    assert response["Data"]


def test_by_name():
    """Should select user by name"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    assert user_repo.select_user_params["name"] == attributes["name"]
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name():
    """Should select user by name"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(
        user_id=attributes["id"], name=attributes["name"]
    )

    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]
    assert response["Success"] is True
    assert response["Data"]
