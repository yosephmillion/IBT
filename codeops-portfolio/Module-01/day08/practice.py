#Exercise 1
def total(nums):
    if not nums:
        return 0
    return nums[0] + total(nums[1:])


def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)


numbers = [100, 250, 400]

print("Total:", total(numbers))

count_down(5)

#Exercise 2
def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


balances = [500, 1000, 1500, 2000, 2500]

print(binary_search(balances, 2000))
print(binary_search(balances, 3000))

#Exercise 3
import random


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


numbers = [random.randint(1, 100) for _ in range(10)]

print(numbers)
print(merge_sort(numbers))
print(sorted(numbers))

#Exercise 4
accounts = [
    ("Almaz", 2500),
    ("Dawit", 1800),
    ("Hanna", 3200),
    ("Sara", 1500)
]

sorted_accounts = sorted(
    accounts,
    key=lambda account: account[1],
    reverse=True
)

print(sorted_accounts)

#Exercise 5
def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1

    return False


numbers = [2, 4, 6, 8, 10, 12]

print(has_pair(numbers, 14))
print(has_pair(numbers, 25))
