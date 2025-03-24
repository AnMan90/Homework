from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """Функция должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        description = ""
        if (
            transaction.get("description") == "Перевод организации"
            or transaction.get("description") == "Перевод со счета на счет"
            or transaction.get("description") == "Перевод с карты на карту"
        ):
            description = transaction["description"]
        else:
            continue
        yield description


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт."""
    if start > stop:
        start, stop = stop, start
    if start > 0 and stop > 0:
        for number in range(start, stop + 1):
            card_number = f"{number:016d}"
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
