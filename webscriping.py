# import section
# ---------------------------------------------------
import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DAPPLE", verify=False)
# print(response)

soup=BeautifulSoup(response.content)
# print(soup)

names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)    


ratings=soup.find_all('span',class_='_2_R_DZ')
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(d)
# print(rating)    


features=soup.find_all('div',class_='fMghEO')
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
# print(feature)    

    
    
    