def filter_by_currency(transactions, currency_code):
    """Функция должна возвращать итератор,
     который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    description = ""
    for transaction in transactions:
        if transaction["description"] == "Перевод организации":
            description = transaction["description"]
        elif transaction["description"] == "Перевод со счета на счет":
            description = transaction["description"]
        elif transaction["description"] == "Перевод с карты на карту":
            description = transaction["description"]
        yield description


def card_number_generator(start=1, stop=9999999999999999):
    """Генератор, который выдает номера банковских карт."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"




