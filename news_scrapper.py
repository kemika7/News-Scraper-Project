import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kathmandupost.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

headlines = soup.find_all("h3")

for h in headlines:
    title = h.text.strip()
    
    if title != "":
        data.append({"title": title})

df = pd.DataFrame(data)

df.to_csv("nepal_news.csv", index=False)

print("News saved successfully")