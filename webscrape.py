from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import re

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
            #print(page_post.find('h3',{"class":"post-title entry-title"}).text) 
            post['author'] = "chycho"
            title = page_post.find('h3',{"class":"post-title entry-title"}).text
            post['title'] = title.replace('\n','')
            post['date'] = date.find('h2',{"class":"date-header"}).text
            post['body'] = page_post.find('div',{"class":"post-body entry-content"}).text
            links = page_post.findAll('strong')
            for link in links:
                post['links'] = str(link.find('a',href=True))
            posts.append(post)

    print(posts)
    return posts

nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
posts = []
while nextPage is not None:
    dates = homepageSoup.findAll("div",{"class":"date-outer"})
    get_posts(dates, posts)
    nextPage = homepageSoup.find_all("a",{"class":"blog-pager-older-link"}, href=True)
    my_url = nextPage[0]['href']
    request = urlopen(my_url)
    homepage = request.read()
    homepageSoup = BeautifulSoup(homepage, "html.parser")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)

request.close()