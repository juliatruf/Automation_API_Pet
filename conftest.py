import pytest

from api import Pets
from settings import DEFAULT_USER, VALID_PET_PAYLOAD


class PetControl:
    def __init__(self, pet_id):
        self.pet_id = pet_id
        self.deleted = False

@pytest.fixture()
def user_token_id():
    login_user = Pets()
    res = login_user.get_token(DEFAULT_USER)
    user_token = res[1]
    user_id = res[2]
    return user_token, user_id

@pytest.fixture()
def pet_id(user_token_id):
    pet = Pets()
    new_pet_id = pet.create_pet(user_token_id, VALID_PET_PAYLOAD)[1]
    pet_control = PetControl(new_pet_id)
    yield pet_control
    if not pet_control.deleted:
        pet.delete_pet_by_id(user_token_id, pet_control.pet_id)