def filter_by_state(list_dict: list[dict[str, str | int]], filter_key: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filter_by_state_list = []
    for dict_state in list_dict:
        if dict_state["state"] == filter_key:
            filter_by_state_list.append(dict_state)
    return filter_by_state_list


def sort_by_date(list_dict_sort: list[dict[str, str | int]], descending: bool = True) -> list[dict[str, str | int]]:
    """Функция должна возвращать новый список, отсортированный по дате."""
    list_dict_sort.sort(key=lambda dict_date: dict_date["date"], reverse=descending)
    return list_dict_sort
