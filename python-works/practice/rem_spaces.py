class str_meth:
    def __init__(self,strin):
        self.strin=strin
        self.list=self.strin.split(" ")
        self.nl=[]
        for l in self.list:
            if l.isalnum():
                self.nl.append(l)
        self.ns=" ".join(self.nl)
        print(self.ns)

stri_instance=str_meth("hello  how are   you")
