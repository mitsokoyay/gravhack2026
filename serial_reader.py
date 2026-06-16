import serial

# Open the serial port
ser = serial.Serial("/dev/ttyUSB0", 9600)

try:
    while True:
        if ser.in_waiting:
            data = ser.readline()
            print(data.decode("utf - 8").strip())
except KeyboardInterrupt:
    ser.close()
