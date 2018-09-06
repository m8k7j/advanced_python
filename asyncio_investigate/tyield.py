import time

def consumer():
    r = ''
    while True:
        n = yield r                                       #  接受send传进来的参数
        if not n:
            return 
        print ('[CONSUMER] Consuming %s.. ' %n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    next(c)                                                      # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print ('[Product] producing %s..' % n)
        r = c.send(n)
        print('[Product] consumer return %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)