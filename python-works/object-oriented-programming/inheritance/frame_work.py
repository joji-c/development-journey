class Framework:
    name:str
    language:str
    architecture:str

    def set_framework(self,name,language,architecture):
        self.name=name
        self.language=language
        self.architecture=architecture
    def display(self):
        print("Framework name:",self.name)
        print("Framework language:",self.language)
        print("Framework architecture:",self.architecture)
        print()
    
django=Framework()
django.set_framework("django","python","MVT")
django.display()

angular=Framework()
angular.set_framework("angular","typescript","ng model")
angular.display()

asp=Framework()
asp.set_framework("asp","c#","asp.net")
asp.display()
