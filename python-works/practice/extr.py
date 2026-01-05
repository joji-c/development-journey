class ExtUser:
    def __init__(self,strin):
        self.strin=strin
        print(self.strin.rstrip("@gmail.com"))
    
instance=ExtUser("joji @gmail.com")