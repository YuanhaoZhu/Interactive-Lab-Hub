import time
import board
import busio
import adafruit_mpr121
import subprocess
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
# cap sensor config
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#oled config
# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)




def OLEDdo():
	# Clear display.
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
	draw.text((0, 0), text, font=font2, fill=255)
	text2 = time.strftime("%e %b %Y")
	draw.text((0, 14), text2, font=font2, fill=255)

	oled.image(imageOLED)
	oled.show()

	time.sleep(1)



def showNotice(i):
	draw.rectangle((0, 0, width, height), outline=0, fill=0)
	title = "You scheduled an"
	title2 = f"event at {i}:00 PM"
	#timeline = f"{i}:00 PM"
	y = top
	draw.text((x, y), title, font=font, fill="#FFFFFF")
	y += font.getsize(title)[1]
	draw.text((x, y), title2, font=font, fill="#FFFFFF")
	y += font.getsize(title2)[1]
	#draw.text((x, y), timeline, font=font, fill="#FFFFFF")
	disp.image(image, rotation)
	time.sleep(0.1)


while True:
	OLEDdo()
	for i in range(12):
		if mpr121[i].value:
			showNotice(i)
	time.sleep(0.25) 