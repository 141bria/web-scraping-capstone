from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.timeanddate.com/weather/glossary.html")
gwords = driver.find_element(By.CSS_SELECTOR,'["gwords"]')
definitions = gwords.find_elements(By.CSS_SELECTOR,'[id="A"]')
for word in definitions:
    one_word = driver.find_element(By.TAG_NAME,"dl")
    weather_words ={"Words":word.text,"Definitions":definitions}
weather = []
