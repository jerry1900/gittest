#-*-coding:utf8-*-
__author__ = '万壑'

import threading
import Queue
import copy
import time

def job(l,q):
    res = sum(l)
    q.put(res)

def normal(l):
    total = sum(l)
    print(total)

def multithreading(l):
    q = Queue.Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job,args=(copy.copy(l),q))
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print total

if __name__ == '__main__':
    l = list(range(100000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)

    s_t = time.time()
    multithreading(l)
    print('Multithreading: ', time.time() - s_t)
