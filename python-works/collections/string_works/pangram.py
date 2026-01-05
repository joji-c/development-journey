#check if its pangram or not
#pangram == all alphabets in english
#word="the quick brown fox jumps over the lazy dog"
def pangram(word):
    flag=True
    ALPHABETS="abcdefghijklmnopqrstuvwxyz"
    for ch in ALPHABETS:   #here we are checking each alphabets 
        if ch not in word.casefold() and ch.isalpha():   # and matching them with word to see if all alphabets exist in it
            flag=False
            break
    return flag


print(pangram("the quick brown fox jumps over the lazy dog"))
print(pangram("Hello World"))

