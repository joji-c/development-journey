#palindrome is a word that when reversed is the same
def is_palindrome(word):
    word=word.casefold()
    return word==word[::-1]

print(is_palindrome("Malayalam"))
print(is_palindrome("Hello"))
