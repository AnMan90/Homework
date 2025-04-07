import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_list(file_path) -> list[dict]:
    """Функция, которая возвращает список словарей с данными о финансовых транзакциях."""
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
