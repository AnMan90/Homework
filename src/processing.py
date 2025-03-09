def filter_by_state(
    accepted_lst: list[dict[str, str | int]], filter_key: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filtered_by_state_lst = []
    for dict_state in accepted_lst:
        if dict_state["state"] == filter_key:
            filtered_by_state_lst.append(dict_state)
    return filtered_by_state_lst


def sort_by_date(sortable_lst: list[dict[str, str | int]], descending: bool = True) -> list[dict[str, str | int]]:
    """Функция должна возвращать новый список, отсортированный по дате."""
    sortable_lst.sort(key=lambda dict_date: dict_date["date"], reverse=descending)
    return sortable_lst
