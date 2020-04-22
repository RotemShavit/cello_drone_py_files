import socket
import time

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('147.234.54.189', 1234))
print("connected")

counter = 0
msg = ""
fin_msg = bytes("finished", "utf-8")
while msg != fin_msg:
    msg = s.recv(1024)
    s.sendall(bytes(str(counter), "utf-8"))
    print(msg)
    time.sleep(1)
    counter += 1

# s.sendall(bytes("Client is sending\n:", "utf-8"))
# counter = 0
# while counter < 5:
#     s.sendall(bytes(str(counter), "utf-8"))
#     time.sleep(1)
#     counter += 1
#s.sendall(bytes("finished", "utf-8"))
time.sleep(2)

s.shutdown(socket.SHUT_RDWR)
time.sleep(3)
s.close()
