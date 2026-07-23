customers = {}
try:
    with open("transactions.txt") as file:
        for line in file:
            name, amount = line.strip().split(",")
            amount = int(amount)

            customers[name] = customers.get(name, 0) + amount

except FileNotFoundError:
    print("transactions.txt was not found.")
    exit()

sorted_customers = sorted(
    customers.items(),
    key=lambda item: item[1],
    reverse=True
)
print("Transaction Summary")
print("-------------------")

for name, total in sorted_customers:
    print(f"{name}: {total} ETB")

    file.write("Transaction Summary\n")
    file.write("-------------------\n")

    for name, total in sorted_customers:
        file.write(f"{name}: {total} ETB\n")

print("\nReport saved to report.txt")