import allure
import pytest

from http import HTTPStatus

from data import Data
from helpers import (register_new_courier_and_return_login_password as exist_courier_data,
                     get_data_without_one_required_field,
                     get_response_post_courier as post_courier)


@pytest.mark.get_url('create_courier')
class TestCreateCourier:

    @allure.title('[Позитивный] Создание курьера.')
    def test_create_courier_available_success(self, get_url, get_new_data):
        payload = get_new_data
        response = post_courier(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == Data.RESPONSE_SUCCESS

    @allure.title('[Негативный] Создание двух одинаковых круьеров.')
    def test_create_courier_as_prev_courier_unavailable_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.CONFLICT
        assert message == Data.ERROR_TEXT_FOR_LOGIN_EXIST_YET

    @allure.title('[Негативный] Создание курьера - без обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_required_field_unavailable_success(self, get_url, field, get_new_data):
        payload = dict.fromkeys([field,])
        payload = get_data_without_one_required_field(payload, get_new_data)
        response = post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert message == Data.ERROR_TEXT_FOR_CREATE_WITHOUT_REQUIRED_FIELD
