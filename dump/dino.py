from selenium import webdriver
import pyautogui as auto
import pyttsx3 as pyspeaker
import keyboard
import time


class beebom_automater:
    web = webdriver.Chrome('chromedriver.exe')
    web.get('https://beebom.com/category/news/')
    def get_news(self, n):
        time.sleep(3)
        news_butts = beebom_automater.web.find_elements_by_class_name('item-details')
        anchor_tags = [ele.find_element_by_tag_name("a") for ele in news_butts]
        anchor_tags[n].click()
        time.sleep(1)
        title = beebom_automater.web.find_element_by_class_name('entry-title').text
        news = beebom_automater.web.find_element_by_class_name("td-post-content").text
        news = title +'. ' + news
        beebom_automater.web.quit()
        return news

    def speak_news(self, x):
        latest_news = self.get_news(x)
        latest_news = latest_news.split('.')
        speaker = pyspeaker.init()
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
        for sent in latest_news:
            speaker.say(sent)
            speaker.runAndWait()
            time.sleep(0.5)
            if keyboard.is_pressed('esc'):
                break
            elif keyboard.is_pressed('right'):
                self.get_news(x+1)

bot = beebom_automater()
bot.speak_news(1)

