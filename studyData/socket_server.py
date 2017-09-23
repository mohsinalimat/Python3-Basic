import socket
from time import ctime

# 호스트와 포트를 이용해서 vufsiz 를 만듬 
host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port) # addr 주소를 사용하기 위해서는 튜플로 선언해야함 


if __name__ == '__main__':
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_socket.bind(addr) # host 와 port 로 뭘 할지 정해놓음
     server_socket.listen(5) # 5개의 conection 까지 가능하게 만듬. 한포트에 5개 까지
     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)

     while True:
          print("Server is listening...")
          client_sock, addr = server_socket.accept() # client 가 들어왔다.
          print("client connected from: ", addr)

          while True: # 여기의 절차가 끝날때까지 돌림.
               data = client_sock.recv(bufsiz) # 내가 정의해놓은 bufsiz 만큼 데이터를 주고 받음..
               # 데이터를 받았는데, 데이터가 없으면 끝내야함.

               if not data or data.decode("utf-8") == 'END':
                    break


               print("received data from client: %s" % data.decode("utf-8"))

               print("Sending Server time: %s" %ctime())


               try:
                    client_sock.send(bytes(ctime(), 'utf-8'))

               except KeyboardInterrupt:
                    pritn("Exited by user")

          client_sock.close() # 위의 무한반복이 깨지면 서버 client 를 닫고 
     server_socket.close() # 데이터를 받는 과정까지 끝나면 서버 소켓을 닫음.
     
