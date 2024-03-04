from Interface.IF import *
import time
import eel

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
  
  time.sleep(2)
  eel.showMainWindow()
  time.sleep(2)
  eel.showWakeWindow()
  time.sleep(2)
  eel.showMainWindow()
  

#? Main Execution
if __name__ == '__main__': 
  try: eel.start("index.html", mode='chrome', size=(1500, 1200)) 
  except: print("Jarvis has encountered a fatel error. Please try later."), exit()