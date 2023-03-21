from classes.order import Order

class Customer:
    
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and ( 1 <= len(name) <= 15):
            self._name = name
        else:
            print("must be string ")

    def orders(self):
        orders_list = []
        for order in Order.all:
            if order.customer == self:
                orders_list.append(order)
        return orders_list

    def coffees(self):
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list


     # def __init__(self, customer, coffee, price)
    def create_order(self, coffee, price):
        Order(self, coffee, price)
