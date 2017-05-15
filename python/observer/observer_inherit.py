# -*- coding:utf-8 -*-
__author__ = '万壑'

class Button(object):
    def __init__(self):
        self.observer_list = []
        self.register(playMusic)
        self.register(showMessage)

    def register(self,func):
        self.observer_list.append(func)

    def unregister(self,func):
        self.observer_list.remove(func)

    def on_lick(self):
        for func in self.observer_list:
            func()

class childButton(Button):
    def __init__(self):
        super(childButton, self).__init__()
        super(childButton, self).register(showCarton)


def playMusic():
    print 'Play Music'

def showMessage():
    print 'Show Message'

def showCarton():
    print 'Show Carton'

if __name__ == '__main__':
    newButton = Button()
    newButton.on_lick()

    anotherButton = childButton()
    anotherButton.on_lick()