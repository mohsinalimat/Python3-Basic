## 20_Python3

---

## socket io 활용한 네트워크 통신 

---

 - python 의 내장모듈인 socket을 이용해서, 간이 server, client 를 만들어서 서로 통신을 해보자!

 - 준비물

	1. 서버
	2. 클라이언트
	3. 구현시키고 난후 눈으로 확인할 터미널!
	

 
```python

*** server ***

# Echo server program
import socket

HOST = ''                   # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()

-> terminal 에다 server를 먼저 키고, 난이후에 client에 내 ip 를 설정해주고 실행을 시키면, 서로 통신하는 모습을 볼수 있다.


*** client ***


# Echo client program
import socket

# 아래의 호스트에 내 아이피를 넣자
HOST = '127.0.0.1'                # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)



```

 - socket_server 작동 모습

![screen](/image/socket_server.jpg)

 - socket_client 작동 모습

![screen](/image/socket_client.jpg)


> 작동 순서는 socket_server 작동 -> socket_client 작동 -> 서로 통신하는것 확인할수 있음