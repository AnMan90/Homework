def get_mask_card_number(card_number: int | str) -> str:
    """Функция, принимает на вход номер карты и возвращает ее маску."""
    if not type(card_number) is int and not type(card_number) is str:
        return "Введен некорректный номер карты"
    card_number_str = str(card_number)
    if len(card_number_str) == 16 and card_number_str.isdigit():
        first_num = card_number_str[:4]
        second_num = card_number_str[4:6]
        last_num = card_number_str[-4:]
        return f"{first_num} {second_num}** **** {last_num}"
    elif len(card_number_str) == 0:
        return "Введите номер карты"
    else:
        return "Введен некорректный номер карты"


def get_mask_account(account_number: int | str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    if not type(account_number) is int and not type(account_number) is str:
        return "Введен некорректный номер счета"
    account_number_str = str(account_number)
    if len(account_number_str) == 20 and account_number_str.isdigit():
        return f"**{account_number_str[-4:]}"
    elif len(account_number_str) == 0:
        return "Введите номер счета"
    else:
        return "Введен некорректный номер счета"
