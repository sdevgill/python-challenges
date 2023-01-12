# Distinct List

# Have the function DistinctList(arr) take the array of numbers stored in arr and determine the total number of duplicate entries. For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are two duplicates of one of the elements.

# Examples
# Input: [0,-2,-2,5,5,5]
# Output: 3
# Input: [100,2,101,4]
# Output: 0

# -------------------------------------------------------------

# Solution 1 - Built in method

# def DistinctList(arr):
#     return len(arr) - len(set(arr))

# The function uses the built-in Python set data structure to remove duplicate elements from the input array. A set is a collection of unique elements, so when converting the input array to a set, it will remove any duplicate elements.

# Then, the function calculates the number of duplicate elements by subtracting the length of the unique elements (the set) from the length of the original array. It returns the result.

# This solution is efficient in terms of both time and space complexity. The time complexity is O(n) because the set object in Python uses a hash table internally and the average case of adding an element to a set is O(1) and worst-case is O(n) in the worst case scenario where all the elements are distinct.

# The space complexity of this function is also O(n) where n is the length of the input array. This is because the function uses a set data structure to remove duplicates, which can store up to n elements in the worst case scenario where all elements are distinct.

# It's worth mentioning that this function assumes that the input is a list of integers, it doesn't check for the correct format of the input.

# ---------------------------------------------------------------

# Solution 2 - Using a dictionary


def DistinctList(arr):
    # Initialize an empty dictionary
    dictionary = {}
    # Initialize a counter to keep track of the number of duplicates
    count = 0
    # Iterate through each element in the array
    for num in arr:
        # Check if the element is already in the dictionary
        if num in dictionary:
            # If the element is already in the dictionary, increment the counter
            count += 1
        else:
            # If the element is not in the dictionary, add it to the dictionary
            dictionary[num] = 1
    # Return the number of duplicates
    return count


# Time Complexity: O(n)
# Space Complexity: O(n)


print(DistinctList([0, -2, -2, 5, 5, 5]))  # 3
print(DistinctList([100, 2, 101, 4]))  # 0
print(DistinctList([1, 2, 2, 2, 3]))  # 2
