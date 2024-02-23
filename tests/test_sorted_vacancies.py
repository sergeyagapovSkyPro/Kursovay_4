import pytest
from src.sorted_vacancies import SortedVacancies
from src.connection_hh import HeadHunter


@pytest.fixture
def get_head_hunter():
    return HeadHunter("python", 1)


def test_head_hunter_sorted():
    r = SortedVacancies()
    assert r.head_hunter_sorted == []
    assert r.date_format == None


def test_sorted_vacancies():
    r = SortedVacancies()
    assert r.sorted_vacancies == [{'city': 'Санкт-Петербург',
                                   'data': '26.01.2024',
                                   'name': 'Middle Python Developer',
                                   'payment_from': 100000,
                                   'payment_to': 120000,
                                   'skill_1': 'От 2-х лет коммерческого опыта, знаешь что такое SOLID, DRY, '
                                              'KISS, интересуешься паттернами проектирования. Знаешь '
                                              '<highlighttext>Python</highlighttext> 3.8. ',
                                   'skill_2': 'Участвовать во всех этапах разработки в составе scrum-команды: '
                                              'собирать и анализировать требования, декомпозировать и оценивать '
                                              'задачи, писать код, релизить...'}]


def test_error_sorted_vacancies():
    with pytest.raises(TypeError):
        SortedVacancies(100)