class str_methods:
    def __init__(self,stingr):
        self.stingr=stingr
        self.count=0
        for i in self.stingr:
            if i.isalpha():
                self.count+=1
        print(self.count)
            
stingr_instance=str_methods("how are you")