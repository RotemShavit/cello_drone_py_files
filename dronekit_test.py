from dronekit import *
#from dronekit import mavlink
from line_changer import *
from lcd_script import *
import time

time.sleep(5)
line_change("Mvlink", "False")
test_lcd()

time.sleep(10)


try:
	cello_drone = connect("/dev/ttyS0", wait_ready=True, baud=57600)
### A try to fix connection between QGC and dronekit
	udp_conn = MAVConnection('udpin:0.0.0.0:15667', source_system=1)
#    	cello_drone._handler.pipe(udp_conn)
#   	udp_conn.master.mav.srcComponent = 1
#    	udp_conn.start()
###
	print("Battery: " ,cello_drone.battery)
	print("Status: " ,cello_drone.system_status.state)
	print("Mode: " ,cello_drone.mode.name)
	print("Armed: " ,cello_drone.armed)
	line_change("Mavlink", "True")
	test_lcd()

except Exception as e:
	print("Can not connect: ", e)
	line_change("Mavlink", "False")
	test_lcd()
