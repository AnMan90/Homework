# Homework

## Описание:

Homework - Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/AnMan90/Homework.git
```
2. Установите зависимости:
```
poetry install
```

## Тестирование

Код проекта протестирован с помощью "Pytest". Отчет о покрытии кода содержится в директе htmlcov.

## Модуль Generators

Модуль `generators` предоставляет функции для работы с массивами транзакций. Он включает в себя следующие функции:

- `filter_by_currency(transactions, currency)`: фильтрует транзакции по заданной валюте и возвращает итератор.
- `transaction_descriptions(transactions)`: генератор, возвращающий описания транзакций.
- `card_number_generator(start, stop)`: генератор, который выводит номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.

### Примеры использования:

```python
# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)

# Пример использования transaction_descriptions
for description in transaction_descriptions(transactions):
    print(description)

# Пример использования card_number_generator
for card in card_number_generator(4000123456789010, 4000123456789015):
    print(card)
```

## Модуль decorators

Модуль 'decorators' включает в себя декоратор log, который будет автоматически логировать начало
и конец выполнения функции, а также ее результаты или возникшие ошибки.

### Примеры использования:

```python
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```
### Ожидаемый вывод 
 В лог-файл mylog.txt 
 при успешном выполнении:

 my_function ok

 Ожидаемый вывод при ошибке:

 my_function error: тип ошибки. Inputs: (1, 2), {}

 Где тип ошибки заменяется на текст ошибки.


## Модуль utils
 
### Реализована функция "get_transaction_list", 
которая принимает на вход путь до JSON-файла и возвращает список словарей с
данными о финансовых транзакциях. Если файл пустой,
содержит не список или не найден, функция возвращает пустой список.


## Модуль external_api
### Реализована функцию "get_transaction_amount",
которая принимает на вход транзакцию и возвращает сумму транзакции 
в рублях. Если транзакция была в "USD" или "EUR", происходит обращение 
к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.
Для конвертации валюты воспользуйтесь Exchange Rates Data API: 
### https://apilayer.com/exchangerates_data-api.


## .env.sample
### Шаблон .env-файла 
вложенный в корень проекта, который содержит все необходимые сведения для оперирования 
конфиденциальными данными и области их применения.



