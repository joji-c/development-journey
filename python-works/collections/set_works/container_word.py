def cont(word1,word2):
    flag=True
    for w in word2:
        if w not in word1:
            flag=False
            break
        else:
            pass
    return flag
print(cont("racecar","car"))



def container(word1,word2):
    set1=set(word1)
    set2=set(word2)
    is_container=set1.issuperset(set2)
    return is_container       
print(container("racecar","pace"))



"""  or we can do

print(set(word1).issuperset(set(word2)))

"""
