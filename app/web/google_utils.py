import os 
from urllib import request
import requests 
from pathlib import Path 
from bs4 import BeautifulSoup 
from IPython.display import HTML, display,clear_output

header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

def get_images_url(query):
    urlList = []

    url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
    html = request.urlopen(request.Request(url,headers=header))
    soup = BeautifulSoup(html, 'lxml') 

    img_list = soup.find_all("img")

    for tag in img_list:
        if tag.has_attr('data-src'):
            urlList.append(tag.attrs['data-src'])
            if len(urlList) == 15:
                break

    return urlList

def get_sentence(word):
    sentence_list = []
    url = "https://lengusa.com/sentence-examples/" + word
    html = request.urlopen(request.Request(url, headers=header))
    soup = BeautifulSoup(html, 'lxml')
    li = soup.find_all("p", attrs={'class' : 'text-black mt-1 font-serif'})
    for t in li:
        sentence_list.append(t.text)

    return sentence_list

""" if __name__ == '__main__':
    l = get_sentence('vase')
    print(l) """
