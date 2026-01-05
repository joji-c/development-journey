from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def start(self):
        print("Swift starts")
    def accelerate(self):
        print("Swift accelerate")
    def stop(self):
        print("Swift stops")

car_instance=Swift()
car_instance.start()
car_instance.accelerate()
car_instance.stop()
