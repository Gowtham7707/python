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


links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:10]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
# print(link)    
    


images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
# print(image)

df=pandas.DataFrame()
# print(df)     

data={'Names':name,
      'Ratings':rating,
      'features':feature,
      'links':link,
      'images':image
      }
# print(data)

df=pandas.DataFrame(data)
# print(df)
df.to_csv("mobiles_data.csv")