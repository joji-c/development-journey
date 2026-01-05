class WordC:
    def __init__(self,strin):
        self.strin=strin
        self.list=self.strin.split(" ")
        self.di={}
        for l in self.list:
            if l in self.di:
                self.di[l]+=1
            else:
                self.di[l]=1
        print(self.di)
    
instance=WordC("she sells sea shells at the sea shore")