# The Speak function
#? TTS MP3 (ttsmp3.com/ai) - Text to Speech MP3 Reverse Enginering
import asyncio
import requests
import json
from requests import get
from pygame import mixer
import time
mixer.init()

url = "https://ttsmp3.com/makemp3_ai.php"
headers = {'authority': 'ttsmp3.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','cookie': '_ga=GA1.1.22434835.1709110974; __gads=ID=84df532ef6f9f9aa:T=1709110975:RT=1709278664:S=ALNI_MYrGplVjocOYCBarOSPP4dRXP-u0g; __gpi=UID=00000d1bf2425851:T=1709110975:RT=1709278664:S=ALNI_MZssPqM4cfJm5redhQLS-AHHQuEVA; __eoi=ID=1d52f87eb5ae5b25:T=1709110975:RT=1709278664:S=AA-Afjbi3-sm4wrMVQe79V4xxLqs; FCNEC=%5B%5B%22AKsRol-kl-4UfiwlNkLpoBKwEDyhOfZ6vsk5KLw3A3-FgNTeP_-c9Jf-lFJChtr1RPoGChwUBTtro4BFq89luWqqTdsuxI3cR2yngvEuUKa9ExQI2qtYoyJZEO1wxZfVV66kxFAX1fBkgVIHwXALp8z91LWR6-mOuw%3D%3D%22%5D%2Cnull%2C%5B%5B2%2C%22%5Bnull%2C%5Bnull%2C3%2C%5B1709278665%2C664080000%5D%5D%5D%22%5D%5D%5D; _ga_H0XGBVF70F=GS1.1.1709278663.4.1.1709278893.55.0.2041171874','origin': 'https://ttsmp3.com','referer': 'https://ttsmp3.com/ai','sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

Sample = {'Error': 0, 'Speaker': 'onyx', 'Cached': 1, 'Text': 'Hi', 'tasktype': 'direct', 'URL': 'https://ttsmp3.com/created_mp3_ai/5bff6c1ea54bc6ded04166231e218c6f.mp3', 'MP3': '5bff6c1ea54bc6ded04166231e218c6f.mp3', 'UsedChars': 0}

def PlayURL(URL: str):
  x = get(URL).content
  name = f'.\\Music\music{int(time.time())}.mp3'
  with open(name,'wb') as file:
    file.write(x)
  mixer.music.load(name)
  mixer.music.play()

async def Speak(*args, Model: str = "echo", Speed: float = 0.80):
  message = " ".join(args)
  print("Making the URL")
  payload = f'msg={message}&lang={Model}&speed={Speed}&source=ttsmp3'
  response = json.loads(requests.request("POST", url, headers=headers, data=payload).text)
  
  print(response["URL"])
  PlayURL(response["URL"])

while True: asyncio.run(Speak(input(">>>")))