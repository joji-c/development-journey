class strin_check:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
        if str2.casefold() in str1.casefold():
            print("Yes the given string contains the word:",str2)
        else:
            print("No the given string contains the word:",str2)

string_instance=strin_check("good morning how are you","are")