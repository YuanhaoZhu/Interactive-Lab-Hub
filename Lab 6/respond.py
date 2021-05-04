import paho.mqtt.client as mqtt
import uuid
import qwiic_button
import time
import subprocess
import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont


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
# Display the image
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)


backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Topic for sending messages
this_topic = "IDD/respond"
# Topic for reading messages
other_topic = "IDD/proximity"

on_text = "I'm available now, feel free to reach out."
away_text = "I'm away."


#this is the callback that gets called once we connect to the broker.
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(other_topic)

# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    global status
    

    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    text = msg.payload.decode('UTF-8')

    if text == currMove:
        score += 1
    else:
        client.publish(this_topic, "Game over! Final score was " + str(score) + ". Restarting game.")
        score = 0
        y = top
        screen_text = "GAME OVER!"
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        draw.text((x, y), screen_text, font=font, fill="#FF0000")
        disp.image(image, rotation)
        time.sleep(2)

    y = top
    screen_text = "Current score: " + str(score)
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    draw.text((x, y), screen_text, font=font, fill="#FFFFFF")
    disp.image(image, rotation)

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect('farlab.infosci.cornell.edu',port=8883)

# Initialize all LED buttons
buttonGreen = qwiic_button.QwiicButton(0x33)
buttonRed = qwiic_button.QwiicButton(0x66)

buttonGreen.begin()
buttonRed.begin()

buttonGreen.LED_off()
buttonRed.LED_off()


# Loop to read in the input from controller to send to dancer
while True:
    client.loop()

    if buttonGreen.is_button_pressed():
        client.publish(this_topic, "LEFT")
        currMove = 'L'
    elif buttonRed.is_button_pressed():
        client.publish(this_topic, "RIGHT")
        currMove = 'R'

    time.sleep(0.5)
