import json
import requests
from settings import VALID_EMAIL, VALID_PASS


class Pets:
    """API library to the site http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Request to the site's Swagger to obtain a unique user token using the specified email and password"""
        data = {'email': VALID_EMAIL,
                'password': VALID_PASS}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self):
        """Getting a list of users"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def create_pet(self):
        """Pet creation"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Dana', "type": 'lion', "age": 3, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_photo(self):
        """Pet`s photo uploading"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': (
            'Cat.jpeg', open('C:/Users/User/PycharmProjects/Selenium_API_Pet/tests/photo/Cat.jpeg', 'rb'),
            'image/jpeg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def update_pet_name(self):
        """Pet`s name updating"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Maila', "type": 'monkey', "age": 6, "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        return pet_id, status

    def delete_pet(self):
        """Delete the pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.delete(self.base_url + f'pet/{pet_id}', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def add_like(self):
        """Set a like to the pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def receive_pets_list(self):
        """Get a list of my pets"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, my_id

    def add_comment(self):
        """Adding a comment to a created pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"message": 'Nice pet!'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        comment = res.text
        return status, comment

