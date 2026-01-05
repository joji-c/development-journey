from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def create_module_and_package(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):
    def create_module_and_package(self):
        print("vs code creates modules and packages")
    def edit(self):
        print("vs code edits")
    def execute(self):
        print("vs code executes")
    def debug(self):
        print("vs code debugs")

editor_instance=Vscode()
editor_instance.create_module_and_package()
editor_instance.edit()
editor_instance.execute()
editor_instance.debug()
