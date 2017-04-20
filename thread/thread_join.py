#-*-coding:utf8-*-
__author__ = '万壑'

import threading
import time

def thread_job():
    print 'thread job1 start\n'
    for i in range(10):
        time.sleep(0.1)
    print 'thread job1 finish\n'

def thread_job2():
    print 'thread job2 start\n'
    for i in range(5):
        time.sleep(0.05)
    print 'thread job2 finish\n'

if __name__ == '__main__':
    thread1 = threading.Thread(target=thread_job, name='job1')
    thread2 = threading.Thread(target=thread_job2, name='job2')

    thread1.start()
    thread1.join()

    # 加入join()后，只有当该线程运行完成之后，才会执行join之后的代码

    thread2.start()
    thread2.join()

    print 'All done\n'
