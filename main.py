# Project: Jarvis by Arnav Singh & Avi Sinha

# * Basic imports required for the code just to start it and to run the sotware completely: we will be importing them seperatey in the code.
from playsound import playsound
from Interface.IF import *
from Global.vars import *
import keyboard
import eel
import os

#? Some important inits
eel.init("Interface")

#? Important Variables
porcupine = None
pa = None
audio_stream = None

  
@eel.expose
def Jarvis():
  print("\n🚀: Connected Jarvis with GUI")
  if FULLSCREEN: keyboard.press_and_release("win+up")
  # playsound(f"{os.getcwd()}\\Assets\\Sounds\\Start.mp3", False)  
  
  import time
  eel.ShowIntro() #type: ignore #! Removing the start intro animation not found error.
  eel.showMainWindow() #type: ignore #! Removing the start intro animation not found error.
  
  for file in os.listdir(os.getcwd() + "\\Audio"):  
    if file.endswith(".mp3") and file != "music.mp3": os.remove(os.path.join(os.getcwd() + "\\Audio", file))

  #? All the imports
  
  # Import for Wake Word Detection 
  import pvporcupine
  import struct
  import pyaudio
  
  # time.sleep(2)
  
  eel.ShowMain() # type: ignore #! Removing the show main not found error.
  
  #? Main Execution
  while True:
    try:
      porcupine = pvporcupine.create(keywords=['jarvis'])
      pa = pyaudio.PyAudio()
      audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
      )
      
      while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
          playsound(f"{os.getcwd()}\\Assets\\Sounds\\Beep.mp3", True)
          eel.showWakeWindow() # type: ignore #! Removing the show wake window not found error.
          eel.Recognition() # type: ignore #! Removing the recognition not found error.
          print('Keyword detected')
      
    finally:
      if porcupine is not None:
          porcupine.delete()
      
      if audio_stream is not None:
          audio_stream.close()
      
      if pa is not None:
          pa.terminate()
    

#? Main Execution
if __name__ == '__main__': 
  try: eel.start("index.html", mode='chrome', size=(1500, 1200), position=(0, 0)) 
  except: 
    print("\n💀: Jarvis has encountered a fatel error. Please try later.")
    exit()