def foo(text):
    return len(text)


def show(func):
    size = func("zen of python")
    print("length of string is: %s" %size)


def nick():
    return foo


def get_length(text):     # get_length()-->new_text = clean(text) --> clean(t)
    def clean(t):
        return t[1:]
    new_text = clean(text)
    return len(new_text)


class Add:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x


if __name__ == '__main__':
    print(foo("zen of python"))
    print(id(foo))
    print(type(foo))

# func as object 
    bar = foo
    print("bar func lenth is %d" %bar("zen of python"))

# func can be put in container
    func = [foo, str, len]
    for i in func:
        print(i('hello'))

# func as parameter
    show(foo)
    

# func can be return by function
    print( "func can be return by function")
    re = nick()
    print(re("zen of python"))

# func can be embedded
    print("func can be embeded")
    print(get_length("python"))

# if class has __call__ method, instance can be used as func
    print("if class has __call__ method, instance can be used as func")
    add = Add(1)
    print(add(4))