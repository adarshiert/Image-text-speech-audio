import pytesseract
import pyttsx3
from PIL import Image

#...............This is Adarsh Tiwari.............

img=Image.open("ironman.jpg") #this code open image in given path
text=pytesseract.image_to_string(img) #this code convert image to string

#this code save string to text from and print them
file=open("ironman.txt", "w")
file.write(text)
print(text)
file.close()

#...................this code produce speech from given content in image

engine=pyttsx3.init()
print("loding...........")
engine.say("Now i am converting image to text "+text+"ThankYou")
engine.save_to_file(text,"ironman3000.mp3")
engine.runAndWait()

#.................ThankYou for Breaking My Heart..................
