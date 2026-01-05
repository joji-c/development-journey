word="python programming is very interesting"
list1=word.split()
count=[ch for ch in list1 if len(ch)>5]
print(count)