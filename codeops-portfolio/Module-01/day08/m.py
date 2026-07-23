numbers = [2, 1, 5, 8, 9, 11, 92, 39, 924, 389, 29, 20, 11, 89, 22, 35, 66, 28, 49, 29, 100, 282, 82, 201, 280, 34, 39, 29, 55]

def merge(left, right):
    result = []
    
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        
        result.extend(left)
        result.extend(right)
        return result
    
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)

print("Sorted list: ", merge_sort(numbers))