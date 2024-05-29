from datetime import datetime
from functions import load_operations, get_operations, mask_account, mask_card_number


def main():
    for op in get_operations(load_operations()):
        date = datetime.fromisoformat(op["date"]).strftime("%d.%m.%Y")
        description = op["description"]
        from_account = op["from"]
        to_account = op["to"]

        if 'Счет' in from_account:
            from_account = f"Счет {mask_account(from_account.split()[-1])}"
        else:
            from_account = mask_card_number(from_account.split()[-1])

        if 'Счет' in to_account:
            to_account = f"Счет {mask_account(to_account.split()[-1])}"
        else:
            to_account = mask_card_number(to_account.split()[-1])

        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        return f'''{date}{description}
{from_account} -> {to_account}
{amount} {currency}'''


if __name__ == '__main__':
    main()
