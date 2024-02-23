import pytest
from src.vacancies import Vacancies


@pytest.fixture()
def get_vacancies():
    return Vacancies("pathon", 1)


def test_str(get_vacancies):
    assert str(get_vacancies) == "pathon"


def test_repr(get_vacancies):
    assert repr(get_vacancies) == "Vacancies(('pathon', 1)"


def test_name_error(get_vacancies):
    with pytest.raises(AttributeError):
        get_vacancies.name = "Hello"
