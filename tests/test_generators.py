import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(pending_transactions_new):
    fil_by_cur = filter_by_currency(pending_transactions_new, "PEN")
    assert next(fil_by_cur) == {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
    fil_by_cur = filter_by_currency(pending_transactions_new, "EUR")
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
