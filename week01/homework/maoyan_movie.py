import requests
import random
from bs4 import BeautifulSoup as bs
import pandas as pd

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

user_agent = random.choice(USER_AGENT_LIST)
header = {'user-agent': user_agent}
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl, headers=header)

bs_info = bs(response.text, "html.parser")
# for tags in bs_info.find_all('div', attrs={'class':'hd'}) :
#     for atag in tags.find_all('a'):
#         print(atag.get('href'))
#         print(atag.find('span').text)

info = bs_info.find_all('div', attrs={"class": "movie-hover-title"})
spans = info[0].find_all('span')
title = spans[0].text()
category = info[1].text()
actor = info[2].text()
release_time = info[3].text()

my_list = [title, category, actor, release_time]
movie = pd.DataFrame(data=my_list)
movie.to_csv("./bs4_movie.csv", encoding="utf8", mode="a", index=False, header=False)
