from letters_counter import count_letters
import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [
        pytest.param("Hello world!", (10, 2), id="mixed"),
        pytest.param(".", (0, 1), id="punctuation"),
        pytest.param("a", (1, 0), id="letter"),
        pytest.param("", (0, 0), id="empty"),
    ],
)
def test_count_letters(source_string, result):
    assert count_letters(source_string) == result
