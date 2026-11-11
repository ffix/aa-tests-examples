import pytest

from letters_counter import count_letters


@pytest.fixture
def hello_world():
    return "Hello, world"


def test_hello_world(hello_world):
    assert count_letters(hello_world) == (10, 2)
