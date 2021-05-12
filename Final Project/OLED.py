import time
import math
import board
import busio
import subprocess
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import Adafruit_GPIO.SPI as SPI
#for temp sensor
import adafruit_mcp9808
from playsound import playsound

###Temp####
i2c = board.I2C()  # uses board.SCL and board.SDA
mcp = adafruit_mcp9808.MCP9808(i2c)
def getbodyTemp():
    tempC = mcp.temperature + 3
    return tempC
###end temp######

# diplay config
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
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
midfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
bigfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#oled config
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Get display width and height.
width = oled.width
height = oled.height



def OLEDtime():
    oled.fill(0)
    oled.show()
    # Create blank image for drawing.
    imageOLED = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(imageOLED)
    # Load a font in 2 different sizes.
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    # write the current time to the display after each scroll
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    # text = time.strftime("%A")
    text = time.strftime("%H:%M:%S")
    draw.text((0, 0), text, font=font, fill=255)
    text2 = time.strftime("%e %b %Y")
    draw.text((0, 14), text2, font=font, fill=255)
    oled.image(imageOLED)
    oled.show()
    time.sleep(1)



def showTemp(temp):
    imageTemp = Image.open('temp.ppm').convert('1')
    draw = ImageDraw.Draw(imageTemp)
    textTemp1 = f"{int(temp)}"
    Temp_after_coma = f"{(temp):.2f}".split('.')[1] 
    textTemp2 = f".{Temp_after_coma}"
    textTemp3 = "℃"
    draw.text((89, 0), textTemp1, font=bigfont, fill=255)
    draw.text((89, 18), textTemp2, font=font, fill=255)
    draw.text((112, 16), textTemp3, font=midfont, fill=255)
    if temp >= 30 and temp <= 41:
        draw.rectangle((29, 11, 29 + (temp-30)*5, 21), outline=255, fill=255)
    elif temp >= 41:
        draw.rectangle((29, 11, 29 + 55, 21), outline=255, fill=255)
    
    if temp >= 38:
        draw.text((23, 8), "FEVER!!!", font=midfont, outline=0,fill=0)
    oled.image(imageTemp)
    oled.show()
#measure for one minutes
countDown = 60
while True:
    playsound('/home/pi/Interactive-Lab-Hub/Final Project/temp_start.mp3')
    playsound('beep.mp3')
    while countDown >0 :
        temp = getbodyTemp()
        showTemp(temp) 
        time.sleep(0.25) 
        countDown = countDown - 0.25
        print (countDown)
    playsound('dingdang.mp3')
    playsound('temp_end.mp3')
    break

