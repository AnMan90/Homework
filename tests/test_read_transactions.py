from unittest.mock import mock_open, patch

import pandas as pd

from src.read_transactions import read_fin_trans_csv, read_fin_trans_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="col1;col2\nvol1;vol2\nvol3;vol4",
)
def test_read_fin_trans_csv(mock_file):
    assert read_fin_trans_csv("") == [{"col1": "vol1", "col2": "vol2"}, {"col1": "vol3", "col2": "vol4"}]


@patch("builtins.open")
def test_read_fin_trans_csv_fnf(mock_file, capsys):
    mock_file.side_effect = FileNotFoundError
    read_fin_trans_csv("")
    assert capsys.readouterr().out.strip() == f"Ошибка: файл {""} не найден"


@patch("builtins.open")
def test_read_fin_trans_csv_ex(mock_file, capsys):
    mock_file.side_effect = Exception
    read_fin_trans_csv("")
    assert capsys.readouterr().out.strip() == f"Ошибка:{""}"


@patch("src.read_transactions.pd.read_excel")
def test_read_fin_trans_excel(mock_excel, pending_transactions_new):
    mock_excel.return_value = pd.DataFrame(pending_transactions_new)
    assert read_fin_trans_excel("") == pending_transactions_new


@patch("src.read_transactions.pd.read_excel")
def test_read_fin_trans_excel_fnf(mock_excel, capsys):
    mock_excel.side_effect = FileNotFoundError
    read_fin_trans_excel("")
    assert capsys.readouterr().out.strip() == f"Ошибка: файл {""} не найден"


@patch("src.read_transactions.pd.read_excel")
def test_read_fin_trans_excel_ex(mock_excel, capsys):
    mock_excel.side_effect = Exception
    read_fin_trans_excel("")
    assert capsys.readouterr().out.strip() == f"Ошибка:{""}"
