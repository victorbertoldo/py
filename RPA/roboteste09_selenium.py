from selenium.webdriver import Chrome
from pyautogui import sleep


browser = Chrome()
browser.get('http://www.pudim.com.br/')

sleep(2)
 
browser.quit()