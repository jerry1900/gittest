#-*-coding:utf8-*-
__author__ = '万壑'

import threading

def thread_job():
    print 'Threading hello world'

def main():
    thread = threading.Thread(target=thread_job,)
    thread.start()

if __name__ == '__main__':
    main()
