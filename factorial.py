def factorial(n):
    counter = 1
    for i in range(1, n + 1):
        counter *= i
    return counter


# Time Complexity: O(n)
# Space Complexity: O(1)


# --------------------------------------------


# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)


# Time Complexity: O(n)
# Space Complexity: O(n)


print(factorial(1))
print(factorial(4))
print(factorial(5))
