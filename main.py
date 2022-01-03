from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt





html_text = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data').text
soup = BeautifulSoup(html_text,"lxml")
table = soup.find("table",{'class':"wikitable"})

df=pd.read_html(str(table))
df = pd.DataFrame(df[0])
data = df.drop(["Location","Unnamed: 4","Unnamed: 5","Unnamed: 6","Unnamed: 7"],axis = 1)
data = data.drop(data.index[217])
data = data.rename(columns={"Location.1":"Location"})
for i in range(-10,1):
    plt.scatter(data["Cases"].iloc[-i],data["Deaths"].iloc[-i])
    print(data["Location"].iloc[-i])
    plt.annotate(data["Location"].iloc[-i],(data["Cases"].iloc[-i],data["Deaths"].iloc[-i]))    



plt.show(block=True)







    