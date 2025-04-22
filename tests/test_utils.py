import json
import os
from unittest.mock import patch

from src.utils import get_transaction_list, search_for_operations


def test_get_transaction_list(name_json_file):
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]
    with open(name_json_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    assert get_transaction_list(name_json_file) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]
    if os.path.exists(name_json_file):
        os.remove(name_json_file)


def test_get_transaction_list_json_decode_error(name_json_file):
    with open(name_json_file, "w", encoding="utf-8") as f:
        f.write(str({"name": "руб.", "code": "RUB"}))
    assert get_transaction_list(name_json_file) == []
    if os.path.exists(name_json_file):
        os.remove(name_json_file)


def test_get_transaction_list_type_not_list(name_json_file):
    with open(name_json_file, "w", encoding="utf-8") as f:
        f.write("123")
    assert get_transaction_list(name_json_file) == []
    if os.path.exists(name_json_file):
        os.remove(name_json_file)


def test_get_transaction_list_file_not_found_error():
    assert get_transaction_list("") == []


def test_find_matches(pending_operations):
    result = search_for_operations(pending_operations, "перевод")
    assert len(result) == 2
    assert all("перевод" in t["description"].lower() for t in result)


def test_no_matches(pending_operations):
    result = search_for_operations(pending_operations, "платеж")
    assert len(result) == 0


def test_empty_query(pending_operations):
    result = search_for_operations(pending_operations, "")
    assert len(result) == 3


def test_case_insensitive(pending_operations):
    result = search_for_operations(pending_operations, "ПЕРЕВОД")
    assert len(result) == 2


def test_empty_input():
    result = search_for_operations([], "перевод")
    assert len(result) == 0


@patch("src.utils.re.compile")
def test_search_for_operations_ex(mock_pattern, capsys):
    mock_pattern.side_effect = Exception
    search_for_operations("", "")
    assert capsys.readouterr().out.strip() == f"Внимание! Ошибка {""}! Введены не корректные данные!"
