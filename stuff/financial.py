"""
financial.py

This code features examples of the Dict datatype and shows off accessing and enumerating Dicts

The following table of transactions is represented as a Dict:

| Amount of Money Transferred | Purchase/Sale | Date of Transaction |
|-----------------------------|---------------|---------------------|
| $100.00                     | Sale          | 2021-01-13          |
| $50.00                      | Purchase      | 2021-01-14          |
| $75.00                      | Sale          | 2021-01-15          |
"""

transactionList = [
    {
        "amount": 100.00,
        "date": "2021-01-14",
        "transaction_type": "sale"
    },
    {
        "amount": 50.00,
        "date": "2021-01-14",
        "transaction_type": "purchase"
    },
    {
        "amount": 75.00,
        "date": "2021-01-15",
        "transaction_type": "sale"
    }
]


def sumup_yesterday(type):
    if type != "sale" and type != "purchase":
        raise TypeError
    sum = 0
    for transaction in transactionList:
        if transaction["transaction_type"] is type and transaction["date"] == "2021-01-14":
            sum += transaction["amount"]
    return sum


def sumup(type):
    if type != "sale" and type != "purchase":
        raise TypeError
    sum = 0
    for transaction in transactionList:
        if transaction["transaction_type"] is type:
            sum += transaction["amount"]
    return sum


print(f"In total you made {sumup('sale')} and spent {sumup('purchase')}")

print(f"Yesterday (2021-01-14) you made {sumup_yesterday('sale')} and spent {sumup_yesterday('purchase')}")
