#coding:utf-8

#location actual/formal parameter
def func_location(x,y):   # x y formal parameter
    print(x,y)


#keywords  actual parameter
def func_keyword(x,y,z):
    print(x,y,z)


#default  formal parameter
def func_default(x, y=10):
    print(x,y)


#variable lenth
def func_variable(*args):
    print(args)

#variable lenth keyworkd
def func_variable_key(**kwargs):
    print(kwargs)

# how to recognize args or kwargs
def func_variable_args_key(name, **kwargs):
    print(name)
    print(kwargs)
# *
def func_name(*, name, age):
    print(name, age)

if __name__ == '__main__':
    func_location(1,2)    # 1 2 actual parameter

    func_keyword(1, z=2,y=3) # keywords 

    func_default(1)    # default y is 10
    func_default(1,2)

    func_variable(1,2,3)  #variable lenth
    a = (3,4,5)
    func_variable(*a)

    func_variable_key(x=1, y=2)
    func_variable_key(**{'a':3,'b':4})

    func_variable_args_key(1,y=2)

    func_name(name='terry', age=30)
