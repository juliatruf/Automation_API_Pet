import json
import requests


class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered(self, new_user_cred) -> json:
        """Запрос к Swagger сайта для регистрации нового пользователя
        и получения уникального токена по указанным email и password"""
        res = requests.post(self.base_url + 'register', data=json.dumps(new_user_cred))
        res_json = res.json()
        user_token = res_json.get('token')
        user_id = res_json.get('id')
        status = res.status_code
        return status, user_token, user_id

    def get_token(self, user_cred) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя
        по указанным email и password"""
        res = requests.post(self.base_url + 'login', data=json.dumps(user_cred))
        status = res.status_code
        user_token = res.json().get('token')
        user_id = res.json().get('id')
        return status, user_token, user_id

    def get_list_users(self, token):
        """Запрос к Swagger сайта для получения уникального идентификатора пользователя"""
        headers = {'Authorization': f'Bearer {token[0]}', 'accept': 'application/json'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        user_id = res.text
        return status, user_id

    def create_pet(self, token, pet_data) -> json:
        """Запрос к Swagger сайта для создания нового питомца авторизованным пользователем"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        res = requests.post(self.base_url + 'pet', data=json.dumps(pet_data), headers=headers)
        new_pet_id = res.json().get('id')
        status = res.status_code
        return status, new_pet_id

    def get_pet_by_id(self, id_pet) -> json:
        """Запрос к Swagger сайта для получения данных питомца по id"""
        headers = {'accept': 'application/json'}
        res = requests.get(self.base_url + f'pet/{id_pet}', headers=headers)
        status = res.status_code
        pet_data = res.json()
        pet_data_common_info = pet_data.get('pet', {})
        pet_data_id = pet_data_common_info.get('id', None)
        pet_likes_count = pet_data_common_info.get('likes_count', 0)
        pet_comments = pet_data.get('comments', [])
        return status, pet_data_id, pet_data, pet_likes_count, pet_comments

    def post_pet_photo(self, token, id_pet, image_path) -> json:
        """Запрос к Swagger сайта для загрузки изображения для сохраненного питомца
         по указанному id питомца"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        files = {'pic': ('cat_1.jpg', open(image_path, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + f'pet/{id_pet}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json().get('link')
        return status, link

    def add_pet_like(self, token, id_pet) -> json:
        """Запрос к Swagger сайта для добавления лайка сохраненному питомцу по указанному id питомца"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        res = requests.put(self.base_url + f'pet/{id_pet}/like', headers=headers)
        status = res.status_code
        return status

    def add_pet_comment(self, token, id_pet, message) -> json:
        """Запрос к Swagger сайта для добавления комментария сохраненному питомцу по указанному id питомца"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        data = {"pet_id": id_pet, "message": message, "user_id": token[1]}
        res = requests.put(self.base_url + f'pet/{id_pet}/comment', json=data, headers=headers)
        status = res.status_code
        comment_id = res.json().get('id')
        return status, comment_id

    def delete_pet_by_id(self, token, id_pet) -> json:
        """Запрос к Swagger сайта для удаления питомца по указанному id питомца"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        res = requests.delete(self.base_url + f'pet/{id_pet}', headers=headers)
        status = res.status_code
        return status

    def delete_user_by_id(self, token) -> json:
        """Запрос к Swagger сайта для удаления пользователя по указанному id пользователя"""
        headers = {'Authorization': f'Bearer {token[0]}'}
        res = requests.delete(self.base_url + f'users/{token[1]}', headers=headers)
        status = res.status_code
        return status