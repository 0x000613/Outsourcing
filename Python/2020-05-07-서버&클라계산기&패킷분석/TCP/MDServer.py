# 통신을 위한 socket 모듈 import
import socket
# 사용할 tcp 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓에 Host의 포트를 바인딩하고 TCP 연결 요청 기다림
sock.bind(('127.0.0.1', 4000))
# 클라이언트 접속 대기
sock.listen()
# 클라이언트 접속시 con, addr에 클라이언트의 접속 정보를 저장
con, addr = sock.accept()
while True:
    # data 변수에 클라이언트로부터 전송받은 데이터를 디코딩하여 저장
    data = con.recv(1024).decode()
    # 전달받은 데이터가 존재하지않으면
    if not data:
        # 루프를 종료하고 23번째 라인으로 이동 (sock.close()) << 맨 마지막줄
        break
    # data 변수에 이전의 data값을 eval 함수로 계산하여 data 변수에 저장
    data = eval(data)
    # data 변수에 저장된 값을 str(문자형 데이터)로 형변환하고 인코딩하여 전송
    con.send(str(data).encode())
# 소켓 서버 할당 종료
sock.close()