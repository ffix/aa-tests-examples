from letters_counter import count_letters
import pytest

def test_rejects_non_string():
    with pytest.raises(TypeError):
        count_letters(None)
