from bs4 import BeautifulSoup
import requests

# Read a HTML File
becode_filename = "./assets/becode.html"
file = open(becode_filename, "r")
html_doc = file.read()
file.close()

# In my file (becode.org) by looking at this html script,
# we can see that the main title is arranged in the `h1` tag
soup = BeautifulSoup(html_doc, "lxml")

# for tag in soup.find_all("h2"):
    # We only retrieve the content ==> .text
    # print(tag.text)

# Url of website
# url = "https://www.becode.org/about/"
# Send Get Request
#r = requests.get(url)
# Display URL and status code
# print(url, r.status_code)
# Get HTML Content
# soup = BeautifulSoup(r.content, "lxml")

url = "http://www.allocine.fr/"
r = requests.get(url)
print(url, r.status_code)
soup = BeautifulSoup(r.content, "lxml")

#for a in soup.find_all("a"):
    #print(a.text)


# In addition to the tag `a`, which is easily identifiable, we notice some additional
# information such as the value of the class variable of these identical tags.
#for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
   #print(elem)

#for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    #print(elem.get("href"))

#for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    #print(elem.get("title"))

links = []
for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    links.append(elem.get("href"))

movie_links = ["http://www.allocine.fr" + elem for elem in links if "film" in elem]

for url in movie_links:
    r = requests.get(url)
    #print(url, r.status_code)
    soup = BeautifulSoup(r.content, "lxml")

    for elem in soup.find_all("div", attrs={"class": "titlebar-title titlebar-title-xl"}):
        # Just like that
        print(elem.text)

    for elem in soup.find_all("p", attrs={"class": "bo-p"}):
        # Just like that
        print(elem.text)

