def filter_vacancies(vacancies_data: list, filter_words: str):
    """
    поис вакансии из json по пораметрам пользователя
    :param vacancies_data: берем данные из файла json
    :param filter_words: рапрашиваем слово ключевое у пользоватеоля
    :return:
    """

    filtered_vacancies = []
    for vacancy in vacancies_data:
        for word in filter_words:
            if word.lower() in vacancy.name.lower():
                filtered_vacancies.append(vacancy)
                break  # Прерываем внутренний цикл, чтобы не добавлять вакансию несколько раз
    return filtered_vacancies


def get_vacancies_by_salary(vacancies_data: list, salary_range: str):
    """
    Функция возвращает список вакансий, отфильтрованных по зарплате.
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    ranged_vacancies = []
    for vacancy in vacancies_data:
        if vacancy.salary_from >= min_salary and vacancy.salary_to <= max_salary:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_data: list):
    """
    Эта функция сортирует список вакансий (vacancies_data) по убыванию зарплаты
    :param vacancies_data:
    :return:
    """
    return sorted(vacancies_data, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies_data: list, top_n):
    """
     Она просто возвращает первые N вакансий из списка.
    :param vacancies_data:
    :param top_n:
    :return:
    """
    return vacancies_data[:top_n]
