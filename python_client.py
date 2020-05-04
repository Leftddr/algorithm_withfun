import socket
import argparse

port = 4000

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Client\n-p port\n-i host\n-s string')
    parser.add_argument('-p', help = 'port', required = True)
    parser.add_argument('-i', help = 'host', required = True)
    parser.add_argument('-u', help = 'user', required = True)

    args = parser.parse_args()
    host = args.i
    user = str(args.u)
    try:
        port = int(args.p)
    except:
        pass
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(user.encode())
    receive_data = client_socket.recv(1024)

    print(receive_data.decode('utf-8'))
    client_socket.close()
    
    
