def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
key = 30

result = linear_search(numbers, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the list")
