#coding:utf-8

# decorator is a function or class which can add extra feature to the function
# then the function cannot be change any way.

def foo():
    print("foo")
    
print("**this is a raw func which print foo ")
foo()
# if we want to add some log info

def foo():
    print("foo")
    print("log info")

print("**add log info")
foo()
# I didn't want to add print("log info") into to every function

def foo():
    print("foo")
    
print("**this is a raw func which print foo ")


def use_logging(func):
    func()
    print("log info")

print("**add log into to func, then call func()")
use_logging(foo)

# this changed raw foo, should use use_loggin(), use decorator to use raw foo,
# but also have log info

def use_logging(func):
    def wrapper():
        func()
        print("log info")
    return wrapper

def foo():                                     # can add @
    print("foo")
print("** raw decorator to foo")
foo = use_logging(foo)  # foo=wrapper          # can ommit assignment
foo()   # wrapper(foo)

# if use @ at begging of function, then can ommit assignment


def use_logging(func):
    def wrapper():
        func()
        print("log info")
    return wrapper

@use_logging
def foo():
    print("foo")

print("** add @ to raw decorator to foo")
foo()   # wrapper(foo)

# if foo function have parameters

def use_logging(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("log info")
    return wrapper

@use_logging
def foo(name ,**kwargs):
    print("foo")
    print("my name is %s" %(name))
    for key in kwargs:
        if key is 'weight':
            weight = kwargs[key]
        elif key is 'height':
            height = kwargs[key]
        elif key is 'age':
            age = kwargs[key]
        
    print("my weight is %d, height is %d, age is %d" %(weight, height, age))

print("** add @ *args, **kwargs to raw decorator to foo")
#foo('terry', age=30, **{'weight': 62, 'height': 170})   # wrapper(foo)
foo('terry', age=30, weight=62, height=170)   # wrapper(foo)

# decorator have parameter @decorator(a)
# only add wrapper function to contain these code
# raw is decoratory func, but now at first should have one parameter
# func()-->wraper()-->decortaor()-->using_logging()
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                print('log is warn')
            elif level == 'info':
                print('log is info')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@use_logging(level="warn")
def foo(name ,**kwargs):
    print("foo")
    print("my name is %s" %(name))
    for key in kwargs:
        if key is 'weight':
            weight = kwargs[key]
        elif key is 'height':
            height = kwargs[key]
        elif key is 'age':
            age = kwargs[key]
        
    print("my weight is %d, height is %d, age is %d" %(weight, height, age))

print("** decorator have parameter @decorator(a)")
foo('terry', age=30, weight=62, height=170)   # wrapper(foo)

# class can be decorator, dependency __call__, if one class have this method,
# instance can used as function 
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decortaor running')
        self._func()
        print('class decorator ending')

@Foo
def bar():
    print('bar')
print("**using class as decorator, func as init, then call it")
bar()

# functools.wraps
# decorator will hide raw 

def use_logging(func):
    def wrapper():
        print("log info")
        print(func.__name__)
        print(func.__doc__)
        return func()
    return wrapper

@use_logging
def foo():                                     # can add @
    print("foo")
print("print raw func.__name__, func.__doc__")
foo()



