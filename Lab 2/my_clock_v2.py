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
mediumfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font40 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)


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

# Image Formatting
def image_format(picture, width, height):
    picture = picture.convert('RGB')
    picture = picture.resize((240, 135), Image.BICUBIC)

    return picture


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
        
        endPic = Image.open(r"pomoPic/pomodoro1.png")
        endPic = image_format(endPic, width, height)
        draw = ImageDraw.Draw(endPic)
        # disp.image(endPic, rotation)
        x = 20
        y = height/2 - 25
        draw.text((x, y), "pomodoro", font=font40, fill="#FFFFFF")
        disp.image(endPic, rotation)



        # draw.rectangle((0, 0, width, height), outline=0, fill="#112536")

        

        t=1500
        pic = 25

        while t > 0: #set a 25 mins timer
            mins, secs = divmod(t, 60) 
            pomotimer = '{:02d}:{:02d}'.format(mins, secs) 
            #print(pomotimer, end="\r") 
            time.sleep(1) 
            if t <=1500:
                pic = 26 - t // 60 
            else:
                pic = 1
            

            t -= 1

            tomatoPath = f"pomoPic/pomodoro{pic}.png"

            tomatoPic = Image.open(tomatoPath)
            tomatoPic = image_format(tomatoPic, width, height)

            draw = ImageDraw.Draw(tomatoPic)

            x = width - mediumfont.getsize(pomotimer)[0]-8
            y = 8
            draw.text((x, y), pomotimer, font=mediumfont, fill="#FFFFFF")

            x = 8
            y = 8
            draw.text((x, y), "+1min", font=smallfont, fill="#FFFFFF")

            x = 8
            y = height - 25
            draw.text((x, y), "-1min", font=smallfont, fill="#FFFFFF")

            disp.image(tomatoPic, rotation)

            if buttonB.value and not buttonA.value:#press a
                t += 60
            if buttonA.value and not buttonB.value:#press b
                t -= 60
            if not buttonA.value and not buttonB.value:
                break


            

        
        # time.sleep(5)

        # if buttonA.value and not buttonB.value:
        #     break



        

    if not buttonA.value and not buttonB.value:
    
        n=1
        t=60
        while (t > 0) and (n < 16):

            # Create blank image for drawing.
            # Make sure to create image with mode 'RGB' for full color.

            # if disp.rotation % 180 == 90:
            #     height = disp.width  # we swap height/width to rotate it to landscape!
            #     width = disp.height
                
            # else:
            #     width = disp.width  # we swap height/width to rotate it to landscape!
            #     height = disp.height

            # image = Image.new("RGB", (width, height))

            # # Get drawing object to draw on image.
            # draw = ImageDraw.Draw(image)
            # pictureName = f"hourglass{n}.png"
            # image = Image.open(pictureName)
            # n=n+1
            
            # # Scale the image to the smaller screen dimension
            # image_ratio = image.width / image.height
            # screen_ratio = width / height
            
            # if screen_ratio < image_ratio:
            #     scaled_width = image.width * height // image.height
            #     scaled_height = height
            # else:
            #     scaled_width = width
            #     scaled_height = image.height * width // image.width
            # image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

            # # Crop and center the image
            # x = scaled_width // 2 - width // 2
            # y = scaled_height // 2 - height // 2
            # image = image.crop((x, y, x + width, y + height))

            hourglassPath = f"hourglassPic/hourglass{n}.png"
            hourglassPic = Image.open(hourglassPath)
            hourglassPic = image_format(hourglassPic, width, height)
            draw = ImageDraw.Draw(hourglassPic)
            n=n+1

            # Display image.
            disp.image(hourglassPic, rotation)
            t=t-4
            time.sleep(4)






        






    # Display image.
    #disp.image(image, rotation)
    #time.sleep(1)