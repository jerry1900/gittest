# -*- coding:utf-8 -*-
__author__ = '万壑'

# 带传参的装饰器
def decorator_factory(enter_message,exit_message):
     def simple_decorator(f):
          def wrapper():
                print enter_message

                f()

                print exit_message

          return wrapper

     return simple_decorator

@decorator_factory('Start','End')
def helloWorld():
    print('Hello World')


helloWorld()
