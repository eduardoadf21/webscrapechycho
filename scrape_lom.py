from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import re

from pymongo_get_database import get_database
dbname = get_database()
mongo_posts = dbname["posts2"]

my_url = "https://chycho.blogspot.com/2010/01/language-of-mathematics-table-of.html"

request = urlopen(my_url)
page = request.read()
pageSoup = BeautifulSoup(page, "html.parser")


def get_post():
    post = {}
    lom_post = pageSoup.find('div',{"class":"post hentry uncustomized-post-template"})
    post['author'] = "chycho"
    title = lom_post.find('h3',{"class":"post-title entry-title"}).text
    post['title'] = title.replace('\n','')
    post['body'] = lom_post.find('div',{"class":"post-body entry-content"}).prettify()
    post['tag'] = "math_language"

    mongo_posts.insert_one(post)


get_post()

request.close()