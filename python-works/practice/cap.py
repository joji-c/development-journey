class StrCap:
    def __init__(self,strin):
        self.strin=strin
        self.list=self.strin.split(" ")
        self.nl=[]
        for l in self.list:
            l=l.capitalize()
            self.nl.append(l)
        self.ns=" ".join(self.nl)
        print(self.ns)
        
instance=StrCap("how are you")