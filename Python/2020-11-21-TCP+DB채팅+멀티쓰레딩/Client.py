# 사용할 모듈 Import
import socket
import argparse
import threading

# 접속할 서버의 포트
port = 4000

# 서버로 데이터를 보내는 함수
def handle_receive(num, lient_socket, user):
    # 무한 루프
    while 1:
        try:
            # 서버로부터 데이터를 1024 바이트까지 전송받음
            data = client_socket.recv(1024)
        except:
            # 위 구문이 에러가 날 경우 연결을 종료
            print("연결 끊김")
            break
        # 받은 데이터를 decode
        data = data.decode()
        # 유저가 data에 없을 경우
        if not user in data:
            # 데이터 출력
            print(data)

# 서버로 데이터를 전송하는 함수
def handle_send(num, client_socket):
    while 1:
        # 사용자에게 데이터를 input받음
        data = input()
        # 데이터를 encoding하고 서버로 전송
        client_socket.sendall(data.encode())
        # 내가 보낸 데이터가 "/종료"일 경우 데이터를 전송하고 프로그램 종료
        if data == "/종료":
            break
    # 소켓 close
    client_socket.close()


if __name__ == '__main__':
    #parser와 관련된 메서드 정리된 블로그 : https://docs.python.org/ko/3/library/argparse.html
    #description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
    #help - 인자가 하는 일에 대한 간단한 설명.
    #nargs - 소비되어야 하는 명령행 인자의 수. -> '+'로 설정 시 모든 명령행 인자를 리스트로 모음 + 없으면 경고
    #required - 명령행 옵션을 생략 할 수 있는지 아닌지 (선택적일 때만).
    parser = argparse.ArgumentParser(description="\nJoo's client\n-p port\n-i host\n-s string")
    parser.add_argument('-p', help="port")
    parser.add_argument('-i', help="host", required=True)
    parser.add_argument('-u', help="user", required=True)

    args = parser.parse_args()
    host = args.i
    user = str(args.u)
    try:
        port = int(args.p)
    except:
        pass
    #IPv4 체계, TCP 타입 소켓 객체를 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 지정한 host와 prot를 통해 서버에 접속합니다.
    client_socket.connect((host, port))

    # 모든 유저에게 메시지를 보낸 유저로부터 받은 데이터를 전송
    client_socket.sendall(user.encode())

    # 컴퓨터는 일을 처리할 때 직렬처리, 즉 한 번에 하나의 일밖에 하지 못하기때문에
    # 스레드를 사용해서 병렬처리를 할 수 있게끔 함

    # 데이터를 전송받는 스레드 객체를 생성하고 실행
    receive_thread = threading.Thread(target=handle_receive, args=(1, client_socket, user))
    receive_thread.daemon = True
    receive_thread.start()

    # 데이터를 전송하는 스레드 객체를 생성하고 실행
    send_thread = threading.Thread(target=handle_send, args=(2, client_socket))
    send_thread.daemon = True
    send_thread.start()

    # 두 스레드 객체를 Join
    send_thread.join()
    receive_thread.join()