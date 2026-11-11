from letters_counter import count_letters


def test_hello_world():
    assert count_letters("Hello world!") == (10, 2)


def test_empty_string():
    assert count_letters("") == (0, 0)
