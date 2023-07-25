import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

s=Service('C:/Users/buzma/Downloads/chromedriver_win64/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru")
time.sleep(1)
driver.set_window_size(1366,768)
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[1]/input").clear()
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("demo")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[2]/input").clear()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[2]/input").send_keys("demo")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()
time.sleep(1)
driver.find_element(By.ID, "otp-code").clear()
driver.find_element(By.ID, "otp-code").send_keys("0000")
driver.find_element(By.ID, "otp-code").click()
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(10)
driver.find_element(By.ID, "logout-button").click()
time.sleep(10)
driver.get("https://idemo.bspb.ru")
time.sleep(5)
driver.quit()
