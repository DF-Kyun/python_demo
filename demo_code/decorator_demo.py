import functools

def log(func):
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        func_tmp =  func(*args, **kw)
        print('end call %s():' % func.__name__)
        return func_tmp
    return wrapper



def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s %s():' % (text, func.__name__))
            func_tmp =  func(*args, **kw)
            print('end call %s %s():' % (text, func.__name__))
            return func_tmp
        return wrapper
    return decorator

@log
def now():
    print('2017')


@log1('execute')
def now1():
    print('execute 2017')

now()  
now1()

