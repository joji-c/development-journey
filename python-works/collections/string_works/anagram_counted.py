def anagram(word1,word2):
    is_anagram=True
    if len(word1)!=len(word2):
        return False
    for ch in word1:
        count_word1=word1.count(ch)
        count_word2=word2.count(ch)
        if count_word1!=count_word2:
            is_anagram=False
            break
    return is_anagram

print(anagram("silent","listen"))
