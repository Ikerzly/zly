#!usr/bin/env python3
#-*-coding:utf-8 -*-

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func._name_)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func_name_))
            return func(*arg,**kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)