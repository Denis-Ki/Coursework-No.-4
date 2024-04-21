from src.parcer import HH
from src.vacancy import Vacancy
from src.file import JSONSaver

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()


# Функция для взаимодействия с пользователем
def user_interaction():
    # Получение вакансий с hh.ru в формате JSON по ключевому слову
    search_query = input("Введите поисковый запрос(например Python): ")
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(f"Получено {len(vacancies_list)} вакансий с HeadHunter")

    # for i in range(len(vacancies_list)):
    #     print(vacancies_list[i])

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.save_data(vacancies_list)
    # Удаление информации о вакансиях из файла
    del_keywords = input("Введите ключевые слова для удаления вакансий из файла (например Python Developer): ")
    json_saver.delete_value(del_keywords)

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

# ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
# sorted_vacancies = sort_vacancies(ranged_vacancies)
# top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
# print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
