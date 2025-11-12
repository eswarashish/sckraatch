# Liskov substitution principle states that
# Objects of subclasses should be able to replace objects of their parents classes
# which means once subclassses objects replaced it must not break the methods of parent class
# They must be easily seamlessly be substituted

import random
from enum import Enum

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
    

class Payment:

    def __init__(self,order:Order,amount:float,):

        self.order = order
        self.amount= amount
    def process(self):
        pass
class OnlinePayment(Payment):
    def __init__(self, order, amount):
        super().__init__(order, amount)

    def process(self):
        """since it is an online mode exact amount will be deducted"""
        return  f"Purchase of {self.order.order_price()} successful in online method"
    
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

    def process(self
               # ,email:str
                ):
        return  f"Purchase of {self.order.order_price()} successful with paypal {self.email}" 
        # This actually violates the liskov principle because we cannot subsitite this class' object with its parent object
        # Parent method breaks 
# 

if __name__=='__main__':
    item_1 = Item('apple')
    item_2 = Item('orange')
    order = Order([item_1,item_2])
    payment = Payment(order=order,amount=1000.0)
    print(payment.process())



        
    
