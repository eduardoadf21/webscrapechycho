
from urllib.request import urlopen
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver

my_url = "https://chycho.blogspot.com/"

request = urlopen(my_url)

homepage = request.read()

homepageSoup = BeautifulSoup(homepage, features="lxml")

posts = homepageSoup.findAll("div",{"class":"post hentry uncustomized-post-template"})

print(len(posts))
print(posts)

request.close()