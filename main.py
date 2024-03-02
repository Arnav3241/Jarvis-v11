from Interface.IF import *
from pygame import mixer
import pvporcupine
import keyboard
import pyaudio
import struct
import eel

#? Recomendations:
# https://groq.com/

#? Some important inits
eel.init("Interface")

#? Main function

@eel.expose
def Jarvis():
  ...

#? Main Execution
if __name__ == '__main__': 
  try: eel.start("index.html") 
  except: print("Jarvis has encountered a fatel error. Please try later."), exit()