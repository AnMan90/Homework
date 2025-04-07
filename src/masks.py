import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция, принимает на вход номер карты и возвращает ее маску."""
    if not isinstance(card_number, (int, str)):
        logger.error("Введен некорректный номер карты")
        return "Введен некорректный номер карты"
    card_number_str = str(card_number)
    if len(card_number_str) == 16 and card_number_str.isdigit():
        logger.info("Операция выполнена успешно")
        first_num = card_number_str[:4]
        second_num = card_number_str[4:6]
        last_num = card_number_str[-4:]
        return f"{first_num} {second_num}** **** {last_num}"
    elif len(card_number_str) == 0:
        logger.error("Номер карты не введен")
        return "Введите номер карты"
    else:
        logger.error("Введен некорректный номер карты")
        return "Введен некорректный номер карты"


def get_mask_account(account_number: int | str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    if not isinstance(account_number, (int, str)):
        logger.error("Введен некорректный номер счета")
        return "Введен некорректный номер счета"
    account_number_str = str(account_number)
    if len(account_number_str) == 20 and account_number_str.isdigit():
        logger.info("Операция выполнена успешно")
        return f"**{account_number_str[-4:]}"
    elif len(account_number_str) == 0:
        logger.error("Номер счета не введен")
        return "Введите номер счета"
    else:
        logger.error("Введен некорректный номер счета")
        return "Введен некорректный номер счета"
