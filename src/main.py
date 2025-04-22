import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_fin_trans_csv, read_fin_trans_excel
from src.utils import get_transaction_list, search_for_operations
from src.widget import get_date, mask_account_card

directory_file_path = "../data/"
json_path = "operations.json"
csv_path = "transactions.csv"
xlsx_path = "transactions_excel.xlsx"


def main():
    """Функция, которая отвечает за основную логику проекта
    и связывает функциональности между собой."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        select_file_extension = input("Введите номер пункта: ").strip()
        if select_file_extension == "1":
            current_dir = os.path.dirname(__file__)
            filename_json = os.path.join(current_dir, directory_file_path, json_path)
            print("Для обработки выбран JSON-файл.")
            read_file_out = get_transaction_list(filename_json)
            read_file = []
            for transaction in read_file_out:
                new_transaction = {
                    "id": transaction.get("id", ""),
                    "state": transaction.get("state", ""),
                    "date": transaction.get("date", ""),
                    "amount": transaction.get("operationAmount", {}).get("amount", ""),
                    "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name"),
                    "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code"),
                    "from": transaction.get("from", ""),
                    "to": transaction.get("to", ""),
                    "description": transaction.get("description", ""),
                }
                read_file.append(new_transaction)
            break
        elif select_file_extension == "2":
            current_dir = os.path.dirname(__file__)
            filename_csv = os.path.join(current_dir, directory_file_path, csv_path)
            print("Для обработки выбран CSV-файл.")
            read_file = read_fin_trans_csv(filename_csv)
            break
        elif select_file_extension == "3":
            current_dir = os.path.dirname(__file__)
            filename_xlsx = os.path.join(current_dir, directory_file_path, xlsx_path)
            print("Для обработки выбран XLSX-файл.")
            read_file = read_fin_trans_excel(filename_xlsx)
            break
        else:
            print("Введены некорректные данные. Попробуйте еще раз.")

    print("Выберете статус, по которому необходимо выполнить фильтрацию.")
    statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        filtering_status = (
            input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n" "Введите статус: ").strip().upper()
        )
        if filtering_status in statuses:
            read_file = filter_by_state(read_file, filtering_status)
            break
        else:
            print(f"Статус операции {filtering_status} недоступен.")

    print(f"Операции отфильтрованы по статусу {filtering_status}")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        sorted_by_date = input("Ввод: ").strip().lower()
        if sorted_by_date == "да":
            while True:
                print("Отсортировать:\n 1 - по возрастанию\n 2 - по убыванию")
                sort_date = input("Ввод: ").strip()
                if sort_date == "1":
                    read_file = sort_by_date(read_file)
                    break
                elif sort_date == "2":
                    read_file = sort_by_date(read_file, False)
                    break
                else:
                    print("Введены некорректные данные. Попробуйте еще раз.")
            break
        elif sorted_by_date == "нет":
            break
        else:
            print("Введены некорректные данные. Попробуйте еще раз.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        sorted_by_currency = input("Ввод: ").strip().lower()
        if sorted_by_currency == "да":
            read_file = list(filter_by_currency(read_file, "RUB"))
            break
        elif sorted_by_currency == "нет":
            break
        else:
            print("Введены некорректные данные. Попробуйте еще раз.")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        sort_by_word = input("Ввод: ").strip().lower()
        if sort_by_word == "да":
            word_sort = input("Введите слово:").strip().lower()
            read_file = search_for_operations(read_file, word_sort)
            break
        elif sort_by_word == "нет":
            break
        else:
            print("Введены некорректные данные. Попробуйте еще раз.")

    if len(read_file) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(read_file)}")

        for transaction in read_file:
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            if transaction["description"] == "Открытие вклада":
                print(mask_account_card(transaction["to"]))
            else:
                print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
            print(f"Сумма: {transaction["amount"]} {transaction["currency_name"]}")


main()
