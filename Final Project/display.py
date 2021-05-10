# Setup the Display
import board
import displayio
import adafruit_hx8357
displayio.release_displays()
spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25
 
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = adafruit_hx8357.HX8357(display_bus, width=800, height=480, backlight_pin=board.D18)