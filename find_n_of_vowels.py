def count_vowels(str):
    counter = 0
    lower_str = str.lower()
    for i in range(len(lower_str)):
        char = lower_str[i]
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            counter += 1
    return counter

print(count_vowels("Hello, world!")) # should print 3
print(count_vowels("This is a test")) # should print 4
print(count_vowels("abcdefghijklmnopqrstuvwxyz")) # should print 5
print(count_vowels("AEIOU")) # should print 5
print(count_vowels("")) # should print 0
