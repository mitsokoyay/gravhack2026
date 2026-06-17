import sys
import serial
import pyscsi

printSettings=True
myDevice=serial.Serial(port='COM3')
#myDevice=SCSIDevice.init(self,"COM3")   ,9600,8,1,None,False,False,False,None,False,None,None
#myDevice.perform_inquiry('COM3')
if myDevice.is_open:
    print("device open\n")
else:
    print("device not open\n")
mySettings=myDevice.get_settings
if printSettings:
        # Display the parsed standard inquiry data
        print("Standard INQUIRY Results:")
        print("========================")
        print(mySettings)
"""        print(f"Peripheral Qualifier: {mySettings['peripheral_qualifier']}")
        print(f"Device Type: {mySettings['peripheral_device_type']}")
        print(f"RMB (Removable): {mySettings['rmb']}")
        print(f"Version: {mySettings['version']}")
        print(f"NormACA: {mySettings['normaca']}, HiSUP: {mySettings['hisup']}")
        print(f"Data Format: {mySettings['response_data_format']}")
"""
while True:
    myByte=myDevice.read(1)
    myLine=myDevice.readline(8)
    print(myByte)
    print(myLine)
print("inquiry complete\n")
# Open the serial port
"""
ser = serial.Serial('COM3')
pyscsi.scsi_device
pyscsi.init_device(Any)
try:
    data = ser.read(1)
    print('data4u')
    print(data.decode("utf - 8").strip())

"""
"""
    while True:
        if ser.in_waiting:
            data = ser.readline()
        else:
            print(data.decode("utf - 8").strip())
            break;
        
except KeyboardInterrupt:
    ser.close()
    print('connection closed')
"""