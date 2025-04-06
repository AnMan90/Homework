import json


def get_transaction_list(file_path) -> list[dict]:
    """Функция, которая возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data_file = json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    else:
        if type(data_file) is not list:
            return []
        return data_file
