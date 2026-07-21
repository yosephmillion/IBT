# -----------------------------
# Exercise 1 - Temperature Label
# -----------------------------

temperature = int(input("Temperature (°C): "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")


# -----------------------------
# Exercise 2 - Receipt Loop
# -----------------------------

for i in range(1, 11):
    print(f"Receipt #{i}")


# -----------------------------
# Exercise 3 - Even Numbers
# -----------------------------

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# -----------------------------
# Exercise 4 - Discount Function
# -----------------------------

def apply_discount(price, percent=10):
    discount = price * (percent / 100)
    final_price = price - discount
    return final_price


print(apply_discount(1000))
print(apply_discount(1000, 20))


# -----------------------------
# Exercise 5 - Countdown
# -----------------------------

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Liftoff!")