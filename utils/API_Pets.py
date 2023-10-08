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

class Pet_Demo_api():
    ID = None# в методе POST присвоим созданный ID

    """Метод для Получения списка всех животных."""

    @staticmethod
    def get_all_Pets():
        print("Запуск GET запроса для Получения всех категорий животных")
        params = {
            'limit': 1,
            'offset': 3
        }
        url_get_all_pets = f'{base_url}pet/'

        try:
            response_get_all_pets = requests.get(url=url_get_all_pets, auth=auth, headers=headers, params=params)
            response_get_all_pets.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP ошибка {err}")
            raise #указываем об ошибке
        except Exception as err:
            print(f"Ошибка  {err}")
            raise #указываем об ошибке
        assert response_get_all_pets.status_code == 200 #Проверяем фактический и ожидаемый результат
        print('GET запрос успешный. Список категорий животных получен!')
        print(response_get_all_pets.json())

    """Метод для Создания животного"""

    @staticmethod
    def post_Pet():
        print("Запуск Post запроса для Создания  животного")
        data = {
            "name": f"Post_Name{a}{b}",
            "photo_url": f"Post_url{a}{b}",
            "category": {
                "name": f"Post_Name_cat{a}{b}"
            },
            "status": "available"
        }
        url_post_pet_ID = f'{base_url}pet/'
        try:
            response_post_pet_ID = requests.post(url=url_post_pet_ID, auth=auth, headers=headers, json=data)
            response_post_pet_ID.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP ошибка: {err}")
            raise #указываем об ошибке
        except Exception as err:
            print(f"An ошибка: {err}")
            raise #указываем об ошибке
        assert response_post_pet_ID.status_code == 201#Проверяем фактический и ожидаемый результат
        print('Post запрос успешный. Создание категории животного')
        print(response_post_pet_ID.json())
        Pet_Demo_api.ID = response_post_pet_ID.json().get("id")  # обновляем ID


    """Метод для Получения животного по Id"""
    @staticmethod
    def get_Pet_for_ID():
        if Pet_Demo_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке


        print("Запуск GET запроса для Получения ID животного")
        url_get_pet = f'{base_url}pet/{Pet_Demo_api.ID}/'
        try:
            response_get_pet = requests.get(url=url_get_pet, auth=auth, headers=headers)
            response_get_pet.raise_for_status()  # Этот метод вызовет HTTPError для плохих ответов (4xx и 5xx)
        except requests.exceptions.HTTPError as err:
            print(f"HTTP ошибка {err}")
            raise #указываем об ошибке
        except Exception as err:
            print(f"Ошибка: {err}")
            raise #указываем об ошибке

        assert response_get_pet.status_code == 200 #Проверяем фактический и ожидаемый результат
        print('GET запрос успешный. ID категории животного получено  ID = ' + str(Pet_Demo_api.ID))
        print(response_get_pet.json())

    """Метод для Обновления имени животного"""
    @staticmethod
    def put_change_Pet():
        if Pet_Demo_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке

        print("Запуск PUT запроса для Обновления имени животного")

        data = {
            "name": f"Put_Name{a}{b}",
            "photo_url": f"Put_url{a}{b}",
            "category": {
                "name": f"Put_Name_cat{a}{b}"
            },
            "status": "available"
        }
        url_put_pet_ID = f'{base_url}pet/{Pet_Demo_api.ID}/'
        try:
            response_put_category_ID = requests.put(url=url_put_pet_ID, auth=auth, headers=headers, json=data)
            response_put_category_ID.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP ошибка {err}")
            raise #указываем об ошибке
        except Exception as err:
            print(f"ошибка: {err}")
            raise #указываем об ошибке

        assert response_put_category_ID.status_code == 200 #Проверяем фактический и ожидаемый результат
        print('PUT запрос успешный. Обновления категории животного ID = ' + str(Pet_Demo_api.ID))
        print(response_put_category_ID.json())


    """Метод для Удаления категории животного"""

    @staticmethod
    def DELETE_Pet():
        if Pet_Demo_api.ID is None:
            print("ID не установлен")
            raise  # указываем об ошибке

        print("Запуск DELETE запроса для УДАЛАЕНИЯ животного")
        url_delete_pet_ID = f'{base_url}pet/{Pet_Demo_api.ID}/'
        try:
            response_delete_pet_ID = requests.delete(url=url_delete_pet_ID, auth=auth, headers=headers)
            response_delete_pet_ID.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP ошибка: {err}")
            raise #указываем об ошибке
        except Exception as err:
            print(f"ошибка: {err}")
            raise #указываем об ошибке

        assert response_delete_pet_ID.status_code == 204 #Проверяем фактический и ожидаемый результат
        print('DELETE запрос успешный. Удаления категории животного ID = ' + str(Pet_Demo_api.ID))
