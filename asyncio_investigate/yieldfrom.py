#coding:utf-8

"""
different from yield and yield from
"""

def iterator(n):
    item = 0
    while item < n:
        r = yield item
        if r is None:
            item += 1
        else:
            item += r

def generator(n):
    yield from iterator(n)
        

def accmulate():
    tally = 0
    while True:
        next = yield 
        if next is None:
            return tally
        tally += next

def gather_tallies(tallies):
    while True:
        tally = yield from accmulate()
        tallies.append(tally)

if __name__ == '__main__':
    re = iterator(10)
    print(re)
    for item in re:
        print(item)
    
    print("now is send a singal 5 to the iterator")
    re = iterator(10)
    next(re)
    re.send(5)
    for item in re:
        print(item)

    re = generator(10)
    print(re)
    for item in re:
        print(item)

    print("accumulate and gather tallies")
    tallies = []
    acc = gather_tallies(tallies)
    next(acc)
    for i in range(4):
        acc.send(i)
    acc.send(None)
    for i in range(5):
        acc.send(i)
    acc.send(None)
    print(tallies)
    print(""" yield form iterable 
          for item in iterable:
              yield item 的缩写
        但是yield from 允许子生成器直接从调用者接收其发送的信息
        或者抛出的异常，并且返回给委派生成器一个值如：
        子生成器 accumulate()返回一个总值，接收委派生成器gather_tallies() send
        过来的值， gather_tallies()的作用是给tallies列表加值。
    
    """)
    
    