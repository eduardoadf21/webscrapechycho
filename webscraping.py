
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = "https://chycho.blogspot.com/"

request = urlopen(my_url)

homepage = request.read()

homepageSoup = BeautifulSoup(homepage, features="lxml")


nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
posts = homepageSoup.findAll("div",{"class":"post hentry uncustomized-post-template"})
titles = homepageSoup.findAll("h3",{"class":"post-title entry-title"})
dates = homepageSoup.findChild("h2",{"class":"date-header"})

#for link in nextPage:
print(nextPage[0]['href'])

c = 0
nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
while nextPage is not None:
    c += 1
    my_url = nextPage[0]['href']
    request = urlopen(my_url)
    homepage = request.read()
    homepageSoup = BeautifulSoup(homepage, features="lxml")
    nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
    print(nextPage[0]['href'])

request.close()