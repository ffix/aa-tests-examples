# Примеры к лекции по тестированию в Python

Из корня репозитория выполните:

```sh
uv sync --locked
uv run python -m pytest -q
```

Проект использует Python 3.13, pytest 8.4.2 и Hypothesis 6.146.0.

| Демонстрация | Команда из корня |
| --- | --- |
| unittest | `uv run python -m unittest discover -s tasks/tests -p test_count_letters_unit.py` |
| Фикстуры | `uv run python -m pytest -q tasks/tests/test_shared_report.py tasks/tests/test_fixture_tools.py` |
| Faker | `uv run --with Faker==37.12.0 python -m pytest -q extra/test_profile.py` |
| Mock | `uv run --with requests==2.32.5 python -m pytest -q tasks/tests/mock_example_test.py` |
| Coverage | `uv run --with pytest-cov==7.0.0 --with coverage==7.13.0 python -m pytest -q tasks/tests/test_count_letters_cov.py --cov=letters_counter` |
| doctest с несовпадением пробелов | `uv run python -m doctest tasks/tests/letters_counter_doctest_bad.py` |
| doctest с нормализацией | `uv run python -m doctest -o NORMALIZE_WHITESPACE -v tasks/tests/letters_counter_doctest_bad.py` |
| Hypothesis | `uv run python -m pytest -q extra/test_sort.py extra/sort_bad.py` |
| Исходное правило | `uv run python -m pytest -q policy/tests/` |
| Готовая мутация | `uv run python -m pytest -q policy/boundary/test_policy.py` |
| mutmut | `uv run --with mutmut==3.4.0 mutmut run` |

Для практики возьмите [morse.py](practice-morse/morse.py). Напишите тесты в файле `practice-morse/test_morse.py` и запустите из корня:

```sh
uv run python -m pytest -q practice-morse/test_morse.py
```

### Практика без uv

Для Морзе достаточно Python 3.13 и pytest. Из корня репозитория выполните команды для своей системы.

**macOS и Linux**

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install pytest==8.4.2
.venv/bin/python -m pytest -q practice-morse/test_morse.py
```

**Windows PowerShell**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest==8.4.2
.\.venv\Scripts\python.exe -m pytest -q practice-morse/test_morse.py
```

Дефектные версии запускаются по явному пути. Для mutmut нужна система с поддержкой `fork`, например macOS, Linux или WSL.
