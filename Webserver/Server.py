from socket import *
import sys
import constants as c

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", c.PORT))
server_socket.listen(1)
print("Server is on, baby!")
RUN = True
while RUN:
    connectionSocket, address = server_socket.accept()
    # Get the IP
    print(f"{address}")
    try:
        request = connectionSocket.recv(1024).decode()
        filename = request.split()[1]
        f = open(filename[1:], "r")
        output = f.read()
        # print(f"{output}")
        print("I thing i'm onto something")
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("\r\n".encode())
        for i in range(0, len(output)):
            connectionSocket.send(output[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()
server_socket.close()
sys.exit()
