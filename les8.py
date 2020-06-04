import requests


class MyError(Exception):
    def __init__(self, text=''):
        self.text = text


class MyCls:
    a = 22
    b = 33

    def __init__(self, data: str, a, b):
        self.data = data
        self.a = a
        self.b = b

    @staticmethod
    def some(a, b):
        return a + b

    @classmethod
    def some_cls(cls):
        return cls.a + cls.b


class Product:
    name = 'NO NAME'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name


class Catalog:
    __api_url = 'https://5ka.ru/api/v2/special_offers/'
    __headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                      'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}

    def __init__(self):
        self.products = []

    def parse(self):
        url = self.__api_url
        while url:
            response = requests.get(url, headers=self.__headers)
            data = response.json()
            url = data.get('next')
            self.products.extend([Product(**itm) for itm in data['results']])

    def some(self):
        raise MyError('ТУТ ВОЗНИКЛА ОШИБКА')


if __name__ == '__main__':
    a = Catalog()
    try:
        a.some()
    except MyError as e:
        print(e)