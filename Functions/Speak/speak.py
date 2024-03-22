from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

# env = json.loads(f"{os.getcwd()}/env.local.json")
# env = json.loads(f"{os.getcwd()}\\env.local.json")

def setup():
  with open(f"{os.getcwd()}\\env.local.json", 'r') as j:
    env = json.loads(j.read())

  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
  driver.set_window_position(-10000, 0)
  website = "https://pi.ai/talk"

  driver.get(website)
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/button").click()
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/button").click()
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[1]/div[1]/div[2]/button[2]").click()
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div/div/div/div[1]/div/div[1]/button[2]").click()
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"email\"]").send_keys(env["Facebook_Em"])
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"pass\"]").send_keys(env["Facebook_Pw"])
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"loginbutton\"]").click()
  time.sleep(10)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea").send_keys("Reply with \"....\"")
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/button").click()
  time.sleep(3)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button").click()

  return driver

def speak(driver, msg):
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea").send_keys(f"Reply with what is in the quotes AND NOTHING ELSE. \"{msg}\"")
  time.sleep(1)
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/button").click()
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/button").click()
  driver.find_element(by=By.XPATH, value="//*[@id=\"__next\"]/main/div/div/div[3]/div[1]/div[4]/div/button").click()

if __name__ == '__main__':
  print('Initiating setup....')
  driver = setup()
  print('Setup Complete!')
  
  while True: speak(driver, input(">>> "))
