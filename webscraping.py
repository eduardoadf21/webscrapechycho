from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas

my_url = "https://chycho.blogspot.com/"

request = urlopen(my_url)

homepage = request.read()

homepageSoup = BeautifulSoup(homepage, features="lxml")

def get_posts():
    nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
    posts = homepageSoup.findAll("div",{"class":"post hentry uncustomized-post-template"})
    titles = homepageSoup.findAll("h3",{"class":"post-title entry-title"})
    dates = homepageSoup.findChild("h2",{"class":"date-header"})
    return {"nextPage":nextPage,"posts":posts,"titles":titles,"dates":dates}

c = 0
nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
while nextPage is not None and c < 10:
    c += 1
    my_url = nextPage[0]['href']
    request = urlopen(my_url)
    homepage = request.read()
    homepageSoup = BeautifulSoup(homepage, features="lxml")
    nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
    posts = get_posts()
    print(posts['titles'])
    print(nextPage[0]['href'])

request.close()