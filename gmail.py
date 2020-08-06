import sys
import os
from selenium import webdriver

path = "C:\\Users\\Chinu\\Music\\pyproj"
browser = webdriver.Chrome()
browser.get('https://accounts.google.com/login')


def create():
    gmail_auto = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")[0]
    gmail_auto.send_keys('chinmay2003cp@gmail.com')
    gmail_auto = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")[0]
    gmail_auto.click()
    
    # THIS WORKS BUT GOOGLE DOESN'T ALLOW ME TO SIGN IN BECAUSE IT THINKS THAT GOOGLE CHROME CONTROLLED BY AUTOMATED SOFTWARE ISN'T SAFE MEANS GOOGLE CHROME THINKS THAT GOOGLE CHROME ISN'T SAFE WOOOOW!!!!!!
   

if __name__ == "__main__":
    create()