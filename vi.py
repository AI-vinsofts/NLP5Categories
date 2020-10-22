from bs4 import BeautifulSoup
import urllib.request

articlearr = []
page = urllib.request.urlopen("https://www.24h.com.vn/the-gioi-thoi-trang/nhung-doi-giay-balenciaga-chua-bao-gio-"
                              "het-hot-c672a1169533.html")
soup = BeautifulSoup(page, 'html.parser')
article = soup.find_all("p", text=True)
print(article)
# for art in article:
#     art = art.text

