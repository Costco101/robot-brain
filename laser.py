import serial
ser = serial.Serial('/dev/ttyACM0',115200, timeout=1) 
for i in range(10):
	line = ser.readline() # open serial port
	print(line)         # check which port was really use    
ser.close()             # close port
