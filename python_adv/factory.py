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
# Stud.person()
#stud.person() will make this to pass self

class Student(IPerson):
    def person(self):
        print("Im student")

class Teacher(IPerson):
    def person(self):
        print("Im Teacher")

# the purpose of factory principle is to make sure we build instances of classes on fly like a factory

class PersonFactory:
    @staticmethod # since it need not vary based on arguments
    def build_person(classtype: str):
        if classtype =="Student":
            person = Student()
            return person
        elif classtype == "Teacher":
            person = Teacher()
            return person
        else:
            raise TypeError("Invalid person type")
        

if __name__ =="__main__":
    classtype = input("Enter your person type\n")
    person = PersonFactory.build_person(classtype=classtype)
    try:
        person.person()
    except Exception as e:
        print(e)