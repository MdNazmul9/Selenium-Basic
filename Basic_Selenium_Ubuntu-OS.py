# pip install webdriver-manager
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  time
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# driver.get('https://www.google.com')
# driver.get('http://127.0.0.1:5500/index_OutPut.html')
url = r'file:///home/nazmul/Desktop/Selenium-Basic-Python/index.html'


for i, df in enumerate(pd.read_html(url)):
    df.to_csv('HTML_to_CSV.csv')


df = pd.read_csv('HTML_to_CSV.csv')
df = df[~df.Name.str.contains("an")]
df.to_csv(r'without_an_inName.csv', index = False)
df = pd.read_csv('without_an_inName.csv')
ls = df.Name.str.split(',')

fName = []
lName = []

for i in range(len(ls)):
    fName.append(ls[i][0])
    lName.append(ls[i][-1])

df["FastName"] = fName
df["LastName"] = lName
df = pd.DataFrame({'First_Name': df.FastName, 'Last_Name': df.LastName, 'Email': df.Email, 'Phone': df.Phone})


for i in range(len(df)):
    driver.get('file:///home/nazmul/Desktop/Selenium-Basic-Python/index_OutPut.html')
        
    fname = driver.find_element(By.ID, 'firstName')
    fname.send_keys(df.First_Name[i])

    lname = driver.find_element(By.ID, 'lastName')
    lname.send_keys(df.Last_Name[i])

    eml = driver.find_element(By.ID, 'exampleInputEmail1')
    eml.send_keys(df.Email[i])

    phn = driver.find_element(By.ID, 'phone')
    phn.send_keys(df.Phone[i])


    time.sleep(30)
    # field.sendKeys(protractor.Key.chord(protractor.Key.CONTROL, "a"));
    # field.sendKeys(protractor.Key.BACK_SPACE);
    # field.clear();
    # fname.clear()
    # lname.clear()
    # eml.clear()
    # phn.clear()

driver.close()


