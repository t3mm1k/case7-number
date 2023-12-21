import json
from colorama import Fore
from dotenv.main import DotEnv
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
import time
from webdriver_manager.chrome import ChromeDriverManager


class Xd:
    def __init__(self, number):
        self.number: str = number

    def kredito(self):
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.get('https://lk.kredito24.ru/auth')
        cl = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/form/div/div/div[2]/div[1]/div/input')
        cl.click()
        cl.send_keys(self.number)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/form/button').click()
        time.sleep(10)
        if driver.current_url != 'https://lk.kredito24.ru/registration/general':
            with open('./result/kredito.txt', 'a') as f:
                f.write(self.number + '\n')
        driver.quit()

if __name__ == '__main__':
    inic = Xd('9140617112')
    inic.kredito()