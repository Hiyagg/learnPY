#   lambda_func

#!/usr/bin/env python3
# -*- coding: utf-8 -
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1=time.time()
        s=fn(*args,**kw)
        t2=time.time()
        print('%s executed in %s ms' % (fn.__name__, t2-t1))
        return s
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 小结问题

def log(x='call'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                if callable(x):
                    print('begin call %s' % func.__name__)
                else:
                    print('%s %s' % (x,func.__name__))
                s=func(*args,**kw)
                print('end call %s' % func.__name__)
                return s
            return wrapper
        if callable(x):
            return decorator(x)
        else:
            return decorator

@log            #实际上等于fun1 = log(fun1)
def fun1(x,y):
    return x*y
@log('execute') #实际上等于fun2 = log('execute')(fun2)
def fun2(x,y):
    return x*y
print(fun1(8,9),fun2(9,9))


