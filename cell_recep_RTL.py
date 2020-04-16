from line_changer import *
from lcd_script import *
from dronekit import *
import time

def is_conn_func ():
	with open("indication.txt", "r") as fd:
		inet_line = fd.readlines()[0]
		fd.close()

	if ("True" in inet_line):
		yes_working = 1
	else:
		yes_working = 0

	return yes_working


cello_drone = connect("/dev/ttyS0", wait_ready=True, baud=57600)

check = True

while(check):
	is_conn = is_conn_func()
	if(not is_conn):
		# RTL
		check = False


