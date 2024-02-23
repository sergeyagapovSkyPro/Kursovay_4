import pytest
from src.connection_hh import HeadHunter


@pytest.fixture
def get_head_hunter():
    return HeadHunter("python", 1)


def test_str(get_head_hunter):
    assert str(get_head_hunter) == "python"


def test_repr(get_head_hunter):
    assert repr(get_head_hunter) == "HeadHunter(python, 1)"


def test_url(get_head_hunter):
    assert get_head_hunter.url == "https://api.hh.ru"


def test_error_connection():
    with pytest.raises(TypeError):
        HeadHunter()