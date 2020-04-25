import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)

html = r.text
soup = BeautifulSoup(html,'html.parser')
print(soup.title.text)


live_data = soup.find_all('div',id='maincounter-wrap')
#print(live_data)
for i in live_data:
    print(i.text)
table_body = soup.find("tbody")
table_rows = table_body.find_all('tr')

countries = []
totalcases = []
newcases = []
totaldeaths = []
todaysdeaths = []
totalrecoveries = []
for tr in table_rows:
    td = tr.find_all('td')
    countries.append(td[0].text)
    newcases.append(td[1].text)
    totalcases.append(td[2].text)
    totaldeaths.append(td[3].text)
    todaysdeaths.append(td[4].text)
    totalrecoveries.append(td[5].text)
headers = ['Countries','New Cases','Total Cases','Total Deaths','Todays Deaths','Total Recoveries']
df=pd.DataFrame(list(zip(countries,newcases,totalcases,totaldeaths,todaysdeaths,totalrecoveries)),columns=headers)
#print(df)
df.to_csv("C:\\Users\\Admin\\Desktop\\coronadata\\data.csv")
print("*********************WRITING TO THE FILE IS DONE*****************************")

#import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\Admin\\Desktop\\coronadata\\data.csv")

data1 = data[0:10]
countries = data1["Countries"]
totalcases = data1["Total Cases"]
x = []
y = []

x = list(countries)
y = list(totalcases)

plt.plot(x,y)
plt.xlabel('countries')
plt.ylabel('totalcases')
plt.title(" PERSONS AFFECTED BY CORONA VIRUS ")
plt.xticks(rotation=60)