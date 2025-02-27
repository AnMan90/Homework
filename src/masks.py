def get_mask_card_number(card_number: int | str) -> str:
    """Функция, принимает на вход номер карты и возвращает ее маску."""
    card_number_str = str(card_number)
    first_num = card_number_str[:4]
    second_num = card_number_str[4:6]
    last_num = card_number_str[-4:]
    return f"{first_num} {second_num}** **** {last_num}"


def get_mask_account(account_number: int | str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
