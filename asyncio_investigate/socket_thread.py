import socket 
import time
from concurrent import futures
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
def thread_way():
    workers = 16
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(100)}
    return len([fut.result() for fut in futs])

if __name__ == '__main__':
    thread_way()