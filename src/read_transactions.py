import csv

import pandas as pd


def read_fin_trans_csv(path_csv) -> list[dict]:
    """Функция для считывания финансовых операций из csv-файлов
    и возврата данных в виде списка словарей"""
    try:
        with open(path_csv, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        print(f"Ошибка: файл {path_csv} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


def read_fin_trans_excel(path_excel) -> list[dict]:
    """Функция для считывания финансовых операций из excel-файлов
    и возврата данных в виде списка словарей"""
    try:
        transactions_list = pd.read_excel(path_excel)
        transactions_list = transactions_list.fillna("")
        list_of_dicts = transactions_list.to_dict("records")
        return list(list_of_dicts)
    except FileNotFoundError:
        print(f"Ошибка: файл {path_excel} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
