from src.utils import search_for_operations


def filter_by_state(
    transactions: list[dict[str, str | int]], filter_key: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filtered_by_state_lst = []
    for transaction in transactions:
        if "state" in transaction and transaction["state"] == filter_key:
            filtered_by_state_lst.append(transaction)
    return filtered_by_state_lst


def sort_by_date(transactions: list[dict[str, str | int]], descending: bool = True) -> list[dict[str, str | int]]:
    """Функция должна возвращать новый список, отсортированный по дате."""
    filtered_transactions = []
    for item in transactions:
        if "date" in item:
            filtered_transactions.append(item)
    filtered_transactions.sort(key=lambda dict_date: dict_date["date"], reverse=descending)
    return filtered_transactions


def operation_counter(transactions_list: list, categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    number_of_operations = {}
    for category in categories:
        list_length = len(search_for_operations(transactions_list, category))
        number_of_operations[category] = list_length
    return number_of_operations
