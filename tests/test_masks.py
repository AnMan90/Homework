# mypy: ignore-errors

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "received_input, expected_result",
    [
        (1456645398751089, "1456 64** **** 1089"),
        (1456645398751089343, "Введен некорректный номер карты"),
        (145664539875, "Введен некорректный номер карты"),
        ("1456645398751089", "1456 64** **** 1089"),
        ("1456645398751089343", "Введен некорректный номер карты"),
        ("145664539875", "Введен некорректный номер карты"),
        ("", "Введите номер карты"),
        ("12345678876543.2", "Введен некорректный номер карты"),
        ("qwertyuiasdfghjk", "Введен некорректный номер карты"),
        ("qwertyuiasdfgh", "Введен некорректный номер карты"),
        ("qwertyuiasdfghjkl", "Введен некорректный номер карты"),
        ({}, "Введен некорректный номер карты")
    ]
)
def test_get_mask_card_number(received_input, expected_result):
    """Функция тестирования кода функции get_mask_card_number."""
    assert get_mask_card_number(received_input) == expected_result


@pytest.mark.parametrize(
    "received_input, expected_result",
    [
        (54671456645398751089, "**1089"),
        (145664539875108934398998, "Введен некорректный номер счета"),
        (145664539875, "Введен некорректный номер счета"),
        ("54671456645398751089", "**1089"),
        ("145664539875108934398998", "Введен некорректный номер счета"),
        ("145664539875", "Введен некорректный номер счета"),
        ("", "Введите номер счета"),
        ("12345678876543.21234", "Введен некорректный номер счета"),
        ("qwertyuiasdfghjkzxcv", "Введен некорректный номер счета"),
        ("qwertyuiasdfgh", "Введен некорректный номер счета"),
        ("qwertyuiasdfghjklzxvvxcx", "Введен некорректный номер счета"),
        ({}, "Введен некорректный номер счета")
    ]
)
def test_get_mask_account(received_input, expected_result):
    """Функция тестирования кода функции get_mask_account."""
    assert get_mask_account(received_input) == expected_result
