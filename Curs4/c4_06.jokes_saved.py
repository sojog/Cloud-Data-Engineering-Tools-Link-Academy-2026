from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://icanhazdadjoke.com/"

browser = webdriver.Chrome()
browser.get(URL)

browser.find_elements(By.CLASS_NAME, "fc-button-label")[0].click()


joke_list = []

new_joke = browser.find_elements(By.CLASS_NAME, "subtitle")[1].text

joke_list.append(new_joke)

for i in range(2):
    browser.refresh()
    time.sleep(1)
    new_joke = browser.find_elements(By.CLASS_NAME, "subtitle")[1].text
    joke_list.append(new_joke)


print("Joke list:", joke_list)


