import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import webcolors
#refer to image.py
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import


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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

current_time = time.strftime("%H:%M") 






while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    y = top
    draw.text((x, y), current_time, font=font, fill="#FFFFFF")
    disp.image(image, rotation)
    time.sleep(1)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 

    if buttonB.value and not buttonA.value:# just button A pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top

        t=1500

        while t >0: #set a 25 mins timer
            mins, secs = divmod(t, 60) 
            pomotimer = '{:02d}:{:02d}'.format(mins, secs) 
            #print(pomotimer, end="\r") 
            time.sleep(1) 
            t -= 1
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((x, y), pomotimer, font=font, fill="#FFFFFF")
            disp.image(image, rotation)

            if buttonA.value and not buttonB.value:# just button B pressed
                break
        
        
        time.sleep(1)

        

    if buttonA.value and not buttonB.value:# just button B pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        draw.text((x, y), "exercise", font=font, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(1)

    
    if not buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        y = top
        draw.text((x,y), "nonono", font=font, fill="#FFFFFF")
        disp.image(image, rotation)
        time.sleep(1)






    # Display image.
    #disp.image(image, rotation)
    #time.sleep(1)