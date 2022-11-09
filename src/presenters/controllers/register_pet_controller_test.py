from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_handle():
    """Testing handle method"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_controller = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.name(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }
    response = register_pet_controller.handle(HttpRequest(body=attributes))

    assert register_pet_use_case.register_param["name"] == attributes["name"]
    assert register_pet_use_case.register_param["specie"] == attributes["specie"]
    assert register_pet_use_case.register_param["age"] == attributes["age"]
    assert (
        register_pet_use_case.register_param["user_information"]
        == attributes["user_information"]
    )
    assert response.status_code == 200
    assert "error" not in response.body
