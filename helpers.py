import json

import allure
import requests
import random
import string

from data import Data, APICourier, APIOrder


@allure.title('Формирование тела запроса для создания курьера')
def get_data_for_create_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string(6)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }
    return payload


@allure.title('Формирование тела запроса для создания курьера и возвращения логина и пароля')
def register_new_courier_and_return_login_password(get_new_data):
    payload = get_new_data
    courier_create_url = f'{Data.MAIN_URL}{APICourier.ENDPOINT_COURIER_CREATE}'
    response = requests.post(url=courier_create_url, data=payload)
    if response.status_code == 201:
        return payload


@allure.title('Формирование тела запроса '
              'Возвращение и проверка код статуса')
def get_data_for_check_status_code(condition, get_new_data):
    payload = {}
    if condition == 'valid_data':
        payload = {
            'login': get_new_data['login'],
            'password': get_new_data['password']
        }
    if condition == 'only_login':
        payload = {
            'login': get_new_data['login'],
        }
    if condition == 'exist_data':
        payload = register_new_courier_and_return_login_password(get_new_data)
        payload['password'] = f"new{get_new_data['password']}"
    return payload


@allure.title('Проверка возвращаемой ошибки')
def get_data_for_check_response_error(condition, current_data):
    payload = {}
    if condition == 'incorrect_login':
        payload = {
            'login': f"new{current_data['login']}",
            'password': current_data['password']
        }
    if condition == 'incorrect_password':
        payload = {
            'login': current_data['login'],
            'password': f"new{current_data['password']}"
        }
    return payload


@allure.title('Получение данных без одного обязательного поля')
def get_data_without_one_required_field(payload, current_data):
    if 'login' in payload:
        payload['login'] = current_data['login']
    if 'password' in payload:
        payload['password'] = current_data['password']
    return payload


@allure.title('Удаление курьера')
def delete_courier(payload):
    url = APICourier()
    if 'firstName' in payload:
        payload.pop('firstName')
    response = requests.post(url=url.get_api_courier_route(), data=payload)
    if 'id' in response.json():
        courier_id = response.json()['id']
        requests.delete(url=f'{url.post_api_courier_route()}/{courier_id}')


@allure.title('Получить ответа от GET-запроса')
def get_response_get_courier(get_url, payload):
    response = requests.post(get_url, payload)
    return response


@allure.title('Получучение ответа от POST-запроса')
def get_response_post_courier(get_url, payload):
    response = requests.post(url=get_url, data=payload)
    return response


@allure.step('Получение ответа от POST-запроса')
def get_response_post_order(get_url, payload):
    response = requests.post(get_url, payload)
    return response


@allure.step('Получение ответа от GET-запроса')
def get_response_get_order(get_url):
    response = requests.get(get_url)
    return response


@allure.step('Получение тела запроса')
def get_body_request(order_lst):
    current_data = {
        'firstName': order_lst[0],
        'lastName': order_lst[1],
        'address': order_lst[2],
        'metroStation': order_lst[3],
        'phone': order_lst[4],
        'rentTime': order_lst[5],
        'deliveryDate': order_lst[6],
        'comment': order_lst[7],
        'color': order_lst[8]
    }
    payload = json.dumps(current_data)
    return payload


@allure.step('Отмена заказа')
def cancel_order(payload):
    url = APIOrder()
    response = requests.post(url=url.get_post_api_order_route(), data=payload)
    if 'track' in response.json():
        order_track = response.json()['track']
        payload = {
            'track': order_track
        }
        requests.put(url=f'{Data.MAIN_URL}{APIOrder.ENDPOINT_ORDER_CANCEL}', data=payload)
