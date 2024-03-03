# Importing necessary modules from Selenium and other libraries
from selenium import webdriver  # Importing the main webdriver module
from selenium.webdriver.common.by import By  # Importing the 'By' class for locating elements
from selenium.webdriver.chrome.service import Service  # Importing the 'Service' class for ChromeDriver
# from webdriver_manager.chrome import ChromeDriverManager  # Importing ChromeDriverManager for automatic installation
from os import getcwd  # Importing getcwd to get the current working directory
import time  # Importing time for adding delays in the script


# Initializing colorama for colored console output

# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()  # Creating ChromeOptions to customize the behavior of the Chrome browser
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Adding an argument to simulate a fake UI for media stream
chrome_options.add_argument("--headless=new")  # Adding an argument to run Chrome in headless mode with a new session

service = Service(executable_path=".\\CHROMEDRIVER\\chromedriver.exe")

# Setting up the Chrome driver with specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Creating the URL for the website using the current working directory
website = f"{getcwd()}\\Functions\\Listen\\index.html"

# Opening the website in the Chrome browser
driver.get(website)

# Defining a function named Listen
def Listen():
    # Printing a message to indicate that the program is listening
    print( "LISTENING ... ")
    
    # Opening the website in the Chrome browser
    driver.get(website)
    
    # Clicking the 'start' button on the website to initiate voice recognition
    driver.find_element(by=By.ID, value='start').click()
    
    # Running an infinite loop to continuously listen for voice input
    while True:
        # Recording the start time to calculate the time taken for voice recognition
        start = time.time()
        
        # Extracting the recognized text from the 'output' element on the website
        text = driver.find_element(by=By.ID, value='output').text
        
        # Checking if the recognized text is not empty
        if text != "":
            # Printing the recognized text in yellow
            print( "YOU SAID : " + text)
            
            # Clicking the 'end' button on the website to stop voice recognition
            driver.find_element(by=By.ID, value='end').click()
            
            # Recording the end time and calculating the time taken for voice recognition
            end = time.time()
            print( f"TIME TAKEN TO RECOGNIZE YOUR VOICE: {round(end - start, 2)} seconds")
 
            # Returning the recognized text
            return text

# Main block of code
if __name__=="__main__":
    time.sleep(2) # To load the DOM Elements
    # Running the Listen function in an infinite loop
    while True:
        Listen()