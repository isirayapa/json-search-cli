from database_operations import json_to_database, clear_database
import pytest
from database_operations import get_data


def test_main():
    json_to_database()
    output = get_data(1, '_id', 71)
    assert output is not None


def test_invalid_class_name():
    with pytest.raises(Exception):
        assert get_data(5, '_id', 71)


def test_invalid_term():
    with pytest.raises(Exception):
        assert get_data(1, 'INVALID_NAME', 71)


def test_invalid_value():
    with pytest.raises(Exception):
        assert get_data(1, '_id', 9999999)
    assert get_data(1, '_id', 9999999) == []


def test_different_value_formats():
    assert get_data(1, '_id', 71)
    assert get_data(1, '_id', '71')


def test_end():
    clear_database()
    output = get_data(1, '_id', 71)
    assert output == []
