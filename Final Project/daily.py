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


import pygame
import sys
import time


import qwiic_button


pygame.font.init()
# Initialize all LED buttons
buttonRed = qwiic_button.QwiicButton(0x33)
buttonGreen = qwiic_button.QwiicButton(0x66)

buttonGreen.begin()
buttonRed.begin()

buttonGreen.LED_off()
buttonRed.LED_off()


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
	OLEDdraw = ImageDraw.Draw(imageTemp)
	textTemp1 = f"{int(temp)}"
	Temp_after_coma = f"{(temp):.2f}".split('.')[1] 
	textTemp2 = f".{Temp_after_coma}"
	textTemp3 = "℃"
	OLEDdraw.text((89, 0), textTemp1, font=bigfont, fill=255)
	OLEDdraw.text((89, 18), textTemp2, font=font, fill=255)
	OLEDdraw.text((112, 16), textTemp3, font=midfont, fill=255)
	if temp >= 30 and temp <= 41:
		OLEDdraw.rectangle((29, 11, 29 + (temp-30)*5, 21), outline=255, fill=255)
	elif temp >= 41:
		OLEDdraw.rectangle((29, 11, 29 + 55, 21), outline=255, fill=255)
	
	if temp >= 38:
		OLEDdraw.text((23, 8), "FEVER!!!", font=midfont, outline=0,fill=0)
	oled.image(imageTemp)
	oled.show()
#measure for one minutes



# initializing the constructor
pygame.init()


#Score for COVID indicator
score = 0

frame =1


# screen resolution
res = (800,480)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
white = (255,255,255)
black = (0,0,0)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()


# defining a font
bigfont = pygame.font.SysFont('Corbel',50)
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('quit' , True , white)

bg1 = pygame.image.load('screen1.png').convert()
bg1 = pygame.transform.scale(bg1, (800,480))

# bg2 = pygame.image.load('screen2.png').convert()
# bg2 = pygame.transform.scale(bg2, (800,480))

# bg3 = pygame.image.load('screen3.png').convert()
# bg3 = pygame.transform.scale(bg3, (800,480))

# bg4 = pygame.image.load('screen4.png').convert()
# bg4 = pygame.transform.scale(bg4, (800,480))

# bg5 = pygame.image.load('screen5.png').convert()
# bg5 = pygame.transform.scale(bg5, (800,480))

left_padding = 100







def IntroScreen():
	global frame
	frame = 1

	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			#if the mouse is clicked on the button the game is terminated
			if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
				pygame.quit()
			
				
	# fills the screen with a color
	screen.fill(white)
	rectbg1 = bg1.get_rect()

	rectbg1 = rectbg1.move((0, 0))
	screen.blit(bg1, rectbg1)
	# screen.blit(bg1, (0, 0))

	# if mouse is hovered on a button it
	# changes to lighter shade
	if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
		pygame.draw.rect(screen,color_light,[left_padding,20,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[left_padding,20,140,40])
	
	# superimposing the text onto our button
	screen.blit(text , (left_padding+50,25))


	
	# updates the frames of the game
	# pygame.display.update()

	# buttonRed.LED_on(50)
	# buttonGreen.LED_on(50)
	# if buttonGreen.is_button_pressed():
	# 	frame = 2
	# 	break
	# elif buttonRed.is_button_pressed():
	# 	pygame.quit()
				
		


def secScreen():
	while True:
		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
				
			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:
				#if the mouse is clicked on the button the game is terminated
				if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
					pygame.quit()
					
		# fills the screen with a color
		screen.fill(white)
		rectbg2 = bg2.get_rect()

		rectbg2 = rectbg2.move((0, 0))
		screen.blit(bg2, rectbg2)
		# screen.blit(bg1, (0, 0))

		# stores the (x,y) coordinates into
		# the variable as a tuple
		mouse = pygame.mouse.get_pos()

		# if mouse is hovered on a button it
		# changes to lighter shade
		if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
			pygame.draw.rect(screen,color_light,[left_padding,20,140,40])
			
		else:
			pygame.draw.rect(screen,color_dark,[left_padding,20,140,40])

		# superimposing the text onto our button
		screen.blit(text , (left_padding+50,25))

		# updates the frames of the game
		pygame.display.update()

		if buttonGreen.is_button_pressed():
			global frame
			frame = 3
			break
		elif buttonRed.is_button_pressed():
			pygame.quit()
			frame = 3
			global score 
			score = 1
			break
			
def showScreen(picture, currentscreenNum):
	while True:
		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
				
			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:
				#if the mouse is clicked on the button the game is terminated
				if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
					pygame.quit()
					
		# fills the screen with a color
		screen.fill(white)
		rectbg = picture.get_rect()

		rectbg = rectbg.move((0, 0))
		screen.blit(picture, rectbg)
		# screen.blit(bg1, (0, 0))

		# stores the (x,y) coordinates into
		# the variable as a tuple
		mouse = pygame.mouse.get_pos()

		# if mouse is hovered on a button it
		# changes to lighter shade
		if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
			pygame.draw.rect(screen,color_light,[left_padding,20,140,40])
			
		else:
			pygame.draw.rect(screen,color_dark,[left_padding,20,140,40])

		# superimposing the text onto our button
		screen.blit(text , (left_padding+50,25))

		# updates the frames of the game
		pygame.display.update()
		buttonRed.LED_on(50)
		buttonGreen.LED_on(50)


		# while currentscreenNum == 1:
		# 	# execfile('file.py')
		# 	# exec(open("OLED.py").read())
		# 	# break
		# 	from OLED.py import showTemp
		# 	from OLED.py import getbodyTemp
		# 	countDown = 10
		# 	playsound('/home/pi/Interactive-Lab-Hub/Final Project/temp_start.mp3')
		# 	playsound('beep.mp3')
		# 	while countDown >0 :


		# 		temp = getbodyTemp()
		# 		showTemp(temp) 
		# 		time.sleep(0.25) 
		# 		countDown = countDown - 0.25
		# 		print (countDown)
		# 	playsound('dingdang.mp3')
		# 	playsound('temp_end.mp3')
		# 	break

			

		if buttonRed.is_button_pressed() or buttonGreen.is_button_pressed():
			global frame
			frame = currentscreenNum+1
			break
		# elif buttonGreen.is_button_pressed():
		# 	pygame.quit()
			# frame = 3
			# global score 
			# score = 1
			# break





while True:
	bg = pygame.image.load(f'screen{frame}.png').convert()
	bg = pygame.transform.scale(bg, (800,480))
	print(frame)
	showScreen(bg, frame)
	# if frame == 5:
	# 	playsound('/home/pi/Interactive-Lab-Hub/Final Project/temp_start.mp3')
	# 	playsound('beep.mp3')
	# 	while countDown >0 :
	# 		temp = getbodyTemp()
	# 		showTemp(temp) 
	# 		time.sleep(0.25) 
	# 		countDown = countDown - 0.25
	# 		print (countDown)
	# 	playsound('dingdang.mp3')
	# 	playsound('temp_end.mp3')
	# 	break
	time.sleep(1)
	# # IntroScreen()
	# if frame == 1:
		
	# 	break
	# if frame == 2:
	# 	showScreen(bg3, 2)
	# 	break
	# if frame == 3:
	# 	showScreen(bg3, 3)
	# 	break
	# if frame == 4:
	# 	showScreen(bg4, 4)
	# 	break
	# if frame == 5 or frame == 6:
	# 	showScreen(bg5, 5)
	# 	break
	# else:
	# 	break



	
	
	# for ev in pygame.event.get():
		
	# 	if ev.type == pygame.QUIT:
	# 		pygame.quit()
			
	# 	#checks if a mouse is clicked
	# 	if ev.type == pygame.MOUSEBUTTONDOWN:
			
	# 		#if the mouse is clicked on the
	# 		# button the game is terminated
	# 		if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
	# 			pygame.quit()
				
	# # fills the screen with a color
	# screen.fill(white)
	
	# # stores the (x,y) coordinates into
	# # the variable as a tuple
	# mouse = pygame.mouse.get_pos()
	
	# # if mouse is hovered on a button it
	# # changes to lighter shade
	# if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
	# 	pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
	# else:
	# 	pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
	
	# # superimposing the text onto our button
	# screen.blit(text , (width/2+50,height/2))
	
	# # updates the frames of the game
	# pygame.display.update()
