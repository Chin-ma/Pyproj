import sys
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search = pyautogui.prompt('What do you want to search?')

browser = webdriver.Chrome()
browser.get("https://www.google.in")

def create():
    # search = input("firebase")
    python_button = browser.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')[0]
    python_button.send_keys(search, Keys.ENTER)
    # python_button = browser.find_elements_by_xpath('//*[@id="tads"]/div[1]/div/div/div[1]/a/div[1]/span')[0]
    # python_button.click()
    # python_button = browser.find_elements_by_xpath('//*[@id="firebase-helps-mobile-and-web-app-teams-succeed"]/div[2]/div[1]/div/a[2]')[0]
    # python_button.click()


if __name__ == "__main__":
    create()

for i in range(10):
    pyautogui.moveTo(230, 325)
    pyautogui.click()

# for i in range(10):
#     pyautogui.moveTo(240, 325)
#     pyautogui.scroll(-100)