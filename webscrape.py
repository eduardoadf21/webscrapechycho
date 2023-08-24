from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import re

from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["posts2"]

my_url = "https://chycho.blogspot.com/"

request = urlopen(my_url)
homepage = request.read()
homepageSoup = BeautifulSoup(homepage, "html.parser")
dates = homepageSoup.findAll("div",{"class":"date-outer"})



def get_posts(dates, posts):
    for date in dates:
        page_posts = (date.findAll('div',{"class":"post-outer"}))
        for page_post in page_posts:
            post = {}
            post['author'] = "chycho"
            title = page_post.find('h3',{"class":"post-title entry-title"}).text
            post['title'] = title.replace('\n','')
            post['date'] = date.find('h2',{"class":"date-header"}).text
            post['body'] = page_post.find('div',{"class":"post-body entry-content"}).prettify()
            links = page_post.findAll('strong')
            for link in links:
                post['links'] = str(link.find('a',href=True))
            posts.append(post)

    print(posts)
    return posts


nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
while nextPage is not None:
    posts = []
    dates = homepageSoup.findAll("div",{"class":"date-outer"})
    get_posts(dates, posts)
    nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
    my_url = nextPage[0]['href']
    request = urlopen(my_url)
    homepage = request.read()
    homepageSoup = BeautifulSoup(homepage, "html.parser")
    collection_name.insert_many(posts)


#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(posts, f, ensure_ascii=False, indent=4)

request.close()