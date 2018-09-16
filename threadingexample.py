#!usr/bin/env python3
#-*-coding:utf-8 -*-

import threading,time

count = 0
class MyThread(threading.Thread):
    def _init_(self, threadName):
        super(MyThread, self)._init_(name=threadName)

    def run(self):
        global count
        for i in range(100):
            count = count + 1
            time.sleep(0.3)
            print(self.getName(), count)


for i in range(2):
    MyThread("MyThreadName:" + str(i)).start()
