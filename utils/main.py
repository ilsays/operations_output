from datetime import datetime
from functions import load_operations, get_operations, mask_account, mask_card_number


def main():
    """
    Основная работа программы
    """

    for op in get_operations(load_operations()):
        date = datetime.fromisoformat(op["date"]).strftime("%d.%m.%Y")
        description = op.get("description", '')
        from_account = op.get("from", '')
        to_account = op.get("to", '')

        if 'Счет' in from_account:
            from_account = f"Счет {mask_account(from_account)}"
        else:
            from_account = mask_card_number(from_account)

        if 'Счет' in to_account:
            to_account = f"Счет {mask_account(to_account)}"
        else:
            to_account = mask_card_number(to_account)

        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        if op["description"] == "Открытие вклада":
            print(f'''{date} {description}
-> {to_account}
{amount} {currency}''')
        else:
            print(f'''{date} {description}
{from_account} -> {to_account}
{amount} {currency}''')


if __name__ == '__main__':
    main()
