#-*-coding:utf8-*-
__author__ = '万壑'

import threading
def job1():
    global A,lock
    lock.acquire()
    for i in range(30):
            A += 1
            print('job1', str(A))
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 100
        print('job2', str(A))
    lock.release()

if __name__ == '__main__':
    A = 0
    lock = threading.Lock()
    thread1 = threading.Thread(target=job1)
    thread2 = threading.Thread(target=job2)
    thread1.start()
    thread2.start()