import pyautogui as auto
from PIL import Image, ImageColor
import time
import keyboard
from selenium import webdriver
auto.FAILSAFE = True

def game_starter():
    chrome = webdriver.Chrome('chromedriver.exe')
    chrome.get('chrome://dino')
    time.sleep(2)
    auto.press('space')
    time.sleep(1)
    auto.hotkey('win', 'up')
    time.sleep(1)
    auto.press('space')



def jump_on_cactus_and_restart():
    # a=input()
    # time.sleep(2)
    # sshot = auto.screenshot()
    for j in range(500, 530):
        for i in range(210, 340):
            if auto.pixelMatchesColor(i,j, (83, 83, 83)) or auto.pixelMatchesColor(486,357,(83,83,83)):
                auto.press('up')
    #             sshot.putpixel((i,j),(0,0,0,255))
    # sshot.show()
    
def duck_dragon():
    # a = input()
    # time.sleep(2)
    # x,y = auto.position()
    # print(x,y)
    if auto.pixelMatchesColor(200,451, (83,83,83)):
        for i in range(3):
            auto.press('down')

game_starter()
while True:
    jump_on_cactus_and_restart()
    duck_dragon()
