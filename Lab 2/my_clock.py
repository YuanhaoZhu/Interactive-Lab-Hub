import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import webcolors


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

current_time = time.strftime("%H:%M:%S") 

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    y = top
    draw.text((x, y), current_time, font=font, fill="#FFFFFF")

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 

    if buttonB.value and not buttonA.value:# just button A pressed
        y = top
        draw.text((x, y), "IP", font=font, fill="#FFFFFF")
        y += font.getsize()
        draw.text((x, y), "WTTR", font=font, fill="#FFFF00")
        y += font.getsize()
        draw.text((x, y), "USD", font=font, fill="#0000FF")
        y += font.getsize()
        draw.text((x, y), "Temp", font=font, fill="#FF00FF")

    if buttonA.value and not buttonB.value:# just button B pressed
       y = top
       draw.rectangle((0, 0, width, height), outline=0, fill=0)
       timezone = timezone - 1
       clock = datetime.now() + timedelta(hours=timezone)
       draw.text((x,y), "Subtracted one hour", font=font, fill="#FFFFFF")
    
    
    
    if not buttonA.value and not buttonB.value:
       draw.text((x,y), clock, font=font, fill="#FFFFFF")



    # if buttonB.value and not buttonA.value:  # just button A pressed
    #     disp.fill(screenColor) # set the screen to the users color
    if buttonA.value and not buttonB.value:  # just button B pressed
        disp.fill(color565(255, 255, 255))  # set the screen to white
    # if not buttonA.value and not buttonB.value:  # none pressed
    #     disp.fill(color565(0, 255, 0))  # green




    # Display image.
    disp.image(image, rotation)
    time.sleep(1)