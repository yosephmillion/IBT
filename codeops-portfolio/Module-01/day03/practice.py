# Exercise 1 

cities = [
    "Addis Ababa",
    "Adama",
    "Addis Ababa",
    "Hawassa",
    "Adama",
    "Bahir Dar"
]

unique_cities = set(cities)

print("Unique Cities:")
print(unique_cities)
print("Count:", len(unique_cities))


# Exercise 2 

prices = {
    "Bread": 50,
    "Milk": 80,
    "Eggs": 120,
    "Sugar": 90,
    "Rice": 150
}

print("\nPrice Report")
for item, price in prices.items():
    print(f"{item}: {price} ETB")


# Exercise 3 

prices_list = [100, 250, 400, 80]

with_tax = [price * 1.15 for price in prices_list]

print("\nPrices with Tax:")
print(with_tax)


# Exercise 4 

cheap_items = [price for price in prices_list if price < 200]

print("\nCheap Items:")
print(cheap_items)

#Exercise 5 

with open("names.txt", "w") as file:
    file.write("John\n")
    file.write("Alice\n")
    file.write("David\n")

print("\nReading names.txt")

with open("names.txt") as file:
    for line in file:
        print(line.strip())


# Exercise 6 

try:
    number = int(input("\nEnter a number: "))
    result = 1000 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program Finished")