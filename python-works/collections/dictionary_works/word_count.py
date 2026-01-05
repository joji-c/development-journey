words=["hai","hello","hai","hello","python"]
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)

#python only way
"""
words=["hai","hello","hai","hello","python"]
word_count={}
for w in words:
    word_count[w]=words.count(w)
print(word_count)
"""
