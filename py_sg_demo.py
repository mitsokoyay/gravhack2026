import os
import struct
from py_sg import py_sg

# 1. Open the SCSI Generic device
device_path = "/dev/sg0" 
sg_fd = os.open(device_path, os.O_RDWR)

# 2. Define the Command Descriptor Block (CDB) for a SCSI INQUIRY (Opcode 0x12)
# Standard INQUIRY requests 36 bytes of peripheral/vendor data
cdb = b'\x12\x00\x00\x00\x24\x00'

# 3. Handshake Execution: Send the command to the target
print(f"Sending SCSI Inquiry to {device_path}...")
try:
    # py_sg handles the IOCTL, passing CDB and allocating buffer for the reply
    reply_data = py_sg.send_scsi(sg_fd, cdb, read_len=36)

    # 4. Parse the Status and Data returned by the target
    if len(reply_data) >= 36:
        # Byte 0 defines the peripheral device type
        periph_type = reply_data[0] & 0x1F
        
        # Extract vendor and product identification (Bytes 8-35)
        vendor_id = reply_data[8:16].decode('utf-8', errors='ignore').strip()
        product_id = reply_data[16:32].decode('utf-8', errors='ignore').strip()
        
        print(f"Device Type: {periph_type}")
        print(f"Vendor: {vendor_id}")
        print(f"Product: {product_id}")
    else:
        print("SCSI handshake completed but data is incomplete.")

except py_sg.SCSIError as e:
    # Captures CHECK CONDITION status
    print(f"SCSI Target returned an error: {e}")

finally:
    os.close(sg_fd)
