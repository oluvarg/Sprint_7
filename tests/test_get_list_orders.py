import allure
import pytest

from helpers import get_response_get_order


@pytest.mark.get_url('get_list_orders')
class TestGetListOrders:

    @allure.title('[Позитивный] Получение списка заказов')
    def test_get_list_orders_return_order_list_success(self, get_url):
        response = get_response_get_order(get_url)
        first_key = list(response.json().keys())[0]
        assert first_key == 'orders' and isinstance(response.json()[first_key], list)
