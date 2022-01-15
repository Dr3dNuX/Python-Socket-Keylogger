import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)

serversocket.bind(('127.0.0.1', 2020))
serversocket.listen()

cli_sock, addr = serversocket.accept()


while True:
    data = bytes.decode(cli_sock.recv(1024))
    if data:
    	print(data)
    else:
    	cli_sock.close()
