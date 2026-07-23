stock = {}

try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)
except FileNotFoundError:
    print("No stock file found. Starting with an empty inventory.")

def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount

while True:
    print("\n1. Update Stock")
    print("2. Show Low Stock")
    print("3. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Item name: ")

        try:
            amount = int(input("Change in quantity (+/-): "))
            adjust(item, amount)
            print("Stock updated.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        low_stock = [item for item, qty in stock.items() if qty < 10]

        print("\nLow Stock Items:")
        if low_stock:
            for item in low_stock:
                print(f"{item}: {stock[item]}")
        else:
            print("No low-stock items.")

    elif choice == "3":
        with open("stock.txt", "w") as file:
            for item, qty in stock.items():
                file.write(f"{item},{qty}\n")
        print("Inventory saved.")
        break

    else:
        print("Invalid option.")