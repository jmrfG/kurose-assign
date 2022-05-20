from socket import *
import sys

if len(sys.argv) != 4:
    print("Unable to establish connection. \n")
    print("Use: Client.py <server_host> <server_port> <filename")

serverHost, serverPort, filename = sys.argv[1:]
serverPort = int(serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverHost, serverPort))
except:
    print("Server is offline.")
    clientSocket.close()
    sys.exit()


clientSocket.send(f"GET /{filename} HTTP/1.1\r\n\r\n".encode())
res = ""
while True:
    clientSocket.settimeout(5)
    d = clientSocket.recv(1024).decode()
    res += d
    if len(d) == 0:
        break
print(res)
clientSocket.close()
