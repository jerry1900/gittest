# -*- coding:utf-8 -*-
__author__ = '万壑'

# 一个基本的装饰器，将被装饰的函数传入，在装饰器前后进行操作
def simple_decorator(f):
    def wrapper():
        print('Entering Function')

        f()

        print('Exit Function')

    return wrapper

@simple_decorator

def helloWorld():
    print('Hello World')


helloWorld()
