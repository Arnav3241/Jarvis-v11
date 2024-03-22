import playsound
import time
import os

def speak(Text:str, GetTimeComplexity:bool=False, Voice:str="en-US-SteffanNeural", Media:str=os.getcwd()):
  "A function that converts Text to Speech with Realestic Voices. Some Voices That you can select other than the default are: "

  st = time.time()
  command = f'edge-tts --voice "{Voice}" --text "{Text}" --write-media "{os.getcwd()}\\Audio\\{st}.mp3"'
  os.system(command)

  et = time.time() - st
  if GetTimeComplexity == True: print(f"The time complexity of speak is {et} seconds")

  try: playsound.playsound(f"{os.getcwd()}\\Audio\\{st}.mp3")
  except: print("Unsuccessful at playing Sound: Playsound error")

if __name__ == "__main__": 
  while True: speak(input(""), True)
