def palindrome(words):
    pal=[]
    for w in words:
        if w==w[::-1]:
            pal.append(w)
    return pal

words=["malayalam","cat","act","madam","racecar"]
print(palindrome(words))