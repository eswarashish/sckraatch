from abc import ABCMeta, abstractmethod

# for a class we  can only create one object

class IPerson(metaclass =ABCMeta):

    @staticmethod
    @abstractmethod
    def get_data():
        """implement in child class"""
        pass

class PersonSingleton(IPerson):
    __instance = None # this will only 
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance ==None:
            raise Exception(" No instance initiated currently")
        return PersonSingleton.__instance

    def __init__(self,name,age):
        if PersonSingleton.__instance != None:
            raise Exception(" Singleton cannot be instantiated more than once")
        self.name = name
        self.age = age
        PersonSingleton.__instance = self
    @staticmethod
    def get_data():
        print(f"Name :{PersonSingleton.__instance.name} Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike",30)
print(p)
print(p.get_data())

# p2 = PersonSingleton("bob",20)
#   File "C:\Users\ashis\Downloads\sckraatch\python_adv\singleton.py", line 23, in __init__
#     raise Exception(" Singleton cannot be instantiated more than once")        
# Exception:  Singleton cannot be instantiated more than once

p2 = PersonSingleton.get_instance()
print(p2)# p1,p2 refer to same