# You're a wizard, Yuanhao

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Page2.png" height="1000">

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

From Erin Gong: I ABSOLUTELY LOVE your sketches!! I think the idea of having the device as a language translator is super cool and wizarding it with a dog will be fun. I’m looking forward to seeing how you would test the system with a pokemon lol
I also like the fact that the system displays an icon to indicate the mode it is currently on.

From Heidi He: wow what a sketch! Wizarding a device for talking to a dog is such a bold idea and I really love it. I am looking forward to the video with maybe the cutest user (a happy puppy or a fluffy pokemon) in it? I am curious where would you place the device in terms on the dog use case. Would it be in a box on the floor or would it be up high and unreachable for the dog?

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

I wanted to make this translator more graphical and user-friendly, so I made the language icon with Figma and Adobe Illustrator. I found translating from the dog, pokemon, and human (English but with a hidden meaning) would be fun to play with, so I made the corresponding icon for those three categories. 
This the screenshot of my working process in Figma:

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/species_icon/lab3_illustration_process.png" height="300">

Below is my final icons that's ready to be fed into the raspberry-pi:

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/species_icon/dog.png" height="200">
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/species_icon/human.png" height="200">
<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/species_icon/pikachu.png" height="200">


*Include videos or screencaptures of both the system and the controller.*

<img src="https://github.com/YuanhaoZhu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Page3.png">

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
*your answer here*

### What worked well about the controller and what didn't?

*your answer here*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

*your answer here*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

*your answer here*

