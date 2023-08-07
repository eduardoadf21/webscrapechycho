from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = "https://chycho.blogspot.com/"

request = urlopen(my_url)

homepage = request.read()

homepageSoup = BeautifulSoup(homepage, "html.parser")

#<div class ="blog-posts hfeed">
posts = homepageSoup.findAll("div",{"class":"post hentry uncustomized-post-template"})
dates = homepageSoup.findAll("h2",{"class":"date-header"})

p = 0
for post in posts:
    print(dates[p].text)
    p = p + 1
    title = post.findAll("h3",{"class":"post-title entry-title"})
    print(title[0].text) 