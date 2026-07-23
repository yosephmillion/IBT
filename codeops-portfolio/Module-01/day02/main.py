account = [
    {"name": "Abel", "balance": 500},
    {"name": "Yoseph", "balance": 1000},
    {"name": "John", "balance": 200},
    {"name": "Lisa", "balance": 250},
    {"name": "Mark", "balance": 300}
]

def account_type(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    elif balance >= 100:
        return "Basic"

for person in account:
    print(person["name"], person["balance"], account_type(person["balance"]))


