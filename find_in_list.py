def find(arr, n):
    for i in range(len(arr) - 1):
        if arr[i] == n:
            return f"Found the number {n}!"
    return f"{n} not found.."


# Time Complexity: O(n)
# Space Complexity: (1)

print(find([1, 3, 5, 7, 9], 5))
print(find([2, 4, 6, 8, 10], 5))
print(find([10, 20, 30, 40, 50], 20))
