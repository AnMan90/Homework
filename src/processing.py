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
