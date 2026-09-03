import csv
import pandas as pd
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.timeanddate.com/weather/glossary.html")
gwords = driver.find_element(By.CSS_SELECTOR,"#gwords")
definitions = gwords.find_elements(By.CSS_SELECTOR,"dd")
words= gwords.find_elements(By.TAG_NAME,"dt")
with open("weather_words.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Word","Definition"])
    for word, definition in zip(words,definitions):
        writer.writerow([word.text,definition.text])

driver.quit()
