# mypy: ignore-errors

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "received_input, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779582", "Счет **9582"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 456878ghjk6573875648", "Введен некорректный номер счета"),
        ("Maestro 159683yjvn705199", "Введен некорректный номер карты"),
        ("", "Пожалуйста, введите данные"),
    ],
)
def test_mask_account_card(received_input, expected_result):
    assert mask_account_card(received_input) == expected_result


@pytest.mark.parametrize(
    "received_input, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0004-03-11T02:26:18.6", "11.03.0004"),
        ("2024-03-11T02:26:18", "Введите корректные данные"),
    ],
)
def test_get_date(received_input, expected_result):
    assert get_date(received_input) == expected_result
