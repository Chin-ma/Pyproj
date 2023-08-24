import pyscreenshot as imageGrab
import pyautogui

img = imageGrab.grab(bbox=(99,137,1689,1069))
ImageName = pyautogui.prompt()
img.save("C:/Users/chinm/OneDrive/Documents/CLGDOCS/SCRSHOTS/"+str(ImageName)+".png","PNG")