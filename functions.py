import serial
import serial.tools.list_ports
import time
"""
Function that find the correct COM port for each computer
it asserts that 'USB Serial Device' is included in the description
since this what my computer is showing as the serial port description
"""
def findCorrectPort():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if 'USB Serial Device' in desc:
            return port

"""
Function that add the correct baud rate
for the serial communication connection
"""
def initializeSerialPort():
    targetPort = findCorrectPort()

    print('Connecting to ' + targetPort)
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.timeout = 10
    ser.port = targetPort
    ser.open()
    return ser

"""
Function that read one line from serial port
and adds to to queue in order for external
threads to access it.
"""
def readData(ser, stack):
    line = ser.readline().decode('utf8')
    stripedData = line.strip()
    stack.append(stripedData)