import requests


def get_word() -> str:
    result = requests.get("https://example.com/test_case.json").json()
    return result[0]
