import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "http://www.allocine.fr/"
r = requests.get(url)
print(url, r.status_code)
soup = BeautifulSoup(r.content, "lxml")

links = []
titles = []
synopsis = []

for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    links.append(elem.get("href"))

movie_href = ["http://www.allocine.fr" + elem for elem in links if "film" in elem]

for url in movie_href:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    for elem in soup.find_all("div", attrs={"class": "titlebar-title titlebar-title-xl"}):
        # Just like that
       titles.append(elem.text)

    for elem in soup.find_all("p", attrs={"class": "bo-p"}):
        # Just like that
        synopsis.append(elem.text)

# Prepare to import datas into a CSV File
target_length = min(len(titles), len(synopsis), len(movie_href))  # Truncate to shortest length

# Fix potential length issue for the CSV
titles = titles[:target_length]
synopsis = synopsis[:target_length]
movie_href = movie_href[:target_length]

# Prepare and write into a CSV File
df = pd.DataFrame({"Title": titles})
df["Synopsis"] = synopsis
df["Links"] = movie_href

df.to_csv("./assets/allo_cine.csv", index=False)
