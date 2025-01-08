import json
import requests
from settings import VALID_EMAIL, VALID_PASS


class Pets:
    """API library for the site http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Swagger request to the site for getting user's unique token using email и password"""
        data = {'email': VALID_EMAIL,
                'password': VALID_PASS}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, my_id

    # Pets().get_token()

    def get_list_users(self):
        """Getting list of users"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json

        print(res.json())
        return status, amount

    # Pets().get_list_users()

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
        print(pet_id)
        print(res.json())
        return pet_id, status

    # Pets().create_pet()

    def get_pet_photo(self):
        """Getting pet's photo"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        # pic = open('/Users/annakulikova/PycharmProjects/Selenium_API_Pet/tests/photo/Cat.jpeg', 'rb')
        files = {'pic': (
            'Cat.jpeg', open('/Users/annakulikova/PycharmProjects/Selenium_API_Pet/tests/photo/Cat.jpeg', 'rb'),
            'image/jpeg')}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        print(res.json())
        return status, link

    # Pets().get_pet_photo()

    def update_pet_name(self):
        """Updating pet's name"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Maila', "type": 'monkey', "age": 6, "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        print(res.json())
        return pet_id, status

    # Pets().update_pet_name()

    def delete_pet(self):
        """Pet deletion"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.delete(self.base_url + f'pet/{pet_id}', data=json.dumps(data), headers=headers)
        status = res.status_code
        print(res.json())
        return status

    def add_like(self):
        """Like adding"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        print(res.json())
        return status

    def receive_pets_list(self):
        """Pet's list receiving"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        print(my_id)
        print(res.json())
        return status, my_id

    def add_comment(self):
        """Comment addition"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"message": 'Nice pet!'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        comment = res.text
        return status, comment


Pets().add_comment()

