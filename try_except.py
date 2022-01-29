def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome(1))
except TypeError:
    print("You are just allowed to write letters: ")