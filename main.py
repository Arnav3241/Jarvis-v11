# Project: Jarvis by Arnav Singh, Avi Sinha & Shubham Sengupta

# * Basic imports required for the code just to start it and to run the sotware completely: we will be importing them seperatey in the code.
from playsound import playsound
from Interface.IF import *
from Global.vars import *
import keyboard
import eel
import os

#? Some important inits
eel.init("Interface")

  
@eel.expose
def Jarvis():
  print("\n🚀: Connected Jarvis with GUI")
  if FULLSCREEN: keyboard.press_and_release("win+up")
  playsound(f"{os.getcwd()}\\Assets\\Sounds\\Start.mp3", False)  
  
  import time
  time.sleep(1)
  eel.ShowIntro() #type: ignore #! Removing the start intro animation not found error.
  eel.showMainWindow() #type: ignore #! Removing the start intro animation not found error.
  
  for file in os.listdir(os.getcwd() + "\\Audio"):  
    if file.endswith(".mp3") and file != "music.mp3": os.remove(os.path.join(os.getcwd() + "\\Audio", file))

  #? All the imports 
    ...
  
  
  time.sleep(6)
  
  eel.ShowMain() # type: ignore #! Removing the show main not found error.
  
  #? Main Execution
  while True:
    ...  
  

#? Main Execution
if __name__ == '__main__': 
  try: eel.start("index.html", mode='chrome', size=(1500, 1200), position=(0, 0)) 
  except: 
    print("\n💀: Jarvis has encountered a fatel error. Please try later.")
    exit()