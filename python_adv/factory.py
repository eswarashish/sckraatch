# if something is an INterface start withh I letter and thhere cant be instances for that interface
from abc import ABCMeta, abstractmethod


class IPerson(metaclass = ABCMeta):
    @staticmethod
    @abstractmethod
    def person():
        """Interface method which means this cannot be used; signature/blueprint
        this is just mentioning each Iperson sublass"""
        pass
    

# p1= IPerson()
# p1.person()
#     p1= IPerson()
# TypeError: Can't instantiate abstract class IPerson without an implementation for abstract method 'person'

# so we need to Implement this abstract class first

class Stud(IPerson):
    def person():
        print("Im a student")

stud = Stud()
Stud.person()
#stud.person() will make this to pass self
stud.person
# above would work

