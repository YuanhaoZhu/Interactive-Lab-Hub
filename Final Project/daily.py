import pygame
import sys
import time


import qwiic_button


# Initialize all LED buttons
buttonRed = qwiic_button.QwiicButton(0x33)
buttonGreen = qwiic_button.QwiicButton(0x66)

buttonGreen.begin()
buttonRed.begin()

buttonGreen.LED_off()
buttonRed.LED_off()


# initializing the constructor
pygame.init()

#frame counter
frame = 1
#Score for COVID indicator
score = 0



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

bg2 = pygame.image.load('screen2.png').convert()
bg2 = pygame.transform.scale(bg2, (800,480))




left_padding = 100



def IntroScreen():
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
	pygame.display.update()

	buttonRed.LED_on(50)
	buttonGreen.LED_on(50)
	# if buttonGreen.is_button_pressed():
	# 	frame = 2
	# 	break	
	# elif buttonRed.is_button_pressed():
	# 	pygame.quit()

	# print(frame)


def secScreen():
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




while True:
	IntroScreen()
	if buttonGreen.is_button_pressed():
		break

	secScreen()

	
	
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
