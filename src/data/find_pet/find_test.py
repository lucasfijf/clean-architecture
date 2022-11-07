from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_id():
    """Should select pet by id"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_id(pet_id=attributes["pet_id"])

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert response["Success"] is True
    assert response["Data"]
