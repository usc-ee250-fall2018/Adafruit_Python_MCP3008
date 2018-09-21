""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.

"""

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration
# Port and device are 0 becuase we are using SPI0 on your RPi
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

if __name__ == '__main__':
