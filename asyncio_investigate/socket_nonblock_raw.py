import socket
from logging_time import logging_time

def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.qq.com', 80))
    except BlockingIOError:
        pass
    request = 'GET / HTTP1.0\r\nHost: www.qq.com\r\n\r\n'
    data = request.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass
    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response

@logging_time
def sync_way():
    res = []
    for i in range(100):
        res.append(nonblocking_way())
    return len(res)


if __name__ == '__main__':
    sync_way()