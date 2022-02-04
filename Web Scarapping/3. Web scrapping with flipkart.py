import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

products=[]
URL = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
desc = soup.find_all('div' , class_='_4rR01T')
for i in range(len(desc)):
    products.append(desc[i].text)
processors=[]
ram=[]
os=[]
storage=[]
inches=[]
warranty=[]
commonclass = soup.find_all('li' , class_='rgWa7D')
for i in range(0,len(commonclass)):
    p=commonclass[i].text # Extracting the text from the tags
    if("Core" in p): 
        processors.append(p)
    elif("RAM" in p): 
        ram.append(p)
    elif("HDD" in p or "SSD" in p):
        storage.append(p)
    elif("Operating" in p):
        os.append(p)
    elif("Display" in p):
        inches.append(p)
    elif("Warranty" in p):
        warranty.append(p)
laptop = []
laptop.append(products)
laptop.append(processors)
laptop.append(ram)
laptop.append(storage)
laptop.append(os)
laptop.append(inches)
laptop.append(warranty)

print(laptop)
