#anagram both words have the same ch
def anagram(word1,word2):
    s_word1=sorted(word1)
    s_word2=sorted(word2)
    return s_word1==s_word2

print(anagram("act","cat"))
print(anagram("silent","listen"))
print(anagram("blue","bblue"))
