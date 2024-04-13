import allure
import pytest


from http import HTTPStatus

from data import Data
from helpers import (get_data_for_check_response_error as response_error,
                     register_new_courier_and_return_login_password as courier_data_is_exist,
                     get_response_get_courier as get_courier)


@pytest.mark.get_url('login_courier')
class TestLoginCourier:

    @allure.title('[Позитивный] Авторизация курьера')
    def test_login_courier_positive(self, get_url, get_new_data):
        payload = courier_data_is_exist(get_new_data)
        response = get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK and 'id' in response.json()

    @allure.title('[Негативный] Авторизация курьера с некорректными кредами')
    @pytest.mark.parametrize('condition', ('incorrect_login', 'incorrect_password'))
    def test_login_courier_with_incorrect_creds(
            self, get_url, condition, get_new_data):
        current_data = courier_data_is_exist(get_new_data)
        payload = response_error(condition, current_data)
        response = get_courier(get_url, payload)
        assert response.json()['message'] == Data.ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD

    @allure.title('[Негативный] Авторизация несуществующего пользователя')
    def test_login_courier_with_required_fields_available_success(self, get_url, get_new_data):
        payload = courier_data_is_exist(get_new_data)
        password = get_new_data['login']
        payload['login'] = f"new{get_new_data['login']}"
        response = get_courier(get_url, payload)
        payload['login'] = password
        message = response.json()['message']
        assert (response.status_code == HTTPStatus.NOT_FOUND and
                message == Data.ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD)
