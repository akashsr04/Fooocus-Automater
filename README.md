# Fooocus Automater

Fooocus Automater.py is used to automate the creation of AI generated images using Fooocus and upload them to your social media simultaneously all in one click.

## Fooocus Repo
Heres the link to [Fooocus](https://github.com/lllyasviel/Fooocus) repo.

### Dev Notes

Since the API system of Fooocus is extremely difficult to comprehend I have made this script which will allow me to automatically generate and upload them in my instagram account.
This script *does not use any API calls*. It simply uses webbrowser interaction with Selenium and pyautogui modules to automatically generate and upload them.

+ This script depends on the screen orientation of your system so make sure that you change the x and y coordinates wherever  required according to your screen resolution.

+ No changes have to be made for screen resolution of 1920 x 1080 and no changes in time.sleep() for GPU Nvidia RTX 3050 and above.

+ You can either enter prompt for you Fooocus server manually or use Fooocus/config.txt to set a default prompt for image generation.

+ Change the username and password fields to the username and password of your own Instagram account and enter the description/caption for the post in the 'Tags' (tags) field.

+ Run the Fooocus local server 127.0.0.1 by pressing run.bat and AFTER the App has successfully started, you can run this script and MAKE SURE to go to the webbrowser running 127.0.0.1 .

+ After generating the pic, this script will use Selenium and pyautogui to start the driver for your preferred webbrowser and start upload to Instagram.

+ time.sleep(value) - value can be increased if your GPU is taking more time and vice versa.

+ Fooocus generated images should be in .jpeg or .png format. The default format can be changed in Fooocus/config.txt.

+ The entire program is divided into two parts : 1. Fooocus Automatic Image Generator 2. AutoUploader to generate Images automatically and Upload automatically simultaneously.

+ I am reiterating that the time.sleep() , 350 value in the part 1 and screen resolution have to be manually set/tweaked if your screen orientation is not equal to 1920 x 1080 and if your GPU is below RTX 3050. 

+ If you are using chrome set webdriver.Chrome or connect the webdriver to the path of your driver.

## Requirements
Basic requirements of Fooocus

pip install pyautogui

pip install selenium
