class StrEnd:
    def __init__(self,string,str1):
        self.str1=str1
        self.string=string
        if self.string.endswith(str1):
            print("Yes")
        else:
            print("No")

instance=StrEnd("how are you","you")
instance=StrEnd("how are you","are")