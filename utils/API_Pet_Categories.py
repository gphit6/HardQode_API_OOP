import random
import requests
from requests.auth import HTTPBasicAuth

"""Методы для тестирования Pet Demo Project API"""
base_url = 'http://91.210.171.73:8080/api/' #Базовая url
auth = HTTPBasicAuth('admin', 'admin') #Логин/пароль для авторизации
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

a = random.random() #для создания уникального имени
b = random.random() #для создания уникального имени


class Pet_Demo_Project_api():
    ID = None # в методе POST присвоим созданный ID

    """Метод для Получения списка всех категорий животных."""

    @staticmethod
    def get_all_Pet_Categories():
        print("Запуск GET запроса для Получения всех категорий животных")
        params = {
            'limit': 1,
            'offset': 3
        }
        url_get_all_category = f'{base_url}category/'
        response_get_all_category = requests.get(url=url_get_all_category, auth=auth, headers=headers, params=params)
        if response_get_all_category.status_code == 200:
            print('GET запрос успешный. Список категорий животных получен!')
            print(response_get_all_category.json())
        else:
            print(f'Ошибка в GET запросе: {response_get_all_category.status_code}')
            print(response_get_all_category.text)
            raise # если не отрабатывается корректно IF, то выводит ошибку


    """Метод для Создания категории животного"""

    @staticmethod
    def post_Pet_Categories():
        print("Запуск Post запроса для Создания категории животного")
        a = random.random()
        b = random.random()
        data = {
            "name": f"Post_Name{a}{b}"
        }


        url_post_category_ID = f'{base_url}category/'

        response_post_category_ID = requests.post(url=url_post_category_ID, auth=auth, headers=headers, json=data)
        if response_post_category_ID.status_code == 201:
            print('Post запрос успешный. Создание категории животного')
            print(response_post_category_ID.json())
            Pet_Demo_Project_api.ID = response_post_category_ID.json().get("id")  # обновляем ID
        else:
            print(f'Ошибка в Post запросе: {response_post_category_ID.status_code}')
            print(response_post_category_ID.text)
            raise # если не отрабатывается корректно IF, то выводит ошибку



    """Метод для Получения категории животного по Id"""
    @staticmethod
    def get_Pet_Categories_for_ID():
        if Pet_Demo_Project_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке

        print("Запуск GET запроса для Получения категории животного")
        url_get_category = f'{base_url}category/{Pet_Demo_Project_api.ID}/'
        response_get_category = requests.get(url=url_get_category, auth=auth, headers=headers)
        if response_get_category.status_code == 200:
            print('GET запрос успешный. ID категории животного получено  ID = ' + str(Pet_Demo_Project_api.ID))
            print(response_get_category.json())
        else:
            print(f'Ошибка в GET запросе: {response_get_category.status_code}')
            print(response_get_category.text)
            raise # если не отрабатывается корректно IF, то выводит ошибку

    """Метод для Обновления категории животного"""
    @staticmethod
    def put_change_Pet_Categories():
        if Pet_Demo_Project_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке

        print("Запуск PUT запроса для Обновления категории животного")

        data = {
            "name": f"Put_Name{a}{b}"
        }
        url_put_category_ID = f'{base_url}category/{Pet_Demo_Project_api.ID}/'

        response_put_category_ID = requests.put(url=url_put_category_ID, auth=auth, headers=headers, json=data)
        if response_put_category_ID.status_code == 200:
            print('PUT запрос успешный. Обновления категории животного ID = ' + str(Pet_Demo_Project_api.ID))
            print(response_put_category_ID.json())
        else:
            print(f'Ошибка в PUT запросе: {response_put_category_ID.status_code}')
            print(response_put_category_ID.text)
            raise # если не отрабатывается корректно IF, то выводит ошибку


    """Метод для Удаления категории животного"""

    @staticmethod
    def DELETE_Pet_Categories():
        if Pet_Demo_Project_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке

        print("Запуск DELETE запроса для УДАЛАЕНИЯ категории животного")
        url_delete_category_ID = f'{base_url}category/{Pet_Demo_Project_api.ID}/'
        response_delete_category_ID = requests.delete(url=url_delete_category_ID, auth=auth, headers=headers)

        # Проверка статуса ответа
        if response_delete_category_ID.status_code == 204:
            print('DELETE запрос успешный. Удаления категории животного ID = ' + str(Pet_Demo_Project_api.ID))
        else:
            print(f'Ошибка: {response_delete_category_ID.status_code}')
            print(response_delete_category_ID.text)
            raise # если не отрабатывается корректно IF, то выводит ошибку

