import machine
import utime

# ///////////////////////
# // General Constants //
# ///////////////////////
BQ72441_I2C_ADDRESS = 0x55
BQ27441_UNSEAL_KEY = 0x8000  # Secret code to unseal the BQ27441-G1A
BQ27441_DEVICE_ID = 0x0421  # Default device ID
BQ72441_I2C_TIMEOUT = 2000  # in ms

# ///////////////////////
# // Standard Commands //
# ///////////////////////
# // The fuel gauge uses a series of 2-byte standard commands to enable system
# // reading and writing of battery information. Each command has an associated
# // sequential command-code pair.
BQ27441_COMMAND_CONTROL = 0x00  # Control()
BQ27441_COMMAND_TEMP = 0x02  # Temperature()
BQ27441_COMMAND_VOLTAGE = 0x04  # Voltage()
BQ27441_COMMAND_FLAGS = 0x06  # Flags()
BQ27441_COMMAND_NOM_CAPACITY = 0x08  # NominalAvailableCapacity()
BQ27441_COMMAND_AVAIL_CAPACITY = 0x0A  # FullAvailableCapacity()
BQ27441_COMMAND_REM_CAPACITY = 0x0C  # RemainingCapacity()
BQ27441_COMMAND_FULL_CAPACITY = 0x0E  # FullChargeCapacity()
BQ27441_COMMAND_AVG_CURRENT = 0x10  # AverageCurrent()
BQ27441_COMMAND_STDBY_CURRENT = 0x12  # StandbyCurrent()
BQ27441_COMMAND_MAX_CURRENT = 0x14  # MaxLoadCurrent()
BQ27441_COMMAND_AVG_POWER = 0x18  # AveragePower()
BQ27441_COMMAND_SOC = 0x1C  # StateOfCharge()
BQ27441_COMMAND_INT_TEMP = 0x1E  # InternalTemperature()
BQ27441_COMMAND_SOH = 0x20  # StateOfHealth()
BQ27441_COMMAND_REM_CAP_UNFL = 0x28  # RemainingCapacityUnfiltered()
BQ27441_COMMAND_REM_CAP_FIL = 0x2A  # RemainingCapacityFiltered()
BQ27441_COMMAND_FULL_CAP_UNFL = 0x2C  # FullChargeCapacityUnfiltered()
BQ27441_COMMAND_FULL_CAP_FIL = 0x2E  # FullChargeCapacityFiltered()
BQ27441_COMMAND_SOC_UNFL = 0x30  # StateOfChargeUnfiltered()

# //////////////////////////
# // Control Sub-commands //
# //////////////////////////
# // Issuing a Control() command requires a subsequent 2-byte subcommand. These
# // additional bytes specify the particular control function desired. The
# // Control() command allows the system to control specific features of the fuel
# // gauge during normal operation and additional features when the device is in
# // different access modes.
BQ27441_CONTROL_STATUS = 0x00
BQ27441_CONTROL_DEVICE_TYPE = 0x01
BQ27441_CONTROL_FW_VERSION = 0x02
BQ27441_CONTROL_DM_CODE = 0x04
BQ27441_CONTROL_PREV_MACWRITE = 0x07
BQ27441_CONTROL_CHEM_ID = 0x08
BQ27441_CONTROL_BAT_INSERT = 0x0C
BQ27441_CONTROL_BAT_REMOVE = 0x0D
BQ27441_CONTROL_SET_HIBERNATE = 0x11
BQ27441_CONTROL_CLEAR_HIBERNATE = 0x12
BQ27441_CONTROL_SET_CFGUPDATE = 0x13
BQ27441_CONTROL_SHUTDOWN_ENABLE = 0x1B
BQ27441_CONTROL_SHUTDOWN = 0x1C
BQ27441_CONTROL_SEALED = 0x20
BQ27441_CONTROL_PULSE_SOC_INT = 0x23
BQ27441_CONTROL_RESET = 0x41
BQ27441_CONTROL_SOFT_RESET = 0x42
BQ27441_CONTROL_EXIT_CFGUPDATE = 0x43
BQ27441_CONTROL_EXIT_RESIM = 0x44

# ///////////////////////////////////////////
# // Control Status Word - Bit Definitions //
# ///////////////////////////////////////////
# // Bit positions for the 16-bit data of CONTROL_STATUS.
# // CONTROL_STATUS instructs the fuel gauge to return status information to
# // Control() addresses 0x00 and 0x01. The read-only status word contains status
# // bits that are set or cleared either automatically as conditions warrant or
# // through using specified subcommands.
BQ27441_STATUS_SHUTDOWNEN = (1 << 15)
BQ27441_STATUS_WDRESET = (1 << 14)
BQ27441_STATUS_SS = (1 << 13)
BQ27441_STATUS_CALMODE = (1 << 12)
BQ27441_STATUS_CCA = (1 << 11)
BQ27441_STATUS_BCA = (1 << 10)
BQ27441_STATUS_QMAX_UP = (1 << 9)
BQ27441_STATUS_RES_UP = (1 << 8)
BQ27441_STATUS_INITCOMP = (1 << 7)
BQ27441_STATUS_HIBERNATE = (1 << 6)
BQ27441_STATUS_SLEEP = (1 << 4)
BQ27441_STATUS_LDMD = (1 << 3)
BQ27441_STATUS_RUP_DIS = (1 << 2)
BQ27441_STATUS_VOK = (1 << 1)

# ////////////////////////////////////
# // Flag Command - Bit Definitions //
# ////////////////////////////////////
# // Bit positions for the 16-bit data of Flags()
# // This read-word function returns the contents of the fuel gauging status
# // register, depicting the current operating status.
BQ27441_FLAG_OT = (1 << 15)
BQ27441_FLAG_UT = (1 << 14)
BQ27441_FLAG_FC = (1 << 9)
BQ27441_FLAG_CHG = (1 << 8)
BQ27441_FLAG_OCVTAKEN = (1 << 7)
BQ27441_FLAG_ITPOR = (1 << 5)
BQ27441_FLAG_CFGUPMODE = (1 << 4)
BQ27441_FLAG_BAT_DET = (1 << 3)
BQ27441_FLAG_SOC1 = (1 << 2)
BQ27441_FLAG_SOCF = (1 << 1)
BQ27441_FLAG_DSG = (1 << 0)

# ////////////////////////////
# // Extended Data Commands //
# ////////////////////////////
# // Extended data commands offer additional functionality beyond the standard
# // set of commands. They are used in the same manner; however, unlike standard
# // commands, extended commands are not limited to 2-byte words.
BQ27441_EXTENDED_OPCONFIG = 0x3A  # OpConfig()
BQ27441_EXTENDED_CAPACITY = 0x3C  # DesignCapacity()
BQ27441_EXTENDED_DATACLASS = 0x3E  # DataClass()
BQ27441_EXTENDED_DATABLOCK = 0x3F  # DataBlock()
BQ27441_EXTENDED_BLOCKDATA = 0x40  # BlockData()
BQ27441_EXTENDED_CHECKSUM = 0x60  # BlockDataCheckSum()
BQ27441_EXTENDED_CONTROL = 0x61  # BlockDataControl()

# ////////////////////////////////////////
# // Configuration Class, Subclass ID's //
# ////////////////////////////////////////
# // To access a subclass of the extended data, set the DataClass() function
# // with one of these values.
# // Configuration Classes
BQ27441_ID_SAFETY = 2  # // Safety
BQ27441_ID_CHG_TERMINATION = 36  # // Charge Termination
BQ27441_ID_CONFIG_DATA = 48  # // Data
BQ27441_ID_DISCHARGE = 49  # // Discharge
BQ27441_ID_REGISTERS = 64  # // Registers
BQ27441_ID_POWER = 68  # // Power
# // Gas Gauging Classes
BQ27441_ID_IT_CFG = 80  # // IT Cfg
BQ27441_ID_CURRENT_THRESH = 81  # // Current Thresholds
BQ27441_ID_STATE = 82  # // State
# // Ra Tables Classes
BQ27441_ID_R_A_RAM = 89  # // R_a RAM
# // Calibration Classes
BQ27441_ID_CALIB_DATA = 104  # // Data
BQ27441_ID_CC_CAL = 105  # // CC Cal
BQ27441_ID_CURRENT = 107  # // Current
# // Security Classes
BQ27441_ID_CODES = 112  # // Codes

# /////////////////////////////////////////
# // OpConfig Register - Bit Definitions //
# /////////////////////////////////////////
# // Bit positions of the OpConfig Register
BQ27441_OPCONFIG_BIE = (1 << 13)
BQ27441_OPCONFIG_BI_PU_EN = (1 << 12)
BQ27441_OPCONFIG_GPIOPOL = (1 << 11)
BQ27441_OPCONFIG_SLEEP = (1 << 5)
BQ27441_OPCONFIG_RMFCC = (1 << 4)
BQ27441_OPCONFIG_BATLOWEN = (1 << 2)
BQ27441_OPCONFIG_TEMPS = (1 << 0)

#####  Variables

m = machine.I2C(0, sda=19, scl=18, speed=20000)


#####  User interface functions here

def deviceType():
    return readControlWord(BQ27441_CONTROL_DEVICE_TYPE)


def firmwareVersion():
    return readControlWord(BQ27441_CONTROL_FW_VERSION)


def percentageHealth():
    sohRaw = readWord(BQ27441_COMMAND_SOH)
    percent = sohRaw & 0x00ff
    return percent


def status():
    return readControlWord(BQ27441_CONTROL_STATUS)


def voltage():
    return readWord(BQ27441_COMMAND_VOLTAGE)


def avgCurrent():
    return twos_comp(readWord(BQ27441_COMMAND_AVG_CURRENT), 16)


def socFiltered():
    return readWord(BQ27441_COMMAND_SOC)


def capacityRemain():
    return readWord(BQ27441_COMMAND_REM_CAPACITY)


def capacityFull():
    return readWord(BQ27441_COMMAND_FULL_CAPACITY)


def flags():
    return readWord(BQ27441_COMMAND_FLAGS)


def getDesignCapacity():
    msb = readExtendedData(BQ27441_ID_STATE, 10)
    lsb = readExtendedData(BQ27441_ID_STATE, 11)
    return (msb << 8) + lsb


def setDesignCapacity(cap):
    msb = (cap >> 8) & 0xff
    lsb = cap & 0xff
    buf = bytearray([msb, lsb])
    return writeExtendedData(BQ27441_ID_STATE, 10, buf)


#####  Utility functions here

_userConfigControl = True
_sealFlag = False


def i2cReadBytes(subaddress, count):
    buf = bytearray([subaddress])
    m.writeto(BQ72441_I2C_ADDRESS, buf)
    x = m.readfrom(BQ72441_I2C_ADDRESS, count)
    return x


def i2cWriteBytes(subaddress, src):
    buf = bytearray([subaddress])
    buf.extend(src)
    m.writeto(BQ72441_I2C_ADDRESS, buf)


def readControlWord(controlWord):
    msb = (controlWord >> 8) & 0xff
    lsb = controlWord & 0xff
    command = bytearray([lsb, msb])
    i2cWriteBytes(0, command)
    x = i2cReadBytes(0, 2)
    return ((x[1] << 8) & 0xff00) | (x[0] & 0xff)


def readWord(commandWord):
    x = i2cReadBytes(commandWord, 2)
    return ((x[1] << 8) & 0xff00) | (x[0] & 0xff)


def executeControlWord(func):
    msb = (func >> 8) & 0xff
    lsb = func & 0xff
    buf = bytearray([lsb, msb])
    i2cWriteBytes(0, buf)
    return True


def softReset():
    return executeControlWord(BQ27441_CONTROL_SOFT_RESET)


def sealed():
    stat = status()
    retval = False
    if (stat & BQ27441_STATUS_SS) > 0:
        retval = True
    return retval


def seal():
    return readControlWord(BQ27441_CONTROL_SEALED) > 0


def unseal():
    executeControlWord(BQ27441_UNSEAL_KEY)
    executeControlWord(BQ27441_UNSEAL_KEY)
    return True


def enterConfig(userControl):
    if userControl:
        _userConfigControl = True;

    if (sealed()):
        _sealFlag = True;
        unseal()

    if executeControlWord(BQ27441_CONTROL_SET_CFGUPDATE):
        timeout = BQ72441_I2C_TIMEOUT
        while (timeout > 0) and ((flags() & BQ27441_FLAG_CFGUPMODE) == 0):
            timeout -= 1
            utime.sleep_ms(1)

        if timeout > 0:
            return True

    return False


def exitConfig(resim):
    if resim:
        if softReset():
            timeout = BQ72441_I2C_TIMEOUT
            while (timeout > 0) and ((flags() & BQ27441_FLAG_CFGUPMODE) == 0):
                timeout -= 1
                utime.sleep_ms(1)
            if timeout > 0:
                if _sealFlag:
                    seal()
                return True
        return False
    else:
        return executeControlWord(BQ27441_CONTROL_EXIT_CFGUPDATE)


#####  Extended Data functions

def blockDataControl():
    buf = bytearray([0])
    i2cWriteBytes(BQ27441_EXTENDED_CONTROL, buf)
    return True


def blockDataClass(id):
    buf = bytearray([id])
    i2cWriteBytes(BQ27441_EXTENDED_DATACLASS, buf)
    return True


def blockDataChecksum():
    x = i2cReadBytes(BQ27441_EXTENDED_CHECKSUM, 1)
    return x[0]


def computeBlockChecksum():
    x = i2cReadBytes(BQ27441_EXTENDED_BLOCKDATA, 32)
    csum = 0
    for i in range(32):
        csum = csum + x[i]
        csum = csum & 0xff
    csum = 255 - csum
    return csum


def blockDataOffset(offset):
    buf = bytearray([offset])
    i2cWriteBytes(BQ27441_EXTENDED_DATABLOCK, buf)
    return True


def readBlockData(offset):
    address = offset + BQ27441_EXTENDED_BLOCKDATA
    x = i2cReadBytes(address, 1)
    return x[0]


def writeBlockData(offset, data):
    address = offset + BQ27441_EXTENDED_BLOCKDATA
    buf = bytearray([data])
    return i2cWriteBytes(address, buf)


def writeBlockChecksum(csum):
    buf = bytearray([csum])
    return i2cWriteBytes(BQ27441_EXTENDED_CHECKSUM, buf)


def readExtendedData(classID, offset):
    if _userConfigControl:
        enterConfig(False)

    if blockDataControl() == False:
        return False
    if blockDataClass(classID) == False:
        return False

    blockDataOffset(int(offset / 32))
    computeBlockChecksum()
    oldCsum = blockDataChecksum()
    retData = readBlockData(offset % 32)

    if _userConfigControl == False:
        exitConfig(False)

    return retData


def writeExtendedData(classID, offset, data):
    length = len(data)

    if length > 32:
        return False

    if _userConfigControl:
        enterConfig(False)

    if blockDataControl() == False:
        return False
    if blockDataClass(classID) == False:
        return False

    blockDataOffset(int(offset / 32))
    computeBlockChecksum()
    oldCsum = blockDataChecksum()

    for i in range(length):
        writeBlockData((offset % 32) + i, data[i])

    newCsum = computeBlockChecksum()
    writeBlockChecksum(newCsum)

    if _userConfigControl == False:
        exitConfig(False)

    return True


# other helpful bits

def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)  # compute negative value
    return val  # return positive value as is


def hexdump(src, length=16):
    result = []
    digits = 2
    for i in range(0, len(src), length):
        s = src[i:i + length]
        hexa = " ".join(map("{0:0>2X}".format, s))
        text = "".join([chr(x) if 0x20 <= x < 0x7F else "." for x in s])
        result.append("%04X   %-*s   %s" % (i, length * (digits + 1), hexa, text))
    return "\n".join(result)
