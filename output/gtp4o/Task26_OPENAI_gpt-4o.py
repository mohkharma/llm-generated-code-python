def find_odd_occurrence(arr):
    result = 0
    for number in arr:
        result ^= number
    return result

print(find_odd_occurrence([7]))
print(find_odd_occurrence([0]))
print(find_odd_occurrence([1, 1, 2]))
print(find_odd_occurrence([0, 1, 0, 1, 0]))
print(find_odd_occurrence([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))