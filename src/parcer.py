from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_params(self, keyword: str):
        """
        Абстрактный метод для поиска вакансий с разных платформ.
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        Абстрактный метод для получения вакансий с разных платформ.
        """
        pass


class HH(AbstractAPI):
    """Класс для работы с API hh.ru"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_params(self, keyword: str):
        """
        Подготовка параметров для запроса к сервису
        keyword: str значение для поиска в полях вакансий
        """
        params = {
            'per_page': 100,
            'page': 1,
            'text': keyword
        }
        return params

    def get_vacancies(self, vacant_name):
        """
        Метод для поиска вакансий через HeadHunter API
        и записи их в список
        """
        params = self.get_params(keyword=vacant_name)
        result = requests.get(url=self.__url, params=params)
        result_json = result.json()
        return result_json.get("items", [])