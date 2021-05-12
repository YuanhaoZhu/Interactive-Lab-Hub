import time
from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import qwiic_joystick



cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000
spi = board.SPI()
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


height = disp.width  
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Enable the buttons for demo
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)

# Define default coordination
x, y = 0, 0

# Enable the joystick
joystick = qwiic_joystick.QwiicJoystick()

if joystick.is_connected() == False:
    print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
        file=sys.stderr)

joystick.begin()

print("Initialized. Firmware Version: %s" % joystick.get_version())

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 

    # Get current time hour 
    hour = int(strftime("%H"))

    print("X: %d, Y: %d, Button: %d" % ( \
            joystick.get_horizontal(), \
            joystick.get_vertical(), \
            joystick.get_button()))

    time.sleep(0.1)

    # Button Push
    # while joystick.get_button() == 0:
    #     ma_img = Image.open("mawen.jpeg")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)

    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)
    # Left
    while 500 < joystick.get_horizontal() <= 600 and joystick.get_vertical() == 0:
        ma_img = Image.open("species_icon/human.png")
        ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
        disp.image(ma_img, rotation)
        time.sleep(0.1)
    # Upper Left
    # while joystick.get_horizontal() == 1023 and 0 <= joystick.get_vertical() < 100:
    #     ma_img = Image.open("2.png")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)
    # Up
    while joystick.get_horizontal() == 1023 and 500 <= joystick.get_vertical() < 600:
        ma_img = Image.open("species_icon/pikachu.png")
        ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
        disp.image(ma_img, rotation)
        time.sleep(0.1)
    # Upper Right
    # while joystick.get_horizontal() == 1023 and 1000 <= joystick.get_vertical() < 1024:
    #     ma_img = Image.open("4.png")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)
    # Right
    while 500 <= joystick.get_horizontal() < 600 and 0 <= joystick.get_vertical() == 1023:
        ma_img = Image.open("species_icon/dog.png")
        ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
        disp.image(ma_img, rotation)
        time.sleep(0.1)
    # Lower Right
    # while joystick.get_horizontal() == 0 and 1000 <= joystick.get_vertical() < 1024:
    #     ma_img = Image.open("6.png")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)
    # Down
    # while joystick.get_horizontal() == 0 and 500 <= joystick.get_vertical() < 600:
    #     ma_img = Image.open("7.png")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)
    # Lower Left
    # while 0 <=joystick.get_horizontal() < 100 and 0 <= joystick.get_vertical() < 100:
    #     ma_img = Image.open("8.png")
    #     ma_img = ma_img.resize((240, 135), Image.BICUBIC)
    
    #     disp.image(ma_img, rotation)
    #     time.sleep(0.1)

 




    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
