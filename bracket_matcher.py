# Bracket Matcher

# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

# Examples
# Input: "(coder)(byte))"
# Output: 0
# Input: "(c(oder)) b(yte)"
# Output: 1


def BracketMatcher(str):
    # Initialize an empty stack
    stack = []
    # Iterate through each character in the string
    for char in str:
        # If the character is an open bracket, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a close bracket
        elif char == ")":
            # Check if the stack is empty
            if not stack:
                # If the stack is empty, it means there is a close bracket without a corresponding open bracket
                return 0
            # Pop the last open bracket from the stack
            stack.pop()
    # Check if the stack is empty
    if not stack:
        # If the stack is empty, it means all brackets are matched
        return 1
    # If the stack is not empty, it means there are unbalanced open brackets
    return 0


print(BracketMatcher("(hello (world))"))
print(BracketMatcher("((hello (world))"))
print(BracketMatcher("(coder)(byte))"))
print(BracketMatcher("(c(oder)) b(yte)"))

# Time Complexity: O(n)
# Space Complexity: O(n)

# The time complexity of this function is O(n) where n is the length of the input string. This is because the function iterates through each character in the string once and performs a constant amount of operations on each character.

# The space complexity of this function is O(n). The function uses an additional data structure, the stack, which stores at most n/2 elements (in the worst case scenario where every other character is an open bracket). Therefore, the maximum space required is proportional to the size of the input string.

# In the best case scenario, where there's no bracket in the string, the function will return 1 with O(1) time and space complexity.


# This function uses a stack data structure to keep track of the open brackets. At each iteration, the function checks the current character, if it's an open bracket, it pushes it to the stack. If it's a closed bracket, it checks if the stack is empty or not. If the stack is empty, it means that there is a closed bracket without a corresponding open bracket and returns 0. If the stack is not empty, it pops the last open bracket from the stack. After iterating through the entire string, if the stack is empty, it means that all the brackets have been correctly matched, so the function returns 1. Otherwise, it means that there are unbalanced open brackets, so the function returns 0.
