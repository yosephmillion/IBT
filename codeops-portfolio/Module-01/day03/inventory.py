stock = {}

try:
    with open("stock.txt") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file found. Starting with an empty inventory.")



def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


print("\nCurrent Inventory")
for item, qty in stock.items():
    print(f"{item}: {qty}")



item = input("\nEnter medicine name: ")
amount = int(input("Enter quantity to add (+) or remove (-): "))

adjust(item, amount)


print("\nUpdated Inventory")
for item, qty in stock.items():
    print(f"{item}: {qty}")


low_stock = [item for item, qty in stock.items() if qty < 10]

print("\nLow Stock Items")
if low_stock:
    for item in low_stock:
        print(item)
else:
    print("No low stock items.")


with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nInventory has been saved successfully.")