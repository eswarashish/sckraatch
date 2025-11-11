from abc import ABCMeta, abstractmethod
# Proxy design pattern involves wrapping up proxy functionality aroud the actual class

class IPerson(metaclass  = ABCMeta):
    @staticmethod
    @abstractmethod
    def person_method():
        """Interface method for the IPerson Interface"""
        pass

class Person(IPerson):
    def person_method(self):
        print("Im a person")

# so this like a security layer for each method of the class which implements interface
class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()
    def person_method(self):
        print("Im a prxoy functionality")
        self.person.person_method()
    
p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
