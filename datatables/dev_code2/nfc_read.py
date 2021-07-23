
import digitalio
from board import *
import board
import busio
import time
# Additional import needed for I2C/SPI
from digitalio import DigitalInOut
#
# NOTE: pick the import that matches the interface being used
#
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from adafruit_pn532.i2c import PN532_I2C


power = DigitalInOut(board.D21)
power.direction = digitalio.Direction.OUTPUT
power.value = True

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)

reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)
try:
    pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
except Exception as err:
    # print(err)
    time.sleep(1)
    pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

ic, ver, rev, support = pn532.firmware_version

pn532.SAM_configuration()


key = b"\xFF\xFF\xFF\xFF\xFF\xFF"


current_time = time.time() * 1000
while (int(time.time() * 1000) - current_time) < 5000:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is not None:
        break

try:
    print("Found card with UID:", [hex(i) for i in uid])
    print("Authenticating block 4 ...")
    authenticated = pn532.mifare_classic_authenticate_block(uid, 4, MIFARE_CMD_AUTH_B, key)
    if not authenticated:
        print("Authentication failed!")
    print("data", [chr(x) for x in pn532.mifare_classic_read_block(4)])
    pn532.power_down()
except Exception as err:
    print("no tags")
    pn532.power_down()
