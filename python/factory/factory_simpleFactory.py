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

class SimpleFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        pizzas = dict(cheese=CheesePizza,vegetable=VegetablePizza,normal=NormalPizza)
        return pizzas[pizza_type]()

class PizzaStore(object):
    def order_pizza(self,pizza_type):

        self.pizza= SimpleFactory.create_pizza(pizza_type)

        self.pizza.pizza_make()


if __name__ == '__main__':
    pizzaStore = PizzaStore()
    pizzaStore.order_pizza('vegetable')