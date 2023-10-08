import allure
from utils.API_Pet_Categories import Pet_Demo_Project_api
from utils.API_Pets import Pet_Demo_api

"""Создание , изменение и удаление новой категории животный"""
@allure.epic("Управление категориями животных")
class Test_Pet_Categories():
    @allure.description("Вывод списка категорий животных")
    def test_search_ALL_Pet_Categories(self):
        Pet_Demo_Project_api.get_all_Pet_Categories()
    @allure.description("Создание категории животного")
    def test_create_ID_Pet_Categories(self):
        Pet_Demo_Project_api.post_Pet_Categories()
    @allure.description("Поиск категории животного по ID")
    def test_search_ID_Pet_Categories(self):
        Pet_Demo_Project_api.get_Pet_Categories_for_ID()
    @allure.description("Изменение имени категории животного по ID")
    def test_change_PUT_ID_Pet_Categories(self):
        Pet_Demo_Project_api.put_change_Pet_Categories()
    @allure.description("Удаление категории животного по ID")
    def test_DELETE_ID_Pet_Categories(self):
        Pet_Demo_Project_api.DELETE_Pet_Categories()

"""Создание , изменение и удаление новых животных"""
@allure.epic("Управление животными")
class Test_Pets():
    @allure.description("Вывод списка животных")
    def test_search_ALL_Pets(self):
        Pet_Demo_api.get_all_Pets()
    @allure.description("Создание животного")
    def test_create_ID_Pet(self):
        Pet_Demo_api.post_Pet()
    @allure.description("Поиск животного по ID")
    def test_search_ID_Pet(self):
        Pet_Demo_api.get_Pet_for_ID()
    @allure.description("Изменение имени животного по ID")
    def test_change_PUT_ID_Pet(self):
        Pet_Demo_api.put_change_Pet()
    @allure.description("Удаление животного по ID")
    def test_DELETE_ID_Pet(self):
        Pet_Demo_api.DELETE_Pet()