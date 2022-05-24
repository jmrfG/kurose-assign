from socket import *
from config import *
import sys

if len(sys.argv) < 3:
    print("Use MAILCLient.py <from> <to> <message>.\n")

FROM, TO, MESSAGE = sys.argv[1], sys.argv[2], sys.argv[3]
print(F"{FROM}/{TO}")
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))

clientSocket.settimeout(5)

recv = clientSocket.recv(1024).decode()
print(recv)

if recv != "220":
    print("220 reply not received from server(1).\n")

clientSocket.send(HELO.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server(2).\n")

print("Aqui")
clientSocket.send((MAIL_FROM.format(FROM)).encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server(3).\n")

clientSocket.send((RCPT_TO.format(TO)).encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server(4).\n")

clientSocket.send(DATA.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server(5).\n")

clientSocket.send("\r\n".encode())
clientSocket.send((MESSAGE + "\r\n").encode())
clientSocket.send(".\r\n".encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print("250 reply not received from server(6).\n")

clientSocket.send(QUIT.encode())
clientSocket.close()
