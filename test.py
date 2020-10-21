from bs4 import BeautifulSoup
import requests
import urllib.request
import time

# GET ARTICLE LINKS FROM 5 PAGES OF 24H.COM.VN
linksarr = []
articlearr = []
count = 0
set_url = set()
for i in range(1, 6):
    url = "https://www.24h.com.vn/kham-pha-cong-nghe-c675.html?vpage=" + str(i)

    html_page = requests.request(method='GET', url=url).content
    # print(html_page)
    print()
    soupp = BeautifulSoup(html_page, "html.parser")
    links = soupp.find_all('span',attrs={"class": "nwsTit postname"})
    print(links)
    # for link in links:
    #     set_url.add(link['href'])
        # print(set_url)
# imgFltT4 imgNwsHm
# nwsTit