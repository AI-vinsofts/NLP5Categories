from bs4 import BeautifulSoup
import urllib.request
import re
import string
import spacy
nlp = spacy.load('vi_spacy_model')

link = 'https://www.24h.com.vn/kham-pha-cong-nghe/chay-tui-khi-mua-sale-sap-san-ngay-le-doc-than-11-thang-11-tai' \
       '-tmall-va-taobao-c675a1192234.html '

articlearr = []
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
article = soup.find_all("p", text=True)
for art in article:
    art = art.text.replace('\xa0', '')\
        # .replace(
        # 'Cơ quan chủ quản: Công ty Cổ phần Quảng cáo Trực tuyến 24H Trụ sở: Tầng 12, Tòa nhà Geleximco, '
        # '36 Hoàng Cầu, Phường Ô Chợ Dừa, Quận Đống Đa, TP Hà Nội. Tel: (84-24) 73 00 24 24 hoặc (84-24) '
        # '3512 1806 - Fax: (84-24) 3512 1804. Chi nhánh: Tầng 7, Tòa nhà Việt Úc, 402 Nguyễn Thị Minh Khai, '
        # 'Phường 5, Quận 3, TP. Hồ Chí Minh. Tel: (84-28) 7300 2424 / Giấy phép số 332/GP – TT ĐT ngày cấp '
        # '22/01/2018 SỞ THÔNG TIN VÀ TRUYỀN THÔNG HÀ NỘI. Chịu trách nhiệm xuất bản: Phan Minh Tâm. '
        # 'HOTLINE: 0965 08 24 24', ' ')
    articlearr.append(art)  # Douma cho nay dung roi ban oi
articlearr = [' '.join(articlearr)]

print(articlearr)
def preprocessing_data(anarticle):
    # text = re.sub(r'\d+', ' ', anarticle)                   # remove number
    # text = text.lower()                                     # lower case
    # translator = str.maketrans('', '', string.punctuation)  # remove punctuation
    # text = text.translate(translator)
    # text = " ".join(text.split())                           # remove whitecase
    anarticle = nlp(anarticle)
    tokens = []
    # for token in doc:
    #     if not token.is_stop:
    #         tokens.append(str(token))
    return tokens
