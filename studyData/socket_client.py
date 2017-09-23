import socket


host = 'localhost'
port = 12345
bufsiz = 4096
addr = (host, port)

# 사용자에게 input을 줘서 사용자가 서버 넘버를 받을수 있게 해줌 
if __name__ == '__main__':
     client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

     host = input() or host # 사용자가 그냥 엔터를 쓰면, 위의 host 를 그냥 사용하게 하는거고, 엔터를 치지않고 사용자가 값을 입력하면 입력한 값을 사용할수 있게 만듬
     port = input("port number[12345] > ") or host


     sock_addr = (host, int(port)) # 주소 지정을 해준것, 주소 지정이 끝나면
     client_sock.connect(sock_addr)
     
     # 패킷 안에 들어 있는 실제 데이터를 payload 라고 통상 부름. 
     payload = 'GET TIME' 

     try:
          while True:
               client_sock.send(payload.encode("utf-8")) # 리눅스 는 utf-8임 맥을 사용할때 전자 홈페이지 들어가서 글씨가 걔지는 이유는 전자정부는 유니코드 이기때문이다.. 아아..
               data = client_sock.recv(bufsiz)
               print(repr(data))
               # repr 을 사용할때는 매소드를 주고 받을때 사용가능. 음.. 원래는 그냥 찍어보면 값이 안나와서 오류가나옴.

               #다른것들도 넣을수 있게 만들어 놓은것임..!  
               more = input("Want more?[y/n]")
               if more.lower() =='y':
                    payload = input("Enter your payload")

               else:
                    break

               
     except KeyboardInterrupt:
          print("Exited")

     # 서버만들떄 리시브와 샌드를 받는과정은 무한루트로 한다..? why? 이거 한번 찾아보자 
     client_sock.close()
