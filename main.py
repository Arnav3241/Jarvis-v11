from Functions.Listen.listen import *
from playsound import playsound
from Interface.IF import *
import pvporcupine
import pyaudio
import struct
# import time
import eel
import os

#? Recomendations:
# https://groq.com/

#? Some important inits
eel.init("Interface")


@eel.expose
def Initialise():
  keyboard.press_and_release("win+up")
  print("Connected 🚀🚀🚀")
  Jarvis()

#? Main function

# @eel.expose
def Jarvis():

  porcupine = None
  pa = None
  audio_stream = None
  
  print("Jarvis is now listening....")
  
  try:
    porcupine = pvporcupine.create(keywords=['jarvis'])
    pa = pyaudio.PyAudio()
    audio_stream = pa.open( rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length )

    while True:
      pcm = audio_stream.read(porcupine.frame_length)
      pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

      keyword_index = porcupine.process(pcm)
      if keyword_index >= 0:
        playsound(f"Assets\\Sounds\\Beep.mp3")
        eel.showWakeWindow() # type: ignore
        input = Listen()  
        print(input)      
        eel.showMainWindow() # type: ignore
        
        
  finally:
    if porcupine is not None: porcupine.delete()
    if audio_stream is not None: audio_stream.close()
    if pa is not None: pa.terminate()
  
  

#? Main Execution
if __name__ == '__main__': 
  try: eel.start("index.html", mode='chrome', size=(1500, 1200)) 
  except: 
    print("Jarvis has encountered a fatel error. Please try later.")
    exit()