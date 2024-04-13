class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    ENDPOINT_COURIER_CREATE = '/api/v1/courier'
    ENDPOINT_COURIER_LOGIN = '/api/v1/courier/login'
    ENDPOINT_ORDERS_CREATE_GET_LIST = '/api/v1/orders'
    ENDPOINT_ORDER_CANCEL = '/api/v1/orders/cancel'


class Data:

    ERROR_TEXT_FOR_CREATE_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для создания учетной записи'
    ERROR_TEXT_FOR_LOGIN_EXIST_YET = 'Этот логин уже используется. Попробуйте другой.'
    ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD = 'Учетная запись не найдена'
    ERROR_MESSAGE_LOGIN_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для входа'
    RESPONSE_SUCCESS = {'ok': True}

    FIRSTNAME = "Naruto"
    LASTNAME = "Uchiha"
    ADDRESS = "Konoha, 142 apt."
    METRO_STATION = 4
    PHONE = "+7 800 355 35 35"
    RENT_TIME = 5
    DELIVERY_DATE = "2020-06-06"
    COMMENT = "Saske, come back to Konoha"

    data_client = [
        FIRSTNAME,
        LASTNAME,
        ADDRESS,
        METRO_STATION,
        PHONE,
        RENT_TIME,
        DELIVERY_DATE,
        COMMENT
    ]

    SCOOTER_COLOR_BLACK = ['BLACK']
    SCOOTER_COLOR_GRAY = ['GRAY']
    SCOOTER_COLOR_BLACK_AND_GRAY = ['BLACK', 'GRAY']
    SCOOTER_WITHOUT_COLOR = []

    data_color = [
        SCOOTER_COLOR_BLACK,
        SCOOTER_COLOR_GRAY,
        SCOOTER_COLOR_BLACK_AND_GRAY,
        SCOOTER_WITHOUT_COLOR
    ]
