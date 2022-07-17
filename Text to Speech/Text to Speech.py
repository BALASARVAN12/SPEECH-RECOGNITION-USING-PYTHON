#Import gTTS library and “os” module in order to play the converted audio
from gtts import gTTS 
import os

#Reading the text file and store into object called text. My file name is "samplefile.txt"
file=open("samplefile.txt")
text=file.read()

#Choosing language English
language="en"

#Passing the text file into gTTS module and store into speech
obj=gTTS(text=text,lang=language,slow=False)

#Saving the converted audio in a mp3 file named called "sample.mp3"
obj.save("sample.mp3")

#Playing the mp3 file
os.system("sample.mp3")

