import argparse
import socket
import threading
import time

host = '127.0.0.1'
port = 4000

def handle_client(client_socket, addr):
    print('Connecting Client addr : ', addr)
    user = client_socket.recv(1024)
    string = 'hello %s' % user.decode('utf-8')
    client_socket.sendall(string.encode())
    time.sleep(1)
    client_socket.close()

def accept_func():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    while 1:
        try:
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            server_socket.close()
            print('Keyboard interrupt')
    
        t = threading.Thread(target = handle_client, args = (client_socket, addr))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Server -p port')
    parser.add_argument('-p', required = True, help = 'port')

    args = parser.parse_args()
    try:
        port = int(args.p)
    except:
        pass
    accept_func()
