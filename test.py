from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

my_url = "https://chycho.blogspot.com/"
my_url2 = "https://chycho.blogspot.com/search?updated-max=2023-07-27T13:48:00-07:00&max-results=5&start=5&by-date=false"

request = urlopen(my_url2)

homepage = request.read()

homepageSoup = BeautifulSoup(homepage, "html.parser")

dates = homepageSoup.findAll("div",{"class":"date-outer"})

for date in dates:
    print(date.find('h2',{"class":"date-header"}).text)
    posts = (date.findAll('div',{"class":"post-outer"}))
    for post in posts:
        print(post.find('h3',{"class":"post-title entry-title"}).text) 
        print(post.find('div',{"class":"post-body entry-content"}).text)

