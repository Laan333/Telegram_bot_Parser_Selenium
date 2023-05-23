from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
name = None
href = None
def create_new_data():
    global name, href
    browser = webdriver.Chrome()
    url = 'https://store.epicgames.com/ru/'
    browser.get(url)
    time.sleep(5)
    all_elem = browser.find_element(By.CLASS_NAME, "css-1myhtyb")
    data = all_elem.find_elements(By.CLASS_NAME, "css-1b2k567")
    hrefs_links = all_elem.find_elements(By.CLASS_NAME,"css-g3jcms")

    name = [data[i].get_attribute("alt") for i in range(len(data))]  # Generator names
    src = [data[i].get_attribute("src") for i in range(len(data))] #generator imgs
    href = [hrefs_links[i].get_attribute("href") for i in range(len(data))] #generator links

    def save_photo(photo_list: list):
        for i in range(len(photo_list)):
            get_req = requests.get(photo_list[i])
            with open(f"imgs/image{i}.png", "wb") as img_file:
                img_file.write(get_req.content)

    save_photo(src)
