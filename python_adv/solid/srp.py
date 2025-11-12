# Open Close
# Software entities like classes, modules and functions should be open for extension but closed for modification
# This means you can add new functionality without changing existing code

# Item class, Order class, payment class

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

    def __init__(self,order:Order,amount:float,
                # method:str, here if a new payment method like bitcoin or barbaric system is added then we have to change the entire code so we have to create different payment classes for different methods
                 ):

        self.order = order
        self.amount= amount
        # if method == Method.online | Method.offline:
        #     self.method = method
        # else:
        #     raise TypeError(f"Only acceptable payment methods {Method}")

    def process(self):

        
        pass
        # if self.amount>to_pay:
        #     return f"Purchase successful change of {self.amount-to_pay} returned"
        # else: raise ValueError(f"{to_pay-self.amount} more to be paid")

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


if __name__=='__main__':
    item_1 = Item('apple')
    item_2 = Item('orange')
    order = Order([item_1,item_2])
    payment = Payment(order=order,amount=1000.0)
    print(payment.process())



        
    
