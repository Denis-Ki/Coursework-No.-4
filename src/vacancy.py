class Vacancy:
    """
    Класс для получения информации о вакансии.
    """

    def __init__(self, name, url, description, salary_from, salary_to, currency):
        self.name = name
        self.url = url
        self.description = description
        self.salary_from = self.is_salary(salary_from)
        self.salary_to = self.is_salary(salary_to)
        self.currency = currency

    def __str__(self):
        return f'Вакансия: {self.name}\n' \
               f'Требования: {self.description}\n' \
               f'Зарплата от {self.salary_from} до {self.salary_to} {self.currency}\n'

    @staticmethod
    def is_salary(value):
        if value:
            return value
        return 0

    def __lt__(self, other):
        """
        Магический метод сравнивает, является ли данный объект класса Vacancy "меньше"
        по размеру заработной платы, относительно заработной платой другого объекта.
        """
        return self.salary_from < other.salary_from

    def __le__(self, other):
        """
        Магический метод сравнивает, является ли данный объект класса Vacancy "меньше или равен"
        по размеру заработной платы, относительно заработной платой другого объекта.
        """
        return self.salary_from <= other.salary_from

    def __eq__(self, other):
        """
        Магический метод сравнивает, "равен" ли данный объект класса Vacancy по размеру заработной платы,
        с заработной платой другого объекта.
        """
        return self.salary_from == other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancy_list):
        """
        Метод преобразования набора данных из JSON в список объектов класса Vacancy
        """
        object_list = []
        for vacancy in vacancy_list:
            if vacancy['salary']:
                object_vacancy = cls(name=vacancy['name'], url=vacancy['alternate_url'],
                                     description=vacancy['snippet']['requirement'],
                                     salary_from=vacancy['salary']['from'],
                                     salary_to=vacancy['salary']['to'],
                                     currency=vacancy['salary']['currency'])
            else:
                object_vacancy = cls(name=vacancy['name'], url=vacancy['alternate_url'],
                                     description=vacancy['snippet']['requirement'],
                                     salary_from=0, salary_to=0, currency=None)
            object_list.append(object_vacancy)
        return object_list

