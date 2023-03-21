from classes.order import Order

class Coffee:
    def __init__(self, name):
        if type(name) == str:
            self._name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            print("already has a name")

    def orders(self):
        orders_list = []
        for order in Order.all:
            if order.coffee == self:
                orders_list.append(order)
        return orders_list

    def customers(self):
        customer_list = []
        for order in self.orders():
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
        
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        price = 0
        for order in self.orders():
            price += order.price
        return price / len(self.orders())



    