# 통신을 위한 socket 모듈 import
import socket
# udp 소켓을 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# host의 prot번으로 서버 실행
sock.bind(("127.0.0.1", 4000))
while True:
    # data를 data변수에, 클라이언트의 정보를 addr 변수에 저장
    data, addr = sock.recvfrom(1024)
    # data변수에 저장된 값을 디코딩하여 계산한 뒤 str로 형변환하여 data에 재저장
    data = str(eval(data.decode()))
    # data변수에 저장된 값을 클라이언트로 전송
    sock.sendto(data.encode(), addr)
# 소켓 종료
sock.close()