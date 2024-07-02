'''
DEV DOCS
--------
*Developer : github/akashsr04

*Since Fooocus uses a very complex API i.e. gradio, I have made this script so that a user can use Fooocus to make AI generated pics as well as upload the generated pics in instagram in a single click.


PROCEDURE TO USE THIS SCRIPT :
----------------------------
*This script depends on the screen orientation of your system so make sure that you change the x and y coordinates wherever  required.
*No changes have to be made for screen resolution of 1920 x 1080 and no changes in time.sleep() for GPU Nvidia RTX 3050 and above
*You can either enter prompt for you Fooocus server manually or use Fooocus/config.txt to set a default prompt for image generation.
*Change the username and password fields to the username and password of your own Instagram account and enter the description/caption for the post in the 'Tags' (tags) field.
*Run the Fooocus local server 127.0.0.1 by pressing run.bat and AFTER the App has successfully started, you can run this script and MAKE SURE to go to the webbrowser running 127.0.0.1 .
*After generating the pic, this script will use Selenium and pyautogui to start the driver for your preferred webbrowser and start upload to Instagram.
*time.sleep(value) - value can be increased if your GPU is taking more time and vice versa
*Fooocus generated images should be in .jpeg or .png format. The default format can be changed in Fooocus/config.txt
*The entire program is divided into two parts : 1. Fooocus Automatic Image Generator 2. AutoUploader to generate Images automatically and Upload automatically simultaneously.
*I am reiterating that the time.sleep() , 350 value in the part 1 and screen resolution have to be manually set/tweaked if your screen orientation is not equal to 1920 x 1080 and if your GPU is below RTX 3050. 
*If you are using chrome set webdriver.Chrome or connect the webdriver to the path of your driver.
'''

import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Fooocus Automatic Image Generator - Auto Generate AI Images using Fooocus
#-------------------------------------------------------------------------
#click run.bat to start image generation before running this script
sec=30
for i in range(sec,0,-1):
    print(f'{i} seconds left for operation to begin. Please switch to browser window')
    time.sleep(1)
 
button_x, button_y = 1700,800           
button_x_min, button_y_min = 1750,10    
pyautogui.click(button_x, button_y)
print("Generate Clicked")
time.sleep(5)                          
pyautogui.click(button_x_min, button_y_min)
print("Minimized Clicked")
print('Waiting for image generation')
for i in range(350,0,-1):                           #350 - Time taken for Fooocus to generate images. Run it atleast once and you will get an idea about how much time it takes for Fooocus to run basedon your required settings.
    print(f'{i} seconds left for Image Generation')
    time.sleep(1)
print("Image Generation Completed (Most probably)")

#AutoUploader - Upload the generated images to your instagram account automatically
#----------------------------------------------------------------------------------

username = 'username'
password = 'password'
tags = r'caption for the post'

time.sleep(10)
driver = webdriver.Firefox() 
driver.maximize_window()
driver.get('https://www.instagram.com/')

current_date = str(datetime.now().date())
dir_outputs = r'enter your C:\\...\Fooocus\outputs folder path here'
dir_outputs += '\\'+current_date
print(dir_outputs)
time.sleep(10) 

driver.find_element(By.NAME,'username').send_keys(username)
driver.find_element(By.NAME,'password').send_keys(password)
print("Username and password entered .. ")
login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()
time.sleep(10) 
print("Login Attempted")

button_nn_x , button_nn_y = 1085,630
pyautogui.click(button_nn_x,button_nn_y)
time.sleep(5)
button_x_notnow, button_y_notnow = 1000,750
pyautogui.click(button_x_notnow,button_y_notnow)
print("Notifications rejected")

button_x_create, button_y_create = 50,700
pyautogui.click(button_x_create,button_y_create)
time.sleep(5)
print('Post Button Click Attempted')

button_x_select , button_y_select = 900,680
pyautogui.click(button_x_select,button_y_select)
time.sleep(3)
print('Selecting files for posting')
pyautogui.typewrite(dir_outputs)
pyautogui.press('enter')
time.sleep(1)

files = os.listdir(dir_outputs)
selected_files = [file for file in files if ((file.endswith('.jpeg'))or(file.endswith('.png')))]
selected_files = sorted(selected_files,reverse=True)
files_to_be_posted = ''
for i in range(0,len(selected_files)):
    files_to_be_posted+=selected_files[i]
files_to_be_posted=files_to_be_posted.replace('jpeg','')
files_to_be_posted=files_to_be_posted.replace('png','')
files_to_be_posted=files_to_be_posted.replace('.',' ')
files_to_be_posted=' '+files_to_be_posted
files_to_be_posted=files_to_be_posted.replace(' ','""')
files_to_be_posted=files_to_be_posted.replace('""','" "')
files_to_be_posted=files_to_be_posted[2:len(files_to_be_posted)-1]

pyautogui.typewrite(files_to_be_posted)
time.sleep(5)
pyautogui.press('enter')
print('Filenames to be posted entered in field')

time.sleep(10)
button_x_next , button_y_next = 1245,240
pyautogui.click(button_x_next,button_y_next)
time.sleep(10)
print('First next pressed')

button_x_next2 , button_y_next2 = 1450,240
pyautogui.click(button_x_next2,button_y_next2)
print('Second next pressed')
time.sleep(10)

for i in range(5,0,-1):
    print(f'{i} seconds remaining to write caption')
    time.sleep(1)
    
button_x_desc , button_y_desc = 1450,400
pyautogui.click(button_x_desc,button_y_desc)
time.sleep(10)

pyautogui.typewrite(tags)
print('Tags written')
time.sleep(10)

button_x_share , button_y_share = 1450,240
pyautogui.click(button_x_share,button_y_share)
time.sleep(10)

print('Posting')
for i in range(0,15):
    print(f'{i} seconds elapsed')
    time.sleep(1)

button_x_close , button_y_close = 1880,135
pyautogui.click(button_x_close,button_y_close)
print("Post uploaded successfully")
time.sleep(2)
driver.quit()





