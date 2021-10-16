# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  time
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# driver.get('https://www.google.com')
driver.get('http://127.0.0.1:5500/index_OutPut.html')

# driver.find_element(By.NAME, 'firstName').send_keys('Md Nazmul Hossain')
driver.find_element(By.ID, 'firstName').send_keys('Md Nazmul Hossain')

time.sleep(10)