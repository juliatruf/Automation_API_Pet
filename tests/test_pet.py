import pytest

from api import Pets
from conftest import user_token_id, pet_id
from settings import VALID_IMAGE_FILE
from tests.data.testing_data import valid_users, new_user_credentials, comment_message, pet_payload


pt = Pets()

# def test_get_registered_with_valid_data():
#     response = pt.get_registered(new_user_credentials)
#     status, token, user_id = response
#     assert status == 200
#     assert token
#     assert user_id
#     pt.delete_user_by_id((token, user_id))
#
#
# @pytest.mark.parametrize(
#     'user_credentials',
#     [
#         pytest.param(user, id=f'{user["email"]}, {user["password"]}') for user in valid_users
#     ]
# )
# def test_get_token_with_valid_data(user_credentials):
#     response = pt.get_token(user_credentials)
#     status = response[0]
#     token = response[1]
#     assert status == 200
#     assert token
#
#
# def test_get_list_users_with_valid_data(user_token_id):
#     response = pt.get_list_users(user_token_id)
#     status, my_id = response
#     assert status == 200
#     assert my_id
#
#
# def test_create_pet_with_valid_data(user_token_id):
#     response = pt.create_pet(user_token_id, pet_payload)
#     status, new_pet_id = response
#     assert status == 200
#     assert new_pet_id
#     check_result = pt.get_pet_by_id(new_pet_id)
#     status = check_result[0]
#     assert status == 200
#     pt.delete_pet_by_id(user_token_id, new_pet_id)
#
#
# def test_get_pet_data_with_valid_id(pet_id):
#     response = pt.get_pet_by_id(pet_id.pet_id)
#     status = response[0]
#     id_pet = response[1]
#     assert status == 200
#     assert id_pet == pet_id.pet_id
#
#
# def test_post_pet_photo_with_valid_data(user_token_id, pet_id):
#     response = pt.post_pet_photo(user_token_id, pet_id.pet_id, VALID_IMAGE_FILE)
#     status, link = response
#     assert status == 200
#     assert link
#
#
# def test_add_pet_like(user_token_id, pet_id):
#     response = pt.add_pet_like(user_token_id, pet_id.pet_id)
#     assert response == 200
#     check_result = pt.get_pet_by_id(pet_id.pet_id)
#     likes_count = check_result[3]
#     assert likes_count == 1
#
#
# @pytest.mark.parametrize('message', comment_message)
# def test_add_pet_comment(user_token_id, pet_id, message):
#     response = pt.add_pet_comment(user_token_id, pet_id.pet_id, message)
#     status, comment_id = response
#     assert status == 200
#     assert comment_id
#     check_result = pt.get_pet_by_id(pet_id.pet_id)
#     comments = check_result[4]
#     assert len(comments) == 1


def test_delete_pet_by_valid_id(user_token_id, pet_id):
    response = pt.delete_pet_by_id(user_token_id, pet_id.pet_id)
    status = response
    assert status == 200
    check_result = pt.get_pet_by_id(pet_id.pet_id)
    status_check = check_result[0]
    pet_data_id = check_result[1]
    if status_check == 404:
        assert True
    elif pet_data_id is None:
        assert False, "Питомец не найден, но API не вернул 404"
    else:
        assert False, f"Питомец с ID {pet_id.pet_id} не был удален"
    pet_id.deleted = True


# def test_delete_user_by_id_with_valid_data():
#     register = pt.get_registered(new_user_credentials)
#     token_id = (register[1], register[2])
#     response = pt.delete_user_by_id(token_id)
#     assert response == 200
#     user_credentials = new_user_credentials
#     user_credentials.pop("confirm_password")
#     check_result = pt.get_token(user_credentials)
#     status = check_result[0]
#     assert status == 400