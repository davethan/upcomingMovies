# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup
import datetime

URL = "https://www.imdb.com/calendar?region=FR&ref_=rlm"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
movies = soup.find(id = "main").get_text()

print (movies)