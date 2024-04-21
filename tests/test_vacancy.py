import pytest
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        name="Software Engineer",
        url="https://example.com",
        description="Experience with Python and Django",
        salary_from=50000,
        salary_to=80000,
        currency="USD"
    )


def test_vacancy_attributes(sample_vacancy):
    assert sample_vacancy.name == "Software Engineer"
    assert sample_vacancy.url == "https://example.com"
    assert sample_vacancy.description == "Experience with Python and Django"
    assert sample_vacancy.salary_from == 50000
    assert sample_vacancy.salary_to == 80000
    assert sample_vacancy.currency == "USD"


def test_is_salary():
    assert Vacancy.is_salary(50000) == 50000
    assert Vacancy.is_salary(None) == 0


def test_lt():
    vacancy1 = Vacancy(name="A", url="", description="", salary_from=50000, salary_to=None, currency="")
    vacancy2 = Vacancy(name="B", url="", description="", salary_from=60000, salary_to=None, currency="")
    assert vacancy1 < vacancy2


def test_le():
    vacancy1 = Vacancy(name="A", url="", description="", salary_from=50000, salary_to=None, currency="")
    vacancy2 = Vacancy(name="B", url="", description="", salary_from=60000, salary_to=None, currency="")
    assert vacancy1 <= vacancy2


def test_eq():
    vacancy1 = Vacancy(name="A", url="", description="", salary_from=50000, salary_to=None, currency="")
    vacancy2 = Vacancy(name="B", url="", description="", salary_from=50000, salary_to=None, currency="")
    assert vacancy1 == vacancy2


def test_cast_to_object_list():
    vacancy_list = [
        {
            "name": "Software Engineer",
            "alternate_url": "https://example.com",
            "snippet": {"requirement": "Experience with Python and Django"},
            "salary": {"from": 50000, "to": 80000, "currency": "USD"}
        },
        {
            "name": "Data Scientist",
            "alternate_url": "https://example.com",
            "snippet": {"requirement": "Experience with data analysis"},
            "salary": None
        }
    ]
    vacancies = Vacancy.cast_to_object_list(vacancy_list)
    assert len(vacancies) == 2
    assert vacancies[0].name == "Software Engineer"
    assert vacancies[0].salary_from == 50000
    assert vacancies[0].salary_to == 80000
    assert vacancies[1].name == "Data Scientist"
    assert vacancies[1].salary_from == 0
    assert vacancies[1].salary_to == 0
