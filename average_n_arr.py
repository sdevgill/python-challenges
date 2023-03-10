# Oldie method
# def find_avg(arr):
#     total = 0
#     for i in range(len(arr)):
#         total += arr[i]
#     return total / len(arr)

# Best solution

# Without using indexes
def find_avg(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)


# With enumerate
# def find_avg(arr):
#     total = 0
#     for i, num in enumerate(arr):
#         total += num
#     return total / len(arr)

# Time Complexity: O(n)
# Space Complexity: O(1)

print(find_avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_avg([2, 4, 6, 8, 10]))
print(find_avg([10, 20, 30, 40, 50, 60, 70, 90, 100]))
