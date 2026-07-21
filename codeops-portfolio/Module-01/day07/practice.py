#Exercise 1
# 1. List Index
numbers = [10, 20, 30, 40]
print(numbers[2])      # O(1) - Direct index access

# 2. Single Loop
for i in numbers:
    print(i)           # O(n) - Visits each element once

# 3. Nested Loop
for i in numbers:
    for j in numbers:
        print(i, j)    # O(n²) - Loop inside another loop

# 4. Dictionary Lookup
accounts = {
    "ACC001": "Almaz",
    "ACC002": "Dawit"
}
print(accounts["ACC001"])   # O(1) - Hash lookup

# 5. Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = list(range(1, 101))
print(binary_search(nums, 73))    # O(log n)

#Exercise 2
import time

accounts_list = []
accounts_dict = {}

for i in range(100000):
    account = f"ACC{i}"
    accounts_list.append(account)
    accounts_dict[account] = account

target = "ACC99999"

start = time.time()
target in accounts_list
end = time.time()
print("List:", end - start)

start = time.time()
accounts_dict.get(target)
end = time.time()
print("Dictionary:", end - start)

#Exercise 3
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()

names = ["Almaz", "Dawit", "Hanna"]

for name in names:
    stack.push(name)

reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print(reversed_names)

#Exercise 4
from collections import deque

queue = deque()

customers = [
    "Almaz",
    "Dawit",
    "Hanna",
    "Sara",
    "Abel"
]

for customer in customers:
    queue.append(customer)

while queue:
    print("Serving:", queue.popleft())

#Exercise 5
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_all(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


linked = LinkedList()

linked.push_front("Hanna")
linked.push_front("Dawit")
linked.push_front("Almaz")

linked.print_all()

