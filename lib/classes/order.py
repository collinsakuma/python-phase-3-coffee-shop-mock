
class Order:
    
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if (1 <= price <= 10):
            self._price = price
        else:
            print("Price is not in range")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("Cannont change name")

    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            print("cannot change coffee")
