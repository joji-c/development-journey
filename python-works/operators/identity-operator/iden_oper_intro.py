"""
identity operator ( is ): it checks weather the variables point to the same object

note:if the value is same only in case of string the object is the same 
but every other data type creates a new object even for similar values

in : checks if an object exists within a sequence(membership operator)
== : checks if the values are similar(equality operator)
is : checks if variable point to the same object
"""

person_from_kakanad = "abin"
person_from_chavakad = "abin"
print(person_from_chavakad == person_from_kakanad) #true as it has same value
print(person_from_chavakad is person_from_kakanad) #true as it is a string this is a unique case only for string type

person_from_kakanad = ["abin"]
person_from_chavakad = ["abin"]
print(person_from_chavakad == person_from_kakanad) #true as it has same value
print(person_from_chavakad is person_from_kakanad) #false as they have diff objects due to being list type
