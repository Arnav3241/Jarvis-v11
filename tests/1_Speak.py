# The Speak function
#? TTS MP3 (ttsmp3.com/ai) - Text to Speech MP3 Reverse Enginering

from requests import get
from pygame import mixer
import requests
import asyncio
import shutil
import json
import time
import os

mixer.init()

url = "https://ttsmp3.com/makemp3_ai.php"
headers = {
  'authority': 'ttsmp3.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded',
  'origin': 'https://ttsmp3.com',
  'referer': 'https://ttsmp3.com/ai',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin'
}

# For removing all the audio files from the Audio folder so that it doesn't become too large
def removeFilesfromFolder(folder:str):
  for filename in os.listdir(folder):
    if filename == "music.mp3": return
    file_path = os.path.join(folder, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
    except Exception as e:
      print('Failed to delete %s. Reason: %s' % (file_path, e))

def PlayURL(URL: str):
  tss = time.time()
  x = get(URL).content
  name = f'{os.getcwd()}\Audio\{int(time.time())}.mp3'
  # removeFilesfromFolder(f'{os.getcwd()}\Audio')
  with open(name,'wb') as file:
    file.write(x)
  print(f"Time taken to download the file: {time.time() - tss} seconds")
  tts = time.time()
  mixer.music.load(name)
  mixer.music.play()
  print(f"Time taken to play the file: {time.time() - tts} seconds")

async def Speak(*args, Model: str = "echo", Speed: float = 0.95):
  ts = time.time()
  message = " ".join(args)
  payload = f'msg={message}&lang={Model}&speed={Speed}&source=ttsmp3'
  response = json.loads(requests.request("POST", url, headers=headers, data=payload).text)
  print(f"Got the Response from TTSMP3.com in {time.time() - ts} seconds")
  
  PlayURL(response["URL"])
  print(f"Time taken: {time.time() - ts} seconds")

if __name__ == "__main__":
  asyncio.run(Speak("""
Self-management, which is also referred to as ‘selfcontrol’ or ‘self-regulation’, is the ability to regulate
one’s emotions, thoughts, and behaviour effectively
in different situations. This includes motivating
oneself, and setting and working towards personal and
academic goals. Students with strong self-management
skills are able to do different activities effectively,
including managing their timelines, focusing on their
tasks, cooperating with others in school and at home
and perform better in their studies. It help
"""))
  time.sleep(20)
  # asyncio.run(Speak("Hello world"))
  # time.sleep(1)
  # asyncio.run(Speak("Hello world"))
  # time.sleep(1)
  # asyncio.run(Speak("The above code will play the music file indefinitely (though you can call it to stop). The -1 signals PyGame to just play forever, but, if you put, say, a 5 in there, then the music would play once and 5 more times."))
  # time.sleep(20)
