from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах и маскировать их."""
    if len(account_card) == 0:
        return "Пожалуйста, введите данные"
    elif account_card[:4] == "Счет":
        if account_card[5:].isdigit():
            return f"{account_card[:4]} {get_mask_account(int(account_card[5:]))}"
        else:
            return "Введен некорректный номер счета"
    else:
        if account_card[-16:].isdigit():
            return f"{account_card[:-17]} {get_mask_card_number(int(account_card[-16:]))}"
        else:
            return "Введен некорректный номер карты"


def get_date(date: str) -> str:
    """Функция форматирования даты."""
    if len(date) < 20:
        return "Введите корректные данные"
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
