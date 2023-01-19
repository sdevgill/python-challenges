def factorial(n):
    counter = 1
    for i in range(1, n + 1):
        counter *= i
    return counter


print(factorial(1))
print(factorial(4))
print(factorial(5))


# Time Complexity: O(n)
# Space Complexity: O(1)
