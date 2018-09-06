import asyncio

def eager_range(up_to):
    """
    Create a list of integers,
    from 0 to up_to, exclusive.
    """
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence

# if using eager_range， range number very large,
# memory will be exausted.

def lazy_range(up_to):
    """
    Generator to return the sequence of integers
    from 0 to up_to
    """
    index = 0
    while index < up_to:
        yield index
        index += 1

# function will be stash when yield index, until using next() method

def jumping_range(up_to):
    """
    Generator for the sequence of integers from 0 to up_to,
    Sending a value into the generator will shft the sequence
    by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

# send will give function different jump value

def lazy_range_new(up_to):
    """
    Generator to return the sequence of integers from 0 to up_to
    """
    def gratuitous_refactor():
        index = 0
        while index < up_to:
            yield index 
            index += 1
    yield from gratuitous_refactor()

# directly return itertor's every value, not affact by send

def bottom():
    """
    return the yild lets the value that goes up the call stack
    to come right back down.
    """
    return (yield 42)

# asyncio

@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print("T-mins", n , '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1



if __name__ == '__main__':
    re_eager = eager_range(10)
    re_lazy = lazy_range(10)
    re_lazy_new = lazy_range_new(10)
    for item in re_lazy_new:
        print (item)
    print ("now is jump range")
    iteator = jumping_range(5)
    print(next(iteator))              # 0   # first time yield index=0
    print (iteator.send(2))           # 2   # seconde jump=2, yield index=0+2
    print (next(iteator))             # 3   # third jump=None, yield index=2+1
    print (iteator.send(-1))          # 2   # fourth jump=-1, index=3-1
    for item in iteator:              # iteator [0,2,3,2,3,4] remove 0,2,3,2
        print (item)                  # 3,4 #
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(countdown("A", 2)),
        asyncio.ensure_future(countdown("B", 3))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
