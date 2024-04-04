import pytest

from data import APICourier, APIOrder
from helpers import cancel_order, get_data_for_create_courier


@pytest.fixture
def get_url(request):
    marker = request.node.get_closest_marker('get_url')
    data_marker = None if marker is None else marker.args[0]
    if data_marker == 'create_courier':
        url = APICourier()
        test_url = url.post_api_courier_route()
    elif data_marker == 'login_courier':
        url = APICourier()
        test_url = url.get_api_courier_route()
    elif data_marker in ('create_order', 'get_list_orders'):
        url = APIOrder()
        test_url = url.get_post_api_order_route()
    else:
        return None
    return test_url


@pytest.fixture
def cansel_fixture():
    payload = {}
    yield payload
    cancel_order(payload)


@pytest.fixture
def get_new_data():
    payload = get_data_for_create_courier()
    yield payload
