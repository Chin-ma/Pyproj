from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Firefox(firefox_binary=binary)
