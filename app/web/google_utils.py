import os 
from urllib import request
import requests 
from pathlib import Path 
from bs4 import BeautifulSoup 
from IPython.display import HTML, display,clear_output


def get_images_url(query):
    urlList = []
    header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

    url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
    html = request.urlopen(request.Request(url,headers=header))
    soup = BeautifulSoup(html, 'lxml') 

    img_list = soup.find_all("img")

    for tag in img_list:
        if tag.has_attr('data-src'):
            urlList.append(tag.attrs['data-src'])

    return urlList

""" if __name__ == '__main__':
    word = 'pokemon'
    getimage = GetImage()
    urls = getimage.get_images_url(word)
    print(len(urls)) """