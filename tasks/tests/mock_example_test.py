from mock_example import get_word

from unittest.mock import patch


def test_get_cases():
    with patch("mock_example.requests.get") as mocked_get_cases:
        mocked_get_cases.return_value.json = lambda: ("Hello world!", (10, 2))
        assert get_word() == "Hello world!"
        mocked_get_cases.assert_called_once()
