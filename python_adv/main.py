# Encapsulation; turning the complex structure easy by capsuling all the properties of it
#Bundling Data and Methods: A class in Python naturally encapsulates data and methods.
#Encapsulation in Python, a core principle of Object-Oriented Programming (OOP), involves bundling data (attributes) and methods (functions) that operate on that data into a single unit, typically a class.
# a class is an example of encapsulation as it binds all the data members (instance variables) and methods into one single unit


class Person:

    def __init__(self, name, age, gender):
        self.__name =name,
        self.__age = age# two underscores set them private 
        self._gender = gender #protected

    @property # getter so this helps you to access those private or protected variables
    def Name(self):
        return self.__name
    # usage person.Name

    # setter
    @Name.setter # if not used we would get that the method Name is already defined
    def Name(self,value):
        self.__name = value

    # static methods - no need to add tihs tag to definetly add staticmethods but best practice
    @staticmethod #its a method that works irrespective of the object so no need to pass self
    def mymethod():
        print("Static Method")
    # usage
    # Person.mymethod()
    # p1.method() would not work since we pass self



    
    