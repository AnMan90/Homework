import json
import logging
import os
import re

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), "../logs", "utils.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_list(file_path) -> list[dict]:
    """Функция, которая принимает путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        logger.info("Операция успешно выполнена.")
        with open(file_path, "r", encoding="utf-8") as f:
            data_file = json.load(f)
    except json.JSONDecodeError as ex:
        logger.error(f"{ex} - ошибка чтения файла.")
        return []
    except FileNotFoundError as ex:
        logger.error(f"{ex} - ошибка. Файл не найден.")
        return []
    else:
        if type(data_file) is not list:
            logger.warning("Несоответствующий формат файла.")
            return []
        return data_file


def search_for_operations(transactions_list: list, search_string: str) -> list:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    try:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        found_transactions = []
        for transaction in transactions_list:
            if pattern.search(transaction.get("description", "")):
                found_transactions.append(transaction)
        return found_transactions
    except Exception as e:
        print(f"Внимание! Ошибка {e}! Введены не корректные данные!")
