#coding:utf-8
import socket 
import time
from logging_time import logging_time


def blocking_way():
    sock = socket.socket()
    sock.connect(('www.qq.com', 80))
    request = 'GET /HTTP/1.0\r\nHost: www.qq.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response

@logging_time
def sync_way():
    res = []
    for i in range(100):
        res.append(blocking_way())
    end = time.time()
    return len(res)

if __name__ == '__main__':
    sync_way()
    print("""单线程由于socket.connect(), socket.recv()都是
    阻塞型 ，所以必需同步顺序调用。
    """)