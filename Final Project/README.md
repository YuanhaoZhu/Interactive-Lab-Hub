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

### Intall web browser
Reference: [Installing the Chromium Web Browser on a Raspberry Pi](https://pimylifeup.com/raspberry-pi-chromium-browser/)
````
pi@ixe00:~ $ sudo apt update
pi@ixe00:~ $ sudo apt full-upgrade
pi@ixe00:~ $ sudo apt install chromium-browser -y
pi@ixe00:~ $ sudo reboot
````
After installed the Chromium Web Browser and reboot the pi, the icon of the browser appeared on my VNC desktop of pi.

![Chromium installed](https://user-images.githubusercontent.com/46579769/117605247-4ab1ba80-b125-11eb-9fde-cc08897c0676.png)


[Using a USB Audio Device with the Raspberry Pi](https://www.raspberrypi-spy.co.uk/2019/06/using-a-usb-audio-device-with-the-raspberry-pi/)
````
pi@ixe00:~ $ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 003: ID 04d8:0c02 Microchip Technology, Inc. 
Bus 001 Device 004: ID 1908:2070 GEMBIRD 
Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

````

