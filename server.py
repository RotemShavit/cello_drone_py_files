import socket
import time

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(5)

client_socket, address = s.accept()
# accept only our ip
print("Connection from rpi (addr = ", address, ") has been established!")
client_socket.sendall("Server is sending:")
time.sleep(1)
counter = 0

while counter < 11:
    client_socket.sendall(str(counter))
    msg=client_socket.recv(1024)
    print(msg)
    time.sleep(1)
    counter = counter + 1
client_socket.sendall("finished")
time.sleep(2)

#fin_msg = bytes("finished")
#msg =""
#while msg != fin_msg:
#    msg=client_socket.recv(1024)
#    print(msg)
#    counter += 1
#    time.sleep(1)

s.shutdown(socket.SHUT_RDWR)
time.sleep(3)
s.close()
