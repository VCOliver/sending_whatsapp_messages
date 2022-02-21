import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

contacts_df = pd.read_excel('Automating/demo.xlsx') # Pega informação de uma planilha de Excel

browser = webdriver.Chrome() # Abre o Chrome
browser.get("http://web.whatsapp.com/") # Acessa o Whatapp

while len(browser.find_elements_by_id("side")) < 1:
    time.sleep(1)

for i, message in enumerate(contacts_df['Message']):
    person = contacts_df.loc[i, 'Name']
    number = contacts_df.loc[i, 'Number']
    text = urllib.parse.quote(message)
    link = f"https://web.whatsapp.com/send?phone={number}&text={text}"
    browser.get(link)
    while len(browser.find_elements_by_id("side")) < 1:
        time.sleep(3)
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
