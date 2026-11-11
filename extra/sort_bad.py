from collections import Counter

from hypothesis import given, strategies as st

def my_sort(values: list[int]) -> list[int]:
    return []

@given(st.lists(st.integers()))
def test_sort_preserves_and_orders_values(values):
    result = my_sort(values)

    assert result == sorted(result)
    assert Counter(result) == Counter(values)
