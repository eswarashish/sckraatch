# Interface segregation principle
# In the below example for online and paypal methods lets say both need a method called otp_validation
# So this common properties makes us to segregate subclasses from the main Interface

import random
from enum import Enum
from abc import ABC, abstractmethod

class Method(Enum):
    online = "online"
    offline = "offline"

class WarehouseItem:
    def __init__(self,id):
        self.__id = id
    def get_prince(self):
        return random.random()
    @property
    def name(self):
        return str(self.__id)        

class Item:

    def __init__(self,id):
        self._item_id = id
        self.warehouse_item = WarehouseItem(id)
        self.name = self.warehouse_item.name
        self.price = self.warehouse_item.get_prince()
    

   
class Order:

    def __init__(self,items:list[Item]):
        self.items = items
        self.price = 0
    def order_price(self):
        for item in self.items:
            self.price += item.price
        return self.price
    

class Payment(ABC):

    def __init__(self,order:Order,amount:float,):

        self.order = order
        self.amount= amount
    @abstractmethod
    def process(self):
        """Implement in every subclass"""
        pass


class OTPPayment(Payment):
    @abstractmethod
    def otp_validation(self,otp):
        """Method for otp validation"""
        pass
class OnlinePayment(OTPPayment):
    def __init__(self, order, amount,):
        super().__init__(order, amount)
        self.verified = False
    def otp_validation(self, otp):
        self.verified = True
    def process(self):
        """since it is an online mode exact amount will be deducted"""
        if self.verified: return  f"Purchase of {self.order.order_price()} successful in online method"
        else: return f"Otp invalid"
class OfflinePayment(Payment):
    def __init__(self, order, amount):
        super().__init__(order, amount)
    def process(self):
         to_pay = self.order.order_price()
         if self.amount>to_pay:
            return f"Purchase successful change of {self.amount-to_pay} returned"
         else: raise ValueError(f"{to_pay-self.amount} more to be paid")

# lets take an example of paypal processing

class PaypalPayment(Payment):
    def __init__(self, order, amount
                 ,# since using email in other methods breaks liskov we need to take in init itself
                 email:str
                 ):
        super().__init__(order, amount)
        self.email = email
        self.verified = False
    def otp_validation(self, otp):
        self.verified = True
    def process(self
               # ,email:str
                ):
        if self.verified: return  f"Purchase of {self.order.order_price()} successful with paypal {self.email}" 
        else: return f"Otp invalid"
        # This actually violates the liskov principle because we cannot subsitite this class' object with its parent object
        # Parent method breaks 
# 

if __name__=='__main__':
    item_1 = Item('apple')
    item_2 = Item('orange')
    order = Order([item_1,item_2])
    payment = PaypalPayment(order=order,amount=1000.0,email="ashish@gmail.com")
    payment.otp_validation(3453)
    print(payment.process())

# So instead of one general interface more meaningful interface segregation can help to build complex systems easily


        
    
