from selenium import webdriver  
from selenium.webdriver.common.by import By
import pyautogui
import time
driver=webdriver.Chrome(executable_path="chromedriver")
driver.get("https://vidkidz.tistory.com/107")
driver.maximize_window()
pyautogui.moveTo(x=989, y=542)
pyautogui.click()
while True:
    a=driver.find_element(By.XPATH, '//*[@id="canvas"]').get_attribute("style")
    time.sleep(1)
    if a=="cursor: auto; --waf-content-width:550px; --waf-content-height:450px;":
        pyautogui.moveTo(x=1027, y=645)
        pyautogui.click()
#     else:
#         pyautogui.moveTo(x=0, y=0)
#     print(1)
# time.sleep(5)
# a=driver.find_element(By.XPATH, '//*[@id="canvas"]').get_attribute("style")
# print(a)