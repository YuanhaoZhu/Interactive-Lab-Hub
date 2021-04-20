# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
In order to make the webCam work, I downloaded VNC and operate everyting on VNC.

I tried face-detection with my friend's face:
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/face_detetction2.png" height="400">

I tried object-detection with my keys:
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/object_detetction1.png" height="400">

and a toilet paper roll:
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/object_detetction2.png" height="400">
#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

**Below is my process and experimentation**
1. Train [TeachableMachines](https://teachablemachine.withgoogle.com/train), and export models.
Here I choosed the image project because the exported model is compatible with python. 
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Train1.png" height="400">
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Train2.png" height="400">

The initial attempt has 6 classes.
- **husky**: I use Webcam to shoot the husky from many different angles, and no parts of me shown up on the images. Which leads to high accuracy when recognizing husky
- **empty_background**: I used the Webcam to film it during the day time, and the my closet door is closed. This caused some problems when I tested the machine at night, and I opened the closet door, which introduced too much noice and lower the accuracy.
- **keys**: I initially only used the photo of the keys, the background is my black table top. The machine cannot recognize the keys when I hold it on my hand. 
- **laundry_card**: I shoot the image of the front and back of the laundry card with the background of my black table top. The model has low accuracy on this class, and most of the time, it’s been recognized as AirPods.
- **airpods**: I shoot the image of the AirPods case and the AirPods with different angles, with the background of my black table top.
- **empty_table**: In order to get rid of the noise from the black table top that I used as background for training photo of keys, laundry_card and airpods, I took 3 pictures of the black table top.

Below is a video of me trying out the Teachable Machine with different objects. 

[![Video of trying out Teachable Machine](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/teachable_machine_video_cover.png)](https://youtu.be/jgfYqj3IG5U "Video of trying out Teachable Machine")



From the preview, the model often can correctly identfy the object that I trained it on. So I exported the model. 
I my selection for export is below:

> TensorFlow

> Model conversion type: Keras

Click "Download model", and move model to desired directory.

In the same directory for your model, create a .py file. Cut and paste the code given by the *Teachable Machine* into this .py file. 

Modify the .py file following [here](https://github.com/FAR-Lab/TensorflowonThePi/blob/master/TeachableMachinesExample/runModelWithCamera.py) 
to make model work on pi.

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Train2.png" height="400">

2. Install Tensorflow to use with TeachableMachines models on the pi following the guide mentioned above [Tensorflow on The Pi for Teachable Machines](https://github.com/FAR-Lab/TensorflowonThePi)

Since my pi does not have python3-venv package, so I need to install it before following the tutorial.
```shell
pi@ixe00:~ $ python -m venv ~/tf_venv --system-site-packages
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/pi/tf_venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

pi@ixe00:~ $ sudo apt-get install python3-venv
```
> Source: [Tensorflow on The Pi for Teachable Machines](https://github.com/FAR-Lab/TensorflowonThePi)
> 1. Create a new virtual environment: ``python -m venv ~/tf_venv --system-site-packages``
> 1. Activate the environment: ``source ~/tf_venv/bin/activate``
> 1. Get the python wheel from GitHub: ``wget https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl``
> 1. The install the wheel with ``pip install tensorflow-2.4.0-cp37-none-linux_armv7l.whl``

Try out the tutorial:
```shell
pi@ixe00:~ $ python -m venv ~/tf_venv --system-site-packages
pi@ixe00:~ $ source ~/tf_venv/bin/activate
(tf_venv) pi@ixe00:~ $ wget https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl

```
After setup, whenever I want to enter the virtual environment that I created above, just type:
```shell
pi@ixe00:~ $ source ~/tf_venv/bin/activate
(tf_venv) pi@ixe00:~ $ 
```
Here is the video of my trained model working on pi:
[![Video of my trained teachable model working on pi](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/model_video_screenshot1.png)](https://youtu.be/G0lcI8VYL74 "Video of my trained teachable model working on pi")

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it what it is supposed to do?

-  The current interactive prototype is very accuarate in detecting husky, maybe due to color contrast with background, different angles or trainning pictures, or clear features. When the background is the same as the background that I used in training, the accuracy is also higher. 

2. When does it fail? 3. When it fails, why does it fail?

- The current interactive prototype is getting fuzzy between AirPods and laundry cards. When I show the laundry card to the camera, it was very often detected as AirPods. In human eyes, they look so different, from color to shape. But the training model may see they both white rectangles and mistaken them. 
-  Also dim environment will impair the performance of the model. 
-  I used different background when I do the training and testing. When I shoot photos for training, my closet door is closed and in the daytime. When I test the model, my closet door is open and in the nighttime. The clothing in the closet introduce a lot of noise and reduced accuracy. 

4. Based on the behavior you have seen, what other scenarios could cause problems?

- Moving object too fast. The interactive prototype is very slow with significant delay. The object need to stay static in front of camera at least for a few seconds.
- Object is too far from the camera. I noticed this issue from both training and testing period. Occupying the the entire training image with the class object would make model yield better performance during testing. In contrast, if you hold the object too far away from the camera, the features that the model can capture is lesser, and it capture the feature of the background instead. 

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

- I asked my friend to test this sytem. He's fully aware of the delay of the system at the first time he interact with it. There is a lot of misclassfication and some of them are very funny.

> My friend squeezed his face and the model is very sure he is a airpod.
> <img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/mistaken_airpod.png" height="400">


<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/husky_not_me.png" height="400">

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**Include a short video demonstrating the answers to these questions.**

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**

Below is the video of my final result:

[![Video of my final result](https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/final_video_screenshot3.png)](https://youtu.be/6yD_0l5AXYc "Video of my final result")


