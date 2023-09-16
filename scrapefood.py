from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import re

from pymongo_get_database import get_database
dbname = get_database()
mongo_posts = dbname["posts2"]

my_url = "https://chycho.blogspot.com/p/food.html"

request = urlopen(my_url)
foodpage = request.read()
foodpageSoup = BeautifulSoup(foodpage, "html.parser")


def get_post():
    post = {}
    food_post = foodpageSoup.find('div',{"class":"post hentry uncustomized-post-template"})
    post['author'] = "chycho"
    title = food_post.find('h3',{"class":"post-title entry-title"}).text
    post['title'] = title.replace('\n','')
    post['body'] = food_post.find('div',{"class":"post-body entry-content"}).prettify()
    post['tag'] = "food"

    mongo_posts.insert_one(post)


get_post()

request.close()