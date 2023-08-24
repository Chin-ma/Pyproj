import pyautogui as auto
import time

from PIL import Image, ImageGrab
def hit(key):
    auto.keyDown(key)#this presses the key i give
def iscollide(data):
	
	for i in range(150,300):
		for k in range(500,600):
			if data[i,k] < 100:
				return True
	return False



if __name__ == '__main__':#specifes the code to be executed only when the file is run as a script and not module
    while True:
	    time.sleep(3)
	    img = ImageGrab.grab().convert('L')#this takes a screenshot and coverts it into black and white
	    img_data = img.load()#gets image data
	    if iscollide(img_data):
		    hit("up")		
