import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  time
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# import pandas as pd
sales_tax = pd.read_csv("USA_SALES_TAX.csv")
print(sales_tax.shape)

for i in range(len(sales_tax)):
    print(sales_tax.StateName[i],sales_tax.City[i],sales_tax.Salestaxrate[i],sales_tax.AlachuaCounty[i])
    driver.get('http://127.0.0.1:5500/index_OutPut.html')
        
    fname = driver.find_element(By.ID, 'firstName')
    fname.send_keys(sales_tax.StateName[i])

    lname = driver.find_element(By.ID, 'lastName')
    lname.send_keys(sales_tax.City[i])

    eml = driver.find_element(By.ID, 'exampleInputEmail1')
    eml.send_keys(sales_tax.Salestaxrate[i])

    phn = driver.find_element(By.ID, 'phone')
    phn.send_keys(sales_tax.AlachuaCounty[i])


    time.sleep(0.1)
    # field.sendKeys(protractor.Key.chord(protractor.Key.CONTROL, "a"));
    # field.sendKeys(protractor.Key.BACK_SPACE);
    # field.clear();
    # fname.clear()
    # lname.clear()
    # eml.clear()
    # phn.clear()

driver.close()

