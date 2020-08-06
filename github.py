import sys
import os
from selenium import webdriver

path = "C:\\Users\\Chinu\\Music\\pyproj"
browser = webdriver.Chrome()
browser.get('https://github.com/login')


def create():
    # folderName = str(sys.argv[1])
    # os.makedirs(path + folderName)
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")[0]
    python_button.send_keys('chinmay2003cp@gmail.com')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")[0]
    python_button.send_keys('Phanas@1234')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath("/html/body/div[4]/div/div/div/main/div/div/div/div[1]/div/div/div/ul/li[1]/div/a")[1]
    python_button.click()


if __name__ == "__main__":
    create()