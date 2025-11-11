from abc import ABCMeta, abstractmethod
# a strcutural pattern thhat groups objects like a tree is composite design pattern
class IDepartment(metaclass = ABCMeta):
    @staticmethod
    @abstractmethod
    def __init__(self,employees):
        """implement in the class"""

    @staticmethod
    @abstractmethod
    def print_department():
        """implement in the class"""
    
class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department have {self.employees}")


class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development department have {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_dep:list[IDepartment] = []
    
    def add(self,depts: list[IDepartment]):
        for dept in depts:
         self.sub_dep.append(dept)
         self.employees += dept.employees 

    def print_department(self):
        print("Parent department")
        print(f"Base employees: {self.base_employees}")
        for dept in self.sub_dep:
            dept.print_department()
        print(f"Total employee: {self.employees}")
        
p = ParentDepartment(200)
a = Accounting(20)
d = Development(100)

p.add([a,d])
p.print_department()