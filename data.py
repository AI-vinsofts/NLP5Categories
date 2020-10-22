from bs4 import BeautifulSoup
import urllib.request

set_url = set()
categories = [" ", "Cong Nghe", "Du Lich", "Am Thuc", "Quan Su", "Thoi Trang"]
categoriesurl = ["",
                "https://www.24h.com.vn/kham-pha-cong-nghe-c675.html?vpage=",
                "https://www.24h.com.vn/du-lich-24h-c76.html?vpage=",
                "https://www.24h.com.vn/am-thuc-c460.html?vpage=",
                "https://www.24h.com.vn/quan-su-c705.html?vpage=",
                "https://www.24h.com.vn/the-gioi-thoi-trang-c672.html?vpage="]


for n in range(1, 6):
    for i in range(1, 6):
        # LINK FROM ARRAY
        urll = categoriesurl[n] + str(i)
        html_page = urllib.request.urlopen(urll)
        soupp = BeautifulSoup(html_page, "html.parser")
        links = soupp.find_all('span', attrs={"class": "nwsTit postname"})
        for link in links:
            # print(link.find('a', href=True)['href'])
            set_url.add(link.find('a', href=True)['href'])
        linksarr = list(set_url)
        print(len(linksarr))
        count = 0
        for link in linksarr:
            articlearr = []
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
                articlearr.append(art)              # Douma cho nay dung roi ban oi
            articlearr = [''.join(articlearr)]
            count = count + 1
            print('Loading ' + str(count) + '...')
            # CATEGORY FOLDER
            text_file = open(categories[n] + "/article_" + str(i) + str(count) + ".txt", "w", encoding="utf-8")
            text_file.write(str(articlearr))
        del linksarr
