# 통신을 위한 socket 모듈 import
import socket
# 사용할 udp 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# HOST의 PORT로 소켓 접속 시도
sock.connect(('127.0.0.1', 4000))
while True:
    # 계산식을 입력받고 msg 변수에 저장
    msg = input("->")
    # 연결된 소켓으로 msg를 인코딩하여 서버로 전송
    sock.sendto(msg.encode(), ("127.0.0.1", 4000))
    # 서버로부터 받은 데이터를 data 변수에 저장
    recvMsg, addr = sock.recvfrom(2048)
    # data 변수의 값을 디코딩하여 출력
    print(recvMsg.decode())
# 소켓 접속 할당 해제
sock.close()