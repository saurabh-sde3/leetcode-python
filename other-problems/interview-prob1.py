from abc import ABC, abstractmethod

class Calculator(ABC):
    
    @abstractmethod
    def add(a, b):
        pass
    
    @abstractmethod
    def sub(a, b):
        pass
    
    @abstractmethod
    def mul(a, b):
        pass
    
    @abstractmethod
    def divide(a, b):
        pass
    
class SimpleCalculator(Calculator):
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    
class GenericCalc(SimpleCalculator):
    def percentage():
        pass
    
obj = SimpleCalculator()

print("Addition--> ", obj.add(10, 20))