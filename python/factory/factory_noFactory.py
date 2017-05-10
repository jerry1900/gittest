# -*- coding:utf-8 -*-
__author__ = '万壑'

class CheesePizza():
    def pizza_type(self):
        print 'CheesePizza'

class VegetablePizza():
    def pizza_type(self):
        print 'VegetablePizza'

class NormalPizza():
    def pizza_type(self):
        print 'NormalPizza'

class PizzaStore(object):
    def order_pizza(self,pizza_type):
        if pizza_type == 'cheese':
            self.pizza = CheesePizza()
        elif pizza_type == 'vegetable':
            self.pizza = VegetablePizza()
        else:
            self.pizza = NormalPizza()

        self.pizza.pizza_type()


if __name__ == '__main__':
    pizzaStore = PizzaStore()
    pizzaStore.order_pizza('vegetable')