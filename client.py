import socket
import time

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('147.234.54.189', 12341))
s.connect((socket.gethostname(), 12341))

print("connected\n")
s.sendall(bytes("connected", "utf-8"))

while True:
    to_send = "CD;"
    # req_data = [0, 0, 0]
    # req_data_str = ["Battery", "Armed", "Status"]
    # i = 0
    # for d in req_data:
    #     if d == 1:
    #         to_send = to_send + req_data_str[i] + ";"
    #     i += 1
    # to_send_lst = to_send.split(";")
    # print(to_send)
    s.sendall(bytes(to_send, "utf-8"))
    # s_msg = str(s.recv(1024))
    # s_msg = s_msg[2:-2]
    # data = str(s_msg).split(";")
    # i = 1
    # for d in data:
    #     if "Battery" in d:
    #         temp_d = d[8:21]
    #         vol = float(temp_d[8:13])
    #         print(vol)
    #         print(to_send_lst[i] + ": " + temp_d)
    #     else:
    #         print(to_send_lst[i] + ": " + d)
    #     i += 1
    time.sleep(1)

time.sleep(2)
s.shutdown(socket.SHUT_RDWR)
time.sleep(3)
s.close()
