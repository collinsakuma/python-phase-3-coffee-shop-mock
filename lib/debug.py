#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    
    coffee = Coffee("Hazelnut Latte")
    coffee_2 = Coffee("Mocha")

    steve = Customer('Steve')
    bob = Customer('Bob')

    order1 = Order(steve, coffee, 10)
    order2 = Order(steve, coffee, 10)
    order3 = Order(bob, coffee_2, 8)


    ipdb.set_trace()
