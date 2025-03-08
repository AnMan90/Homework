def filter_by_state(list_dict: list[dict[str, str | int]], filter_key: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filter_by_state_list = []
    for dict_state in list_dict:
        if dict_state["state"] == filter_key:
            filter_by_state_list.append(dict_state)
    return filter_by_state_list


def sort_by_date(list_dict_sort: list[dict[str, str | int]], descending: bool = True) -> list[dict[str, str | int]]:
    """ Функция должна возвращать новый список, отсортированный по дате. """
    list_dict_sort.sort(key=lambda dict_date: dict_date["date"], reverse=descending)
    return list_dict_sort


if __name__ == "__main__":
    lst = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(lst))
    print(sort_by_date(lst, False))