from bs4 import BeautifulSoup
import urllib.request

# GET ARTICLE LINKS FROM 5 PAGES OF 24H.COM.VN
linksarr = []
articlearr = []
total = []
count = 0
set_url = set()
for i in range(1, 6):
    print()
    url = "https://www.24h.com.vn/kham-pha-cong-nghe-c675.html?vpage=" + str(i)
    html_page = urllib.request.urlopen(url)
    soupp = BeautifulSoup(html_page, "html.parser")
    links = soupp.find_all('span', attrs={"class": "nwsTit postname"})
    # print()
    for link in links:
        set_url.add(link.find('a', href=True)['href'])

linksarr = list(set_url)

for link in linksarr:
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    article = soup.find_all("p", text=True)
    for art in article:
        art = art.text.replace('\xa0', ' ').replace(
                    'Cơ quan chủ quản: Công ty Cổ phần Quảng cáo Trực tuyến 24H Trụ sở: Tầng 12, Tòa nhà Geleximco, '
                    '36 Hoàng Cầu, Phường Ô Chợ Dừa, Quận Đống Đa, TP Hà Nội. Tel: (84-24) 73 00 24 24 hoặc (84-24) '
                    '3512 1806 - Fax: (84-24) 3512 1804. Chi nhánh: Tầng 7, Tòa nhà Việt Úc, 402 Nguyễn Thị Minh Khai, '
                    'Phường 5, Quận 3, TP. Hồ Chí Minh. Tel: (84-28) 7300 2424 / Giấy phép số 332/GP – TT ĐT ngày cấp '
                    '22/01/2018 SỞ THÔNG TIN VÀ TRUYỀN THÔNG HÀ NỘI. Chịu trách nhiệm xuất bản: Phan Minh Tâm. '
                    'HOTLINE: 0965 08 24 24', ' ')
        articlearr.append(art)
        articlearr = [''.join(articlearr)]
        total.append(articlearr)

#             count = count + 1
#             print(str(count) + ' Loading ...')
# print(len(total))
#     text_file = open("Cong Nghe/article_" + str(i) + ".txt", "w", encoding='utf-8')
#     text_file.write(str(articlearr))

print(len(total))
