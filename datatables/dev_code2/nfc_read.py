# SPDX-FileCopyrightText: <text> 2015 Tony DiCola, Roberto Laricchia,
# and Francesco Crisafulli, for Adafruit Industries </text>

# SPDX-License-Identifier: MIT

# Example of detecting and reading a block from a MiFare classic NFC card.

"""
This example shows connecting to the PN532 and writing & reading a mifare classic
type RFID tag
"""
import digitalio
from board import *
import board
import busio
import time
from digitalio import DigitalInOut
#
# NOTE: pick the import that matches the interface being used
#
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from adafruit_pn532.i2c import PN532_I2C

# from adafruit_pn532.spi import PN532_SPI
# from adafruit_pn532.uart import PN532_UART
power = DigitalInOut(board.D21)
power.direction = digitalio.Direction.OUTPUT
power.value = True

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)

# Non-hardware reset/request with I2C
# pn532 = PN532_I2C(i2c, debug=False)

# With I2C, we recommend connecting RSTPD_N (reset) to a digital pin for manual
# harware reset
reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
req_pin = DigitalInOut(board.D12)
try:
    pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
except Exception as err:
    # print(err)
    time.sleep(1)
    pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

# SPI connection:
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# cs_pin = DigitalInOut(board.D5)
# pn532 = PN532_SPI(spi, cs_pin, debug=False)

# UART connection
# uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=100)
# pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.firmware_version
# print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
# pn532.SAM_configuration()
pn532.SAM_configuration()
# print("Waiting for RFID/NFC card to write to!")

key = b"\xFF\xFF\xFF\xFF\xFF\xFF"


def current_milli_time():
    return round(time.time() * 1000)


current_time = current_milli_time()
while ((int(time.time() * 1000) - current_time) < 5000):
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    #    print(".", end="")
    # Try again if no card is available.
    if uid is not None:
        break

# print("")
# print("failed")
try:
    # print("Found card with UID:", [hex(i) for i in uid])
    # print(len(uid))
    if len(uid) == 4:
        uid_id = "{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(uid[0], uid[1], uid[2], uid[3])
        print(uid_id)
    elif len(uid) > 4:
        uid_id = "{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}:{5:02x}:{6:02x}".format(uid[0], uid[1], uid[2], uid[3],
                                                                                  uid[4], uid[5], uid[6])
        print(uid_id)
    elif len(uid) > 7:
        uid_id = "{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}:{5:02x}:{6:02x}:{7:02x}:{8:02x}:{9:02x}".format(uid[0],
                                                                                                          uid[1],
                                                                                                          uid[2],
                                                                                                          uid[3],
                                                                                                          uid[4],
                                                                                                          uid[5],
                                                                                                          uid[6],
                                                                                                          uid[7],
                                                                                                          uid[8],
                                                                                                          uid[9])
        print(uid_id)


    pn532.power_down()
except Exception as err:
    print("no tags")
    pn532.power_down()