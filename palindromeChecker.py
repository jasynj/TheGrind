# Given an integer x, return true if x is a palindrome, and false otherwise.

def palindrome(string):
    string = string.strip().lower()
    word = list(string)
    copy = word.copy()
    copy.reverse()

    if word == copy:
        return True
    return False

print(palindrome("121"))
print(palindrome("123"))

