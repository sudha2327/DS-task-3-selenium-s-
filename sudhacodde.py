
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.common.keys import Keys
import warnings
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pyautogui
import os


warnings.filterwarnings("ignore")
HEADERS = ({'User-Agent':
                'Chrome/44.0.2403.157 Safari/537.36',
                                'Accept-Language': 'en-US, en;q=0.5'})

comments = ["Dear Customer. Thanks for your feedback."]
ratt=[]
products=[]                     #List to store the name of the product
real_prices=[] 
modified_price=[]               #List to store price of the product
ratings=[]  
url=[]  
img_url=[]
rev=[]
url=[]
l=0
cus=[]
url4=input("enter the URL:")
urll=url4+"/products"
cmt=[]

cwd=os.getcwd()
#S:/coding/DS intern/Task 1/task2/chromedriver.exe
h=os.path.join(cwd,'chromedriver.exe')
browser= webdriver.Chrome(h)
m=int(input("enter how many page wants to scrape:"))
for i in range(1,m+1):
    
    url1=urll+"?page={}".format(i)
    webpage = requests.get(url1, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    print("scrapping url page:",url1)
    for data in soup.find_all('div',attrs={"class":'col-sm-3 col-xs-6'}):
        li=data.find('a',class_="product-link")
        names=data.find('span',class_='product-title')
        #print("real price is :",r.find_next('span').text
        #print(li.get('href'))
        li=url4+str(li.get('href'))
        #print(li)
        browser.get(li)
       
        ko=[]
        time.sleep(5)
        re=browser.find_elements_by_xpath("//div[@class='content-review']")

        for r in re:
            ko.append(r.text)
        while('' in ko):
            ko.remove('')
        
        kd=str(ko)[1:-1]

        #print("text meassage==>",kd)
        if len(kd)>0:
            cmt.append(kd)
        else:
            cmt.append("not yet filled...")
        #customer_name=browser.find_elements_by_xpath("//span[@class='y-label yotpo-user-name yotpo-font-bold pull-left']")
        customer_name=browser.find_elements_by_xpath("//span[@class='y-label yotpo-user-name yotpo-font-bold pull-left']")
        # time.sleep(5)
        ko1=[]
        url.append(li)
        products.append(names.string)
        for r in customer_name:
            ko1.append(r.text)
        while('' in ko1):
            ko1.remove('')
        kd1=str(ko1)[1:-1]

        #print("text meassage==>",kd)
        if len(kd1)>0:
            cus.append(kd1)
        else:
            cus.append("not yet filled...")
        ko1.clear()
        
        if len(customer_name)<3:
            continue
        else:
            
            reviewButton=browser.find_element_by_xpath("//span[@class='yotpo-icon-button-text']")
            # time.sleep(5)
            browser.execute_script("arguments[0].click();", reviewButton)
            # time.sleep(5)
            reviewButton=browser.find_element_by_xpath("//span[@class='yotpo-icon-button-text']")
            # time.sleep(5)
            browser.execute_script("arguments[0].click();", reviewButton)
            # time.sleep(5)
            titleField = browser.find_element_by_xpath("//input[@name='review_title']")
            # time.sleep(5)
            reviewField = browser.find_element_by_xpath("//textarea[@name='review_content']")
            userIDField = browser.find_element_by_xpath("//input[@name='display_name']")
            emailIDField = browser.find_element_by_xpath("//input[@name='email']")
            time.sleep(1)
            
            titleField.send_keys('Thank You!')
            # time.sleep(3)
            reviewField.send_keys('Dear Customer, Thank you for your valuable feedback!')
            # time.sleep(5)
            userIDField.send_keys('SudhagarSvS')
            # time.sleep(5)
            emailIDField.send_keys('sudhagarv.yoshops@gmail.com')
            # time.sleep(5)
            starRating = browser.find_element_by_xpath("//span[@aria-label='score 5']")
            browser.execute_script("arguments[0].click();", starRating)
            
            postButton=browser.find_element_by_xpath("//input[@class='yotpo-default-button primary-color-btn yotpo-submit']")
            browser.execute_script("arguments[0].click();", postButton)
          

df=pd.DataFrame({'Product_name':products,'Product_URL':url,'Customer name':cus,'Review cmt':cmt})    
df.to_excel('outputsudha1.xlsx',index=False,encoding='utf-8')
print("finshed....")





