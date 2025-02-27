from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах и маскировать их."""
    if account_card[:4] == "Счет":
        return f"{account_card[:4]} {get_mask_account(int(account_card[5:]))} "
    else:
        return f"{account_card[:-17]} {get_mask_card_number(int(account_card[-16:]))}"


def get_date(date: str) -> str:
    """Функция форматирования даты."""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
