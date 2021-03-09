import time
import subprocess
import digitalio
import board
from datetime import datetime
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
x = 15

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
bigfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)
smallfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

#current_time = time.strftime("%H:%M") 

now = datetime.now() # current date and time
current_time = now.strftime("%H:%M")
date = now.strftime("%m/%d/%Y")



while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    x = 2
    y = 2
    draw.text((x, y), date, font=smallfont, fill="#FFFFFF")

    x = 15
    y = height/2 - 40
    draw.text((x, y), current_time, font=bigfont, fill="#FFFFFF")


    disp.image(image, rotation)
    time.sleep(1)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 

    if buttonB.value and not buttonA.value:# just button A pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        x = 15
        y = height/2 - 40

        t=1500
        pic = 0

        while t >0: #set a 25 mins timer
            mins, secs = divmod(t, 60) 
            pomotimer = '{:02d}:{:02d}'.format(mins, secs) 
            #print(pomotimer, end="\r") 
            time.sleep(1) 
            if t % 60 == 0:
                pic += 1
            t -= 1
            # draw.rectangle((0, 0, width, height), outline=0, fill=0)
            # adjustImg(r"pomoPic/pomodoro1.png")


            # image = Image.new("RGB", (width, height))

            # # Get drawing object to draw on image.
            # draw = ImageDraw.Draw(image)
            # # pictureName = f"hourglass{n}.png"
            # image = Image.open(r"pomoPic/pomodoro1.png")

            # image = adjustImg(image)


            # if disp.rotation % 180 == 90:
            #     height = disp.width  # we swap height/width to rotate it to landscape!
            #     width = disp.height
                
            # else:
            #     width = disp.width  # we swap height/width to rotate it to landscape!
            #     height = disp.height

            image = Image.new("RGB", (width, height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            # pictureName = f"hourglass{n}.png"
            image = Image.open(r"pomoPic/pomodoro1.png")
            # n=n+1
            
            # Scale the image to the smaller screen dimension
            image_ratio = image.width / image.height
            screen_ratio = width / height
            
            if screen_ratio < image_ratio:
                scaled_width = image.width * height // image.height
                scaled_height = height
            else:
                scaled_width = width
                scaled_height = image.height * width // image.width
            image = image.resize((scaled_width, scaled_height), Image.BICUBIC)





            draw.text((x, y), pomotimer, font=bigfont, fill="#FFFFFF")
            disp.image(image, rotation)

            if buttonA.value and not buttonB.value:
                break
        
        
        time.sleep(1)



        

    if not buttonA.value and not buttonB.value:
        n=1
        t=60
        while (t > 0) and (n < 16):

            # Create blank image for drawing.
            # Make sure to create image with mode 'RGB' for full color.

            if disp.rotation % 180 == 90:
                height = disp.width  # we swap height/width to rotate it to landscape!
                width = disp.height
                
            else:
                width = disp.width  # we swap height/width to rotate it to landscape!
                height = disp.height

            image = Image.new("RGB", (width, height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            pictureName = f"hourglass{n}.png"
            image = Image.open(pictureName)
            n=n+1
            
            # Scale the image to the smaller screen dimension
            image_ratio = image.width / image.height
            screen_ratio = width / height
            
            if screen_ratio < image_ratio:
                scaled_width = image.width * height // image.height
                scaled_height = height
            else:
                scaled_width = width
                scaled_height = image.height * width // image.width
            image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

            # Crop and center the image
            x = scaled_width // 2 - width // 2
            y = scaled_height // 2 - height // 2
            image = image.crop((x, y, x + width, y + height))

            # Display image.
            disp.image(image)
            t=t-4
            time.sleep(4)



        






    # Display image.
    #disp.image(image, rotation)
    #time.sleep(1)