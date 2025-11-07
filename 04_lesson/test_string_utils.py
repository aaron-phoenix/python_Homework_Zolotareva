import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("test", "Test"),
    ("test yourself", "Test yourself"),
    ("pytest", "Pytest"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" test", "test"),
    ("  test yourself", "test yourself"),
    ("   pytest", "pytest")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("test", "t"),
    ("test yourself", "t"),
    ("pytest", "t")
])
def test_contains_positive(input_str, symbol):
    string_utils = StringUtils()
    res = string_utils.contains(input_str, symbol)
    assert res == True


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("testk", "k", "test"),
    ("test wyourself", "w", "test yourself"),
    ("pythest", "h", "pytest")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("test ", "test "),
    ("te st", "te st"),
    ("t e s t", "t e s t")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("test", "u"),
    ("test yourself", "w"),
    ("pytest", "v")
])
def test_contains_negative(input_str, symbol):
    string_utils = StringUtils()
    res = string_utils.contains(input_str, symbol)
    assert res == False


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "", ""),
    ("123", "1", "23"),
    (" ", "", " ")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
