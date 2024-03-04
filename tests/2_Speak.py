from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

# env = json.loads(f"{os.getcwd()}/env.local.json")
# env = json.loads(f"{os.getcwd()}\\env.local.json")

with open(f"{os.getcwd()}\\env.local.json", 'r') as j:
  env = json.loads(j.read())

print(env)
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
website = "https://pi.ai/talk"
text = "To calculate the probability of winning more than one giveaway, we can use the binomial probability formula."

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
time.sleep(3)
driver.find_element(by=By.XPATH, value="""//*[@id="mount_0_0_QY"]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]""").click()
# //*[@id="loginbutton"]

time.sleep(200)