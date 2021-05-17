# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing. 

## Deliverables

1. Documentation of design process
2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)
4. Reflections on process (What have you learned or wish you knew at the start?)


## Teams

I worked on my own.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.


# Documentation
Material:
- [HDMI 4 Pi: 5" Display w/Touch and Mini Driver - 800x480 HDMI](https://www.adafruit.com/product/2109)
- [USB speaker](https://www.adafruit.com/product/3369)
- [Stereo Enclosed Speaker Set - 3W 4 Ohm](https://www.adafruit.com/product/1669)- Not Used in the end
- OLED screen
- High accuracy temperature sensor
- Clear bricks

### Install web browser
Reference: [Installing the Chromium Web Browser on a Raspberry Pi](https://pimylifeup.com/raspberry-pi-chromium-browser/)
````
pi@ixe00:~ $ sudo apt update
pi@ixe00:~ $ sudo apt full-upgrade
pi@ixe00:~ $ sudo apt install chromium-browser -y
pi@ixe00:~ $ sudo reboot
````
After installed the Chromium Web Browser and reboot the pi, the icon of the browser appeared on my VNC desktop of pi.

<img src="https://user-images.githubusercontent.com/46579769/117605247-4ab1ba80-b125-11eb-9fde-cc08897c0676.png" height=400>


Opened the browser and tried to play Youtube Video.

<img src="https://user-images.githubusercontent.com/46579769/117606240-7766d180-b127-11eb-8d13-accea10d03a2.png" height=400>

However the [Stereo Enclosed Speaker Set - 3W 4 Ohm](https://www.adafruit.com/product/1669) I plugged into the mini driver for the HDMI diplay doesn't work. 

<img src="https://cdn-shop.adafruit.com/1200x900/1669-06.jpg" height=300>

I think I need to change the audio output into [USB speaker](https://www.adafruit.com/product/3369) instead.

<img src="https://cdn-shop.adafruit.com/1200x900/3369-00.jpg" height=300>

### Install speaker
In order to make us hear again (being deaf from previous SPK plug in stero speaker), we need to [update the ALSA config](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config).
> All we have to do is tell Raspbian to look at "card #1" for the default audio. Card #0 is the built in audio, so this is fairly straightforward.

> Run sudo nano /usr/share/alsa/alsa.conf and look for the following two lines:
> ````
> defaults.ctl.card 0
> defaults.pcm.card 0
> ````
> Change both “0” to “1” and then save the file. That’s it!

<img src="https://user-images.githubusercontent.com/46579769/117607237-8c446480-b129-11eb-81b3-e4d3ea06b603.png" height=400>

I found other usefull links to connect USB speaker to pi:[Using a USB Audio Device with the Raspberry Pi](https://www.raspberrypi-spy.co.uk/2019/06/using-a-usb-audio-device-with-the-raspberry-pi/). But I think above method is more straightforward and easy.

After testing, my speaker is finally working! :ear:

### Write Main Daily Check program
I've searching some ways to let pi directly write into the HDMI connected screen. 
Our TA @Ilan Mandel said I could use [pygame](https://www.pygame.org/news). 
I found another python toolkit to enable full screen on HDMI screen is [tkinter](https://realpython.com/python-gui-tkinter/), with [example I found](https://stackoverflow.com/questions/47856817/tkinter-canvas-based-kiosk-like-program-for-raspberry-pi?answertab=active#tab-top). 
After a few trials, I finally settled with pygame (but when I look back I think tkinter might be a better choice, because it's easier to work with buttons). 

I used Figma to design the UI of the Daily Check Machine, exported the unclickable elements, and imported them as .png into the pygame file. 

**Below is the user flow and my UI design of the Daily Check Machine**

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/final_project_userflow.png">

[Here is my main portion pygame code](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/daily.py)

Some other details to be noted: I imported [playsound](https://pypi.org/project/playsound/) to let pygame play sound (It also requires other packages and dependencies, but I lost track of them). I noticed once you imported the pygame, and initiate it, the entire .py file follows the pygame rule. So some method that I used to control the OLED screen etc., doesn't work inside pygame anymore. 

### Design and implement OLED screen and thermometer

**Below is my design of OLED display**

I used online [text-to-speech services](https://ttsmp3.com/) to generate voice notification, which helps users to correct control the timing of the thermometer. In addition, I also added "bell-ring" sound. The temperature sensor takes time to get stable value (it's similar to the analog Mercury thermometer). I tested a few times, and find about 1 minutes is a good time range to let readings climbing from room temperature to body temperature. 

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/OLED_design.png">

[Here is OLED code](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/OLED.py)




## Video of my friend using the Daily Check Machine for the first time
[Final Video](https://youtu.be/wWpC-DhkWuY)

## Reflections on process
What have you learned or wish you knew at the start?
1. I think Tkinter would be better than pygame for this project. when implementing the quit button, the mouse click events is associated with an area of the canvas. When you need to change the position of the button, you need to change both the shapes of the button, but also the range of when to respond to click event.
````
for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
				
			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:
				#if the mouse is clicked on the button the game is terminated
# you need to change here
				if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
					pygame.quit()
 
 
# You need to change here too!
		if left_padding <= mouse[0] <= left_padding+140 and 20 <= mouse[1] <= 20+40:
			pygame.draw.rect(screen,color_light,[left_padding,20,140,40])
			
		else:
			pygame.draw.rect(screen,color_dark,[left_padding,20,140,40])
````
This feels like you're pressing a button that's printed on a sheet of paper. The button it's self is not an object. Whereas in tkinter, button looks more manageble. 
````
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
````
2. I feels like everyone is getting vaccinated and no longer needs the Daily Check any more. But the thermometer becomes a handy tool. When I got me second dose vaccine (right after the presentation), I got fever but I don't have a real thermometer. I ran the OLED.py and did get a convincing value (about 38 degrees Celsius, in fever range). At the same time, I realized that my rough tuning of the temperature sensor really worked. I added 3 degrees on the original reading from the temperature sensor [(code I used for testing sensor)](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/temp.py), because I noticed the sensor cannot be placed very tight on human skin, and the body temperature reading was always about 3 degrees lower.
