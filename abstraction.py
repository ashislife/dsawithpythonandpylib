from abc import ABC, abstractmethod


class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")

    @abstractmethod
    def speed(self):
         pass

class Maruti(Car):
    def speed(self):
        print("Speed is 100 km/h")


class Suzuki(Car):
    def speed(self):
        print("Speed is 156 km/h")



obj=Maruti()
obj.show()
obj.speed()

obj1=Suzuki()
obj1.show()
obj1.speed()
