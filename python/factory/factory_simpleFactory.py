# -*- coding:utf-8 -*-
__author__ = '万壑'

class CheesePizza():
    def pizza_make(self):
        print 'CheesePizza'

class VegetablePizza():
    def pizza_make(self):
        print 'VegetablePizza'

class NormalPizza():
    def pizza_make(self):
        print 'NormalPizza'

class CarDeliver():
    def deliver_pizza(self):
        print 'Car Deliver Pizza'

class BikeDeliver():
    def deliver_pizza(self):
        print 'Bike Deliver Pizza'

class SimpleFactory(object):
    def __init__(self, pizza_type,deliver_type):
        self.pizza_type = pizza_type
        self.deliver_type = deliver_type

    def create_pizza(self):
        pizzas = dict(cheese=CheesePizza,vegetable=VegetablePizza,normal=NormalPizza)
        return pizzas[self.pizza_type]()

    def deliver_pizza(self):
        deliver_method = dict(car=CarDeliver,bike=BikeDeliver)
        return deliver_method[self.deliver_type]()

class PizzaStore(object):
    def order_pizza(self,pizza_type,deliver_type):
        simpleFactory = SimpleFactory(pizza_type,deliver_type)
        self.pizza= simpleFactory.create_pizza()
        self.pizza.pizza_make()
        self.pizza = simpleFactory.deliver_pizza()
        self.pizza.deliver_pizza()


if __name__ == '__main__':
    pizzaStore = PizzaStore()
    pizzaStore.order_pizza('vegetable','car')