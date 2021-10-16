#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"


options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("http://127.0.0.1:5500/index_OutPut.html")

driver.find_element(By.ID, 'firstName').send_keys('Md Nazmul Hossain')

time.sleep(10)
# fname = driver.find_element_by_id("firstName")
# fname.send_keys("Nazmul")
