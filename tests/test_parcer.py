from src.parcer import HH
import pytest

@pytest.fixture
def hh_api():
    return HH()


def test_get_params(hh_api):
    keyword = "python"
    params = hh_api.get_params(keyword)
    assert params['per_page'] == 100
    assert params['page'] == 1
    assert params['text'] == keyword


def test_get_vacancies(hh_api):
    vacant_name = "python developer"
    vacancies = hh_api.get_vacancies(vacant_name)
    assert isinstance(vacancies, list)
    for vacancy in vacancies:
        assert isinstance(vacancy, dict)
        assert 'name' in vacancy
        assert 'url' in vacancy
        assert 'salary' in vacancy
