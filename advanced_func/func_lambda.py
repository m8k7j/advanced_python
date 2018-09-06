#coding:utf-8


def add2(x,y):
    return x+y


r = lambda x, y : x+y


print(add2(1,2))
print(r(1,2))

list1 = [3,5,-4,-1,0,-2,-6]
r = sorted(list1, key=lambda x : abs(x))  #change to abs than sort
print(r)

# closure is function which is a internal function used variable which 
# in the external function

def outer(x):
    def inner():
        print(x)
    return inner


def my_add(n):
    return lambda x : x+n

add_3 = my_add(3)
print(add_3(7))   # 3+7 
 # n is a local variable, so if func is called, n shouldn't be avaliable.
 # because my_add return one func which used n， so if call that func n will
 # be used again, this is called clousre, local variable can be used external
 # environment

"""
闭包使得变量与函数一同存在，即使这个变量离开了创造它的环境，如x离开了outer， 但仍能与
inner 一起使用，因此另一种说法是闭包使得局部变量在函数外被访问成为可能，
之所以引入闭包，是因为这样我们可以不用去定义x为全局变量，此外闭包允许将函数与某些数据
关联起来，这一点就非常像类，类有自己的属性和方法，方法可以调用属性，形成一个整体，闭包
其实可以说是当一个类中只有一个方法时，用闭包再好不过.
"""

class Add:
    def __init__(self, n):
        self.n = n 
    def sum(self, x):
        return self.n + x

add = Add(3)
add.sum(7)
print (add.sum(7))


def external(n):
    def internal(x):
        return x+n
    return internal

print(external(3)(7))
