from src.infra.repositories.pet_repository import PetRepository
from src.infra.repositories.user_repository import UserRepository
from src.data.register_pet.register import RegisterPet
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """Composing register pet route
    :param - None
    :return - object with register pet route
    """

    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user_use_case)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
