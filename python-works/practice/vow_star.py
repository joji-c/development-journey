class VowStar:
    def __init__(self,strin):
        self.strin=strin
        self.nl=[]
        for s in self.strin:
            if s in "aeiou":
                s="*"
                self.nl.append(s)
            else:
                self.nl.append(s)
        print("".join(self.nl))
    
instance=VowStar("how are you")