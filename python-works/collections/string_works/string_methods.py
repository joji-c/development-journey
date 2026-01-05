#here we see the most commonly used methods in string
company_name1 = "luMinar"
print(company_name1.capitalize())#first cap all other small

company_name2 = "LUMINAR"
print(company_name2.casefold())#all small

text1="12345"
print(text1.isdigit()) #checks if the string contains digit or not (only 0-9)

text2="asdf"
print(text2.isalpha()) #checks if the string contains alphabet or not (only a-z)

text3="asdf12345"
print(text3.isalnum()) #checks if the string contains both digit and alphabet  (0-9 or a-z)

name1="python programming python programming is simple"
      #0123456789
print(name1.index("pro")) #here we use index to find the first occurance index of the given substring
#in index if the substring is not found an error is shown and tthe code is stopped

name2="python programming python programming is simple"
      #0123456789
print(name2.find("no")) #here the find has the same use as index, but if the substring is not found then instead 
# of an error it gives the user a value of -1 and does not stop the program like the index method
print(name2.find("on",19,26))
#syntax of find = .find(substr,start,stop)
#if we give start and stop value it searches within those range for that substr ,if not then it check the full string

name3="python programming python programming is simple"
print(name3.rfind("ing")) #here the find startrs searching from the right side and finds the last occurance
#of a given substring

word1="#friedrice#"
print(word1.strip("#")) #here the given substr is removed from both sides
print(word1.lstrip("#")) #here the given substr is removed from the left side only
print(word1.rstrip("#")) #here the given substr is removed from the right side only

text4="python is a dynamically typed language"
words2=text4.split(" ")#here we split the text into multiple ones and store them in a list from each seperation given
print(words2)

text5="python.is.a.dynamically.typed.language"
words3=text5.split(".")
print(words3)

text6="programming"
words4=text6.count("g")  #count help count the number of occurances of the given substr
print(words4)