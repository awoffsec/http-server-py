import socket
import threading

def HandleClient(conn: socket.socket, addr: tuple) -> None:
    print('handling connection')
    

def StartServer(args) -> int:
    HOST = '127.0.0.1'
    PORT = int(args.port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Listening on port {}...'.format(str(PORT)))

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=HandleClient, args=(conn, addr))
            thread.start()
        return -1
