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

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.


# Documentation
Material:

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

### Prepare web server
Create virtual environment
```
pi@ixe00:~ $ virtualenv woz
pi@ixe00:~ $ source woz/bin/activate
(woz) pi@yourHostname:~ $ cd Interactive-Lab-Hub/Lab\ 3/demo
(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/demo $ 
(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/demo $ pip install -r requirements.txt
(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/demo $ python app.py
```
