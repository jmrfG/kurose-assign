from socket import *
import time
import sys
# This is the UDP Client

if len(sys.argv) < 2:
    print("Use Ping <optional command> <MSG>. \n")

PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)
msg = sys.argv[-1]

if sys.argv[1] != "-m":
    try:
        clientSocket.sendto(msg.encode(), ("localhost", PORT))
        t0 = time.time()
        res, addr = clientSocket.recvfrom(1024)
        t1 = time.time()
        print(f"{res}.\n")
        print(f"{t1-t0} seconds have passed.\n")
    except socket.timeout:
        print("Timeout.\n")
elif sys.argv[1] == "-m":
    t = 0
    RTT = []
    for i in range(10):
        try:
            clientSocket.sendto(msg.encode(), ("localhost", PORT))
            t0 = time.time()
            res, addr = clientSocket.recvfrom(1024)
            t1 = time.time()
            rtt = t1-t0
          #  print(f"#{i} - {res}.\n")
            print(f"#{i} - {rtt} seconds have passed.\n")
            RTT.append(rtt)
        except Exception as e:
            t += 1
            print(f"#{i} time out,\n")
            continue
    s = 0
    l = len(RTT)
    for i in RTT:
        s += i/l
    print(f"Max RTT: {max(RTT)}.\n")
    print(f"Min RTT: {min(RTT)}.\n")
    print(f"Avg RTT: {s}.\n")
    print(f"{t/10}% of packages were lost.\n")
