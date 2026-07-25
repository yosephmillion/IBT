stock = {}

try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet — starting empty")


def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


adjust("Vitamin C", -2)
adjust("Paracetamol", 10)
adjust("Aspirin", 12)

low_stock = [item for item, qty in stock.items() if qty < 10]

print("Current Stock:")
for item, qty in stock.items():
    print(item, "-", qty)

print("\nLow Stock:", low_stock)

with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}")