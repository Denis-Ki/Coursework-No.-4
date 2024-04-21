import pytest
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy

@pytest.fixture
def sample_vacancies():
    return [
        Vacancy(name="Software Engineer", url="", description="", salary_from=60000, salary_to=None, currency="USD"),
        Vacancy(name="Data Scientist", url="", description="", salary_from=70000, salary_to=None, currency="USD"),
        Vacancy(name="Web Developer", url="", description="", salary_from=50000, salary_to=None, currency="USD"),
        Vacancy(name="Project Manager", url="", description="", salary_from=80000, salary_to=None, currency="USD"),
    ]


def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["software", "data"])
    assert len(filtered) == 2
    assert all(vacancy.name in ["Software Engineer", "Data Scientist"] for vacancy in filtered)


def test_get_vacancies_by_salary(sample_vacancies):
    ranged = get_vacancies_by_salary(sample_vacancies, "60000-80000")
    assert len(ranged) == 3
    assert all(vacancy.name in ["Software Engineer", "Data Scientist", "Project Manager"] for vacancy in ranged)


def test_sort_vacancies(sample_vacancies):
    sorted_vacancies = sort_vacancies(sample_vacancies)
    assert [vacancy.name for vacancy in sorted_vacancies] == ["Project Manager", "Data Scientist", "Software Engineer", "Web Developer"]


def test_get_top_vacancies(sample_vacancies):
    top_vacancies = get_top_vacancies(sample_vacancies, 2)
    assert len(top_vacancies) == 2
    assert [vacancy.name for vacancy in top_vacancies] == ["Software Engineer", "Data Scientist"]
