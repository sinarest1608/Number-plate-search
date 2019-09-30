from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import pandas as pd


class Bot:
    def __init__(self, number):
        self.number = number
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://rtovehicle.info/index.php')
        time.sleep(2)
        
        search = bot.find_element_by_id('vehiclenum')
        search.send_keys(self.number)
       
        clicker = bot.find_element_by_id('searchB')
        clicker.click()
     
        time.sleep(3)
        bot.execute_script("window.scrollTo(0, 400)")
        bot.save_screenshot("rto.png")
        
    def img_text(self):
        pytesseract.pytesseract.tesseract_cmd = r"tesseract"    
        image = Image.open('rto.png')
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        text = []
        text.append(image_to_text)
        print(text)    

q = input("Enter vehicle number: ")
quantin = Bot(q)
quantin.login()
key = Keys()
quantin.img_text()
