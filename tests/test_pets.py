import os.path

import pytest
import requests

from api import Pets
from settings import VALID_EMAIL, VALID_PASS

pt = Pets()  # для удобства создаем новую переменную pt и присваиваем ей весь класс Pets


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_update_pet_name():
    status = pt.update_pet_name()[1]
    pet_id = pt.update_pet_name()[0]
    assert pet_id
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_add_like():
    status = pt.add_like()
    assert status == 200


def test_add_comment():
    status, comment = pt.add_comment()
    assert status == 200
    assert 'id' in comment
