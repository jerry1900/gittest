# -*- coding:utf-8 -*-
__author__ = '万壑'

class Button(object):
    def __init__(self):
        self.observer_list = []

    def register(self,func):
        self.observer_list.append(func)

    def unregister(self,func):
        self.observer_list.remove(func)

    def on_lick(self):
        for func in self.observer_list:
            func()

def playMusic():
    print 'Play Music'

def showMessage():
    print 'Show Message'

if __name__ == '__main__':
    newButton = Button()
    newButton.register(playMusic)
    newButton.register(showMessage)

    newButton.on_lick()