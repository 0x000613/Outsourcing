# 사용할 모듈 Import
import socket
import os
import argparse
import threading
import time
import sqlite3

# 현재 데이터파일이 위치한 경로를 저장
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
# sqlite3 모듈을 이용해 chat.db라는 데이터베이스 파일을 매핑
conn = sqlite3.connect(os.path.join(BASE_DIR, "chat.db"), check_same_thread=False)
# chat.db 메소드에 연결
cur = conn.cursor()

# 만약
try:
    # 'CREATE TABLE chat(name TEXT, chat TEXT)'라는 쿼리를 데이터베이스에 실행했을때 오류가 안날경우 아래 코드 실행
    conn.execute('CREATE TABLE chat(name TEXT, chat TEXT)')
except:
    # 오류가 날경우 위의 코드를 실행하지 않고 패싱
    pass

# 접속 기본 설정
# 서버 아이피
host = "127.0.0.1"
# 서버 포트
port = 4000
# 유저 객체를 담을 딕셔너리 초기화
user_list = {}
# 공지
notice_flag = 0
# 클라이언트의 접속을 받는 함수
def handle_receive(client_socket, addr, user):
    # 무한루프
    while 1:
        # 데이터는 1024바이트만을 받도록 설정
        data = client_socket.recv(1024)
        # string 변수에 클라이언트로부터 받은 data를 decoding (디코딩 안해주면 이진코드라서 못씀)
        string = data.decode()
        # 받은 데이터를 출력
        print(string)
        # 유저명을 위의 채팅 데이터처럼 decoding후 출력
        print(user.decode())
        # 받은 데이터와 해당 데이터를 보낸 유저명을 모두 디코딩한 후 "INSERT"쿼리를 이용해 디비에 저장
        cur.execute("INSERT INTO chat VALUES('{}', '{}')".format(str(user.decode()), str(string)))
        # db파일의 변경사항을 저장
        conn.commit()
        # 받은 데이터가 /종료 일 경우 접속끊음
        if string == "/종료" : break
        # 다시 string을 변환하여 출력
        string = "%s : %s"%(user, string)
        print(string)
        # 매 반복마다 유저 리스트중에서 연결이 비정상적인 소켓을 체크하는 반복문
        for con in user_list.values():
            try:
                # user list에 있는 유저들에게 메시지를 전송해봄
                con.sendall(string.encode())
            except:
                # 만약 정상적으로 메시지가 전달되지 않을 경우 비정상 소켓으로 인지하고 해당 클라이언트를 출력
                print("연결이 비 정상적으로 종료된 소켓 발견")
    # user list에서 해당 유저 삭제
    del user_list[user]
    # 해당 유저 disconnection
    client_socket.close()

# 공지 함수
def handle_notice(client_socket, addr, user):
    pass

def accept_func():
    #IPv4 체계, TCP 타입 소켓 객체를 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #포트를 사용 중 일때 에러를 해결하기 위한 구문
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #ip주소와 port번호를 함께 socket에 바인드 한다.
    #포트의 범위는 1-65535 사이의 숫자를 사용할 수 있다.
    server_socket.bind((host, port))

    #서버가 최대 5개의 클라이언트의 접속을 허용한다.
    server_socket.listen(5)

    while 1:
        try:
            #클라이언트 함수가 접속하면 새로운 소켓을 반환한다.
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            for user, con in user_list:
                con.close()
            server_socket.close()
            print("Keyboard interrupt")
            break
        user = client_socket.recv(1024)
        user_list[user] = client_socket

        #accept()함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        notice_thread = threading.Thread(target=handle_notice, args=(client_socket, addr, user))
        notice_thread.daemon = True
        notice_thread.start()

        receive_thread = threading.Thread(target=handle_receive, args=(client_socket, addr,user))
        receive_thread.daemon = True
        receive_thread.start()


if __name__ == '__main__':
    #description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
    #help - 인자가 하는 일에 대한 간단한 설명.
    parser = argparse.ArgumentParser(description="\nJoo's server\n-p port\n")
    parser.add_argument('-p', help="port")

    args = parser.parse_args()
    try:
        port = int(args.p)
    except:
        pass
    accept_func()