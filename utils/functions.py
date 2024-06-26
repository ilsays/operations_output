import json
from datetime import datetime


def load_operations():
    """
    Загрузка json-файла с данными по операциям
    """

    with open('operations.json', encoding='utf-8') as file:
        return json.load(file)


def mask_card_number(card_number):
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX
    """

    return f'{card_number[:-16]}{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}'


def mask_account(account_number):
    """
    Маскирует номер cчета а формате **XXXX
    """

    return f'**{account_number[-4:]}'


def get_operations(operations):
    """
    Фильтрация и сортировка выполненных операций, и их вывод
    """

    executed_operations = [op for op in operations if op and op["state"] == "EXECUTED"]
    executed_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)
    last_operations = executed_operations[:5]
    return last_operations
