#!/usr/bin/env python
# coding: latin-1
"""
This module is designed to communicate with the XLoBorg

busNumber               I²C bus on which the XLoBorg is attached (Rev 1 is bus 0, Rev 2 is bus 1)
bus                     the smbus object used to talk to the I²C bus
addressAccelerometer    The I²C address of the accelerometer chip
addressCompass          The I²C address of the compass chip
foundAccelerometer      True if the accelerometer chip can be seen, False otherwise
foundCompass            True if the compass chip can be seen, False otherwise
printFunction           Function reference to call when printing text, if None "print" is used
gPerCount               Number of G represented by the LSB of the accelerometer at the current sensitivity
tempOffest              The offset to add to the temperature reading in °C
"""

# Import the libraries we need
import smbus
import struct

### MODULE DATA ###
# Shared values used by this module
global busNumber
global bus
global addressAccelerometer
global addressCompass
global foundAccelerometer
global foundCompass
global printFunction
global gPerCount
global tempOffest 

# Constant values
addressAccelerometer = 0x1C
addressCompass = 0x0E

# Check here for Rev 1 vs Rev 2 and select the correct bus
busNumber = 1

### MODULE FUNCTIONS ###
def Print(message):
    """
Print(message)

Wrapper used by the XLoBorg module to print messages, will call printFunction if set, print otherwise
    """
    global printFunction
    if printFunction == None:
        print message
    else:
        printFunction(message)

def NoPrint(message):
    """
NoPrint(message)

Does nothing, intended for disabling diagnostic printout by using:
XLoBorg.printFunction = XLoBorg.NoPrint
    """
    pass

def Init(tryOtherBus = True):
    """
Init([tryOtherBus])

Prepare the I2C driver for talking to the XLoBorg
If tryOtherBus is True or omitted, this function will attempt to use the other bus if none of the XLoBorg devices can be found on the current busNumber
    """
    global busNumber
    global bus
    global addressAccelerometer
    global addressCompass
    global foundAccelerometer
    global foundCompass

    Print('Loading XLoBorg on bus %d' % (busNumber))

    # Open the bus
    bus = smbus.SMBus(busNumber)

    # Check for accelerometer
    try:
        byte = bus.read_byte_data(addressAccelerometer, 1)
        foundAccelerometer = True
        Print('Found accelerometer at %02X' % (addressAccelerometer))
    except:
        foundAccelerometer = False
        Print('Missing accelerometer at %02X' % (addressAccelerometer))

    # Check for compass
    try:
        byte = bus.read_byte_data(addressCompass, 1)
        foundCompass = True
        Print('Found compass at %02X' % (addressCompass))
    except:
        foundCompass = False
        Print('Missing compass at %02X' % (addressCompass))

    # See if we are missing chips
    if not (foundAccelerometer or foundCompass):
        Print('Both the compass and accelerometer were not found')
        if tryOtherBus:
            if busNumber == 1:
                busNumber = 0
            else:
                busNumber = 1
            Print('Trying bus %d instead' % (busNumber))
            Init(False)
        else:
            Print('Are you sure your XLoBorg is properly attached, and the I2C drivers are running?')
            bus = None
    else:
        Print('XLoBorg loaded on bus %d' % (busNumber))
        if foundAccelerometer:
            InitAccelerometer()
        if foundCompass:
            InitCompass()

def InitAccelerometer():
    """
InitAccelerometer()

Initialises the accelerometer on bus to default states
    """
    global bus
    global addressAccelerometer
    global gPerCount

    # Setup mode configuration
    register = 0x2A             # CTRL_REG1
    data =  (0 << 6)            # Sleep rate 50 Hz
    data |= (0 << 4)            # Data rate 800 Hz
    data |= (0 << 2)            # No reduced noise mode
    data |= (1 << 1)            # Normal read mode
    data |= (1 << 0)                # Active
    try:
        bus.write_byte_data(addressAccelerometer, register, data)
    except:
        Print('Failed sending CTRL_REG1!')

    # Setup range
    register = 0x0E             # XYZ_DATA_CFG
    data = 0x00                 # Range 2G, no high pass filtering
    try:
        bus.write_byte_data(addressAccelerometer, register, data)
    except:
        Print('Failed sending XYZ_DATA_CFG!')
    gPerCount = 2.0 / 128       # 2G over 128 counts

    # System state
    register = 0x0B             # SYSMOD
    data = 0x01                 # Awake mode
    try:
        bus.write_byte_data(addressAccelerometer, register, data)
    except:
        Print('Failed sending SYSMOD!')

    # Reset ready for reading
    register = 0x00             
    try:
        bus.write_byte(addressAccelerometer, register)
    except:
        Print('Failed sending final write!')
            
def InitCompass():
    """
InitCompass()

Initialises the compass on bus to default states
    """
    global bus
    global addressCompass

    # Acquisition mode
    register = 0x11             # CTRL_REG2
    data  = (1 << 7)            # Reset before each acquisition
    data |= (1 << 5)            # Raw mode, do not apply user offsets
    data |= (0 << 5)            # Disable reset cycle
    try:
        bus.write_byte_data(addressCompass, register, data)
    except:
        Print('Failed sending CTRL_REG2!')

    # System operation
    register = 0x10             # CTRL_REG1
    data  = (0 << 5)            # Output data rate (10 Hz when paired with 128 oversample)
    data |= (3 << 3)            # Oversample of 128
    data |= (0 << 2)            # Disable fast read
    data |= (0 << 1)            # Continuous measurement
    data |= (1 << 0)            # Active mode
    try:
        bus.write_byte_data(addressCompass, register, data)
    except:
        Print('Failed sending CTRL_REG1!')

def ReadAccelerometer():
    """
x, y, z = ReadAccelerometer()

Reads the X, Y and Z axis force, in terms of Gs
    """
    global bus
    global addressAccelerometer
    global gPerCount

    # Read the data from the accelerometer chip
    try:
        [status, x, y, z] = bus.read_i2c_block_data(addressAccelerometer, 0, 4)
    except:
        Print('Failed reading registers!')
        status = 0
        x = 0
        y = 0
        z = 0
    
    # Convert from unsigned to correctly signed values
    bytes = struct.pack('BBB', x, y, z)
    x, y, z = struct.unpack('bbb', bytes)

    # Convert to Gs
    x *= gPerCount
    y *= gPerCount
    z *= gPerCount

    return x, y, z


def ReadCompassRaw():
    """
x, y, z = ReadCompassRaw()

Reads the X, Y and Z axis raw magnetometer readings
    """
    global bus
    global addressCompass

    # Read the data from the compass chip
    try:
        bus.write_byte(addressCompass, 0x00)
        [status, xh, xl, yh, yl, zh, zl, who, sm, oxh, oxl, oyh, oyl, ozh, ozl, temp, c1, c2] = bus.read_i2c_block_data(addressCompass, 0, 18)
    except:
        Print('Failed reading registers!')
        status = 0
        xh = 0
        xl = 0
        yh = 0
        yl = 0
        zh = 0
        zl = 0
    
    # Convert from unsigned to correctly signed values
    bytes = struct.pack('BBBBBB', xl, xh, yl, yh, zl, zh)
    x, y, z = struct.unpack('hhh', bytes)

    return x, y, z

def ReadTemperature():
    """
temp = ReadTemperature()

Reads the die temperature of the compass in degrees Celsius
    """
    global bus
    global addressCompass
    global tempOffest 

    # Read the data from the compass chip
    try:
        bus.write_byte(addressCompass, 0x00)
        [status, xh, xl, yh, yl, zh, zl, who, sm, oxh, oxl, oyh, oyl, ozh, ozl, temp, c1, c2] = bus.read_i2c_block_data(addressCompass, 0, 18)
    except:
        Print('Failed reading registers!')
        temp = 0
    
    # Convert from unsigned to correctly signed values
    bytes = struct.pack('B', temp)
    temp = struct.unpack('b', bytes)[0]
    temp += tempOffset

    return temp

### STARTUP ROUTINES ###
# Default user settings
printFunction = None
tempOffset = 0

# Auto-run code if this script is loaded directly
if __name__ == '__main__':
    # Load additional libraries
    import time
    # Start the XLoBorg module (sets up devices)
    Init()
    try:
        # Loop indefinitely
        while True:
            # Read the 
            x, y, z = ReadAccelerometer()
            mx, my, mz = ReadCompassRaw()
            temp = ReadTemperature()
            print 'X = %+01.4f G, Y = %+01.4f G, Z = %+01.4f G, mX = %+06d, mY = %+06d, mZ = %+06d, T = %+03d°C' % (x, y, z, mx, my, mz, temp)
            time.sleep(0.1)
    except KeyboardInterrupt:
        # User aborted
        pass

