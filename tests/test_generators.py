import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(pending_transactions):
    fil_by_cur = filter_by_currency(pending_transactions, "USD")
    assert next(fil_by_cur) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    fil_by_cur = filter_by_currency(pending_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(fil_by_cur)
    fil_by_cur = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(fil_by_cur)


def test_transaction_descriptions(pending_transactions):
    trans_desc = transaction_descriptions(pending_transactions)
    assert next(trans_desc) == "Перевод организации"
    assert next(trans_desc) == "Перевод со счета на счет"
    trans_desc = transaction_descriptions([{}])
    with pytest.raises(StopIteration):
        next(trans_desc)


def test_card_number_generator():
    card_num_gen = card_number_generator(12, 13)
    assert next(card_num_gen) == "0000 0000 0000 0012"
    card_num_gen = card_number_generator(13, 12)
    assert next(card_num_gen) == "0000 0000 0000 0012"
    card_num_gen = card_number_generator(-11, -6)
    with pytest.raises(StopIteration):
        next(card_num_gen)
