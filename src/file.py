from abc import ABC, abstractmethod
import json


class File(ABC):

    @abstractmethod
    def save_data(self, data):
        """
        Абстрактный метод для сохранения в файл
        """
        pass

    @abstractmethod
    def get_data(self):
        """
        Абстрактный метод загрузки данных из файла
        """
        pass

    @abstractmethod
    def delete_value(self, data):
        """
        Абстрактный метод удаления данных из файла
        """
        pass


class JSONSaver(File):

    def save_data(self, vacancies):
        """
        Функция принимает список объектов класса Vacancy и сохраняет их в JSON-файл.
        :param vacancies: (list[Vacancy]) Список объектов класса Vacancy.
        """
        list_vacancies = []
        for vacancy in vacancies:
            if vacancy.salary_from == 0 and vacancy.salary_to == 0 and vacancy.currency is None:
                vacancies_data = {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "description": vacancy.description,
                    "salary": "Зарплата не указана..."
                }
                list_vacancies.append(vacancies_data)
            else:
                vacancies_data = {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "description": vacancy.description,
                    "salary_from": vacancy.salary_from,
                    "salary_to": vacancy.salary_to,
                    "currency": vacancy.currency
                }
                list_vacancies.append(vacancies_data)

        with open('data/hh.json', "w", encoding='utf-8') as file:
            json.dump(list_vacancies, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """
        Загрузка данных из JSON-файла.
        """
        with open('data/hh.json', 'r', encoding='utf-8', errors='replace') as file:
            return json.load(file)

    def delete_value(self, vacancy_name):
        """
        Удаление вакансии по ключевым словам в названии
        """
        with open('data/hh.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Проверяем наличие вакансии с указанным названием
            found_vacancies = [v for v in data if vacancy_name.lower() in v.get('name').lower()]
            if found_vacancies:
                data = [v for v in data if not(vacancy_name.lower() in v.get('name').lower())]
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                print(f'Вакансии c {vacancy_name} удалены из файла')
            else:
                print(f'Вакансии c {vacancy_name} не найдены')


