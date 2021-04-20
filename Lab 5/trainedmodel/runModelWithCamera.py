import tensorflow.keras
import numpy as np
import cv2
import sys
import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
imageOLED = Image.new("1", (oled.width, oled.height))
drawOLED = ImageDraw.Draw(imageOLED)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

# while True:
#     # write the current time to the display after each scroll
#     draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
#     # text = time.strftime("%A")
#     text = time.strftime("%H:%M:%S")
#     draw.text((0, 0), text, font=font, fill=255)
#     text2 = time.strftime("%e %b %Y")
#     draw.text((0, 14), text2, font=font, fill=255)

#     oled.image(image)
#     oled.show()

#     time.sleep(1)



# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())


while(True):
    # drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    # text1 = "Do you wear"
    # drawOLED.text((0,0), text1, font = font, fill = 255)
    # text2 = "a mask?"
    # drawOLED.text((0,14), text2, font = font, fill = 255 )
    # oled.image(imageOLED)
    # oled.show()
    # time.sleep(3)


    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open('/home/pi/openCV-examples/data/test.jpg')
    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print("I think its a:",labels[np.argmax(prediction)])
    prediction_result = labels[np.argmax(prediction)]


    if prediction_result == "Me":
        drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        text1 = "Do you take"
        drawOLED.text((0,0), text1, font = font, fill = 255)
        text2 = "husky with you?"
        drawOLED.text((0,14), text2, font = font, fill = 255 )
        oled.image(imageOLED)
        oled.show()
        #time.sleep(3)
        

    if prediction_result == "husky":
        drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        text1 = "Do you have"
        drawOLED.text((0, 0), text1, font=font, fill=255)
        text2 = "airpods with you?"
        drawOLED.text((0, 14), text2, font=font, fill=255)
        oled.image(imageOLED)
        oled.show()

    if prediction_result == "airpods":
        drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        text1 = "Good! You can"
        drawOLED.text((0, 0), text1, font=font, fill=255)
        text2 = "go outside!"
        drawOLED.text((0, 14), text2, font=font, fill=255)
        oled.image(imageOLED)
        oled.show()
        #Stime.sleep(3)
                

        


        # if prediction_result == "husky":
        #     drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        #     text1 = "Do you have"
        #     drawOLED.text((0, 0), text1, font=font, fill=255)
        #     text2 = "keys with you?"
        #     drawOLED.text((0, 14), text2, font=font, fill=255)
        #     oled.image(imageOLED)
        #     oled.show()
        #     #time.sleep(3)
        #     prediction = model.predict(data)
        #     print("I think its a:",labels[np.argmax(prediction)])
        #     prediction_result = labels[np.argmax(prediction)]


        #     if prediction_result == "keys":
        #         drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        #         text1 = "Do you take"
        #         drawOLED.text((0, 0), text1, font=font, fill=255)
        #         text2 = "airpods with you?"
        #         drawOLED.text((0, 14), text2, font=font, fill=255)
        #         oled.image(imageOLED)
        #         oled.show()
        #         #time.sleep(3)

        #         if prediction_result == "airpods":
        #             drawOLED.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
        #             text1 = "Bravo! You can"
        #             drawOLED.text((0, 0), text1, font=font, fill=255)
        #             text2 = "go outside!"
        #             drawOLED.text((0, 14), text2, font=font, fill=255)
        #             oled.image(imageOLED)
        #             oled.show()
        #             #Stime.sleep(3)







    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
