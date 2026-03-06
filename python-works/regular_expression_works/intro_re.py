import re

text1="it is raining in spain"
print("num of 'in' in text1 :",len(re.findall("in",text1)))
print("")

text2="i have 5 apple and i love eating apple"
print("num of 'apple' in text2 :",len(re.findall("apple",text2)))
print("change apple with orange :",re.sub("apple","orange",text2))
print("")

text3="ml$ is$ a$ subset$ of AI"
print("num of '$' in text3 :",len(re.findall("$",text3)))
print("change $ with null :",re.sub("$","",text3)) 
print("")

text4="i@ have# 2 Bike @and 3 Car#"
pattern="[a-z]"
print("all lowercase in text4 :",re.findall(pattern,text4))
pattern="[A-Z]"
print("all uppercase from text4 :",re.findall(pattern,text4))
pattern="[a-zA-Z]"
print("all alphabets from text4 :",re.findall(pattern,text4))
pattern="[0-9]"
print("all numbers from text4 :",re.findall(pattern,text4))
pattern="[a-zA-Z0-9]"
print("all alphanumerics from text4 :",re.findall(pattern,text4))
print("")

pattern="[^a-zA-Z0-9]"
print("all special characters from text4 :",re.findall(pattern,text4))
pattern="[^a-zA-Z0-9]"
print("remove all special charcters from text4 :",re.sub(pattern,"",text4))
pattern="[^a-zA-Z0-9 ]"
print("remove all special charcters except space from text4 :",re.sub(pattern,"",text4))
