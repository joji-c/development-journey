"""
slicing is extracting a portion from an object

syntax
result=object[start:stop:step]            

#start is 0 by default
#stop is len-1 by default
#step is 1 by default

"""

company_name="luminar technolab"
word0=company_name[8:12]
word1=company_name[:7]  #if no start is given by default it will start from 0
word2=company_name[8:]  #if no stop is given by default it will go till the end of the line
word3=company_name[::2] #it will go from 0 to the end with skipping one char as step is 2
word4=company_name[::-1] #here the object will be reversed
word5=company_name[:] #the full object from 0 to till len-1 is taken

print(word0)
print(word1)
print(word2)
print(word3)
print(word4)
print(word5)
