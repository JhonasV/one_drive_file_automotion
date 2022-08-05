# 2) Segundo:
#     a) Entrar a google drive / one drive
#     b) Subir un documento de su pc a la nube.



from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import config
import pyautogui
import time
import os

load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(config.driver_path, options=options)
driver.get(config.drive_url)

time.sleep(1)

pyautogui.click('./images/sign_in_img.png')

time.sleep(2)

email_input = driver.find_element(By.NAME, 'loginfmt')
email_input.send_keys(os.environ["EMAIL"])


time.sleep(2)

next_button = driver.find_element(By.CSS_SELECTOR, config.next_button_selector)
next_button.click()

time.sleep(2)

password_input = driver.find_element(By.NAME, 'passwd')
password_input.send_keys(os.environ['PASSWORD'])
time.sleep(2)

password_input.submit()

time.sleep(2)

yes_button = driver.find_element(By.CSS_SELECTOR, config.yes_button_selector)
yes_button.click()

time.sleep(2)

pyautogui.click('./images/my_content_img.png')

time.sleep(2)

pyautogui.click('./images/upload_img.png')

time.sleep(2)

pyautogui.click('./images/files_img.png')

time.sleep(2)

pyautogui.click('./images/powerpoint_img_2.png')

time.sleep(2)

pyautogui.keyDown('enter')