#Exercise 1
cities = [
    "Addis Ababa",
    "Adama",
    "Hawassa",
    "Adama",
    "Bahir Dar",
    "Addis Ababa"
]

unique_cities = set(cities)

print("Unique cities:")
for city in unique_cities:
    print(city)

print("Count:", len(unique_cities))

prices = {
    "Bread": 50,
    "Milk": 80,
    "Eggs": 120,
    "Sugar": 95,
    "Rice": 150
}

#Exercise 2
for item, price in prices.items():
    print(f"{item}: {price} ETB")


#Exercise 3
prices = [100, 250, 400, 80]

with_tax = [price * 1.15 for price in prices]

print(with_tax)

#Exercise 4
prices = [100, 250, 400, 80]

cheap_items = [price for price in prices if price < 200]

print(cheap_items)

#Exercise 5
with open("names.txt", "w") as file:
    file.write("Abel\n")
    file.write("Sara\n")
    file.write("Daniel\n")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())

#Exercise 6
try:
    number = int(input("Enter a number: "))
    result = 1000 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program finished.")

