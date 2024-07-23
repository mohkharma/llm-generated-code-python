def find_even_index(arr):
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i
    return -1

arr = [1, 2, 3, 4, 3, 2, 1]
result = find_even_index(arr)
print(result) # Output: 3