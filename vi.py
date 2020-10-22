# -*- coding: utf-8 -*-
from underthesea import sent_tokenize
art = 'Ứng dụng My YANMAR có giao diện đơn giản với tông màu đỏ - trắng chủ đạo, gồm nhiều nội dung như video, tài liệu ' \
      'giới thiệu và hướng dẫn sử dụng, tích hợp hệ thống định vị thông minh SMARTASSIST (SA-R) được biết đến như một ' \
      'công cụ quản lý máy và theo dõi vận hành từ xa hiệu quả.Ứng dụng này miễn phí, tất cả mọi người có điện thoại ' \
      'thông minh đều có thể cài đặt My YANMAR  thông qua chợ ứng dụng App Store và CH Play, ngoài ra, ứng dụng không ' \
      'yêu cầu cung cấp thông tin cá nhân, thao tác cài đặt đơn giản và dễ dàng sử dụng.Nội dung chính của MY ' \
      'YANMARVideo: Các video giới thiệu tính năng máy, hướng dẫn bảo dưỡng cho các loại máy nông nghiệp thương ' \
      'hiệu Yanmar, hướng dẫn sử dụng định vị SMARTASSIST, video lái thử máy, video phỏng vấn khách hàng, v.v…Tài liệu: ' \
      'Catalogue, sách hướng dẫn sử dụng và tài liệu liên quan khác Các liên kết: Danh sách đại lý, Tin tức, hệ thống ' \
      'SA-RCác thông báo: Thông báo mới nhất về chương trình khuyến mãi, chiến dịch chăm sóc máy Yanmar, giới thiệu sản ' \
      'phẩm mới, các tính năng mới, cập nhật các tin tức cần thiết khác liên quan đến sản phẩm Yanmar.Ứng dụng My YANMAR ' \
      'được kỳ vọng sẽ mang đến cho Quý khách hàng những thông tin bổ ích và thiết thực  trong suốt quá trình sử dụng m' \
      'áy, đồng thời đóng vai trò quan trọng trong việc kết nối và là kênh giao tiếp hiệu quả đối vớitất cả các khách ' \
      'hàng đang sử dụng máy Yanmar.Đối với khách hàng đang sử dụng máy nông nghiệp YANMAR có tích hợp bộ định vị thông ' \
      'minh SMARTASSIST (*) sẽ được Đại lý cung cấp tài khoản để đăng nhập hệ thống định vị- [Điểm nhấn đối với việc ' \
      'sử dụng SMARTASSIST]- Dễ dàng theo dõi máy- Truy cập ứng dụng để một cách thuận tiện và nhanh chóng.- Cập ' \
      'nhật nhanh chóng- Nhận thông báo về lần bảo dưỡng định kỳ sắp tới hoặc các sự kiện.- Tìm đại lý ủy quyền của ' \
      'Yanmar- Liên hệ với đại lý bằng email hoặc điện thoại(*) Một số dòng máy đang có tích hợp SMARTASSIST: máy gặt ' \
      'AW70V/82V SX-VN, YH700/850, YM351A/357A, EF725T đời mới.Ứng dụng My YANMAR sử dụng vị trí của bạn để điều ' \
      'hướng tới hoặc tìm kiếm đại   lý gần nhất, chỉ dẫn tuyến đường đi một cách nhanh chóng (tương tự các ứng dụng ' \
      'bản đồ phổ biến khác như Google Maps, Apple Maps). Trong quá trình sử dụng, ứng dụng không thu thập thông ' \
      'tin cá nhân (như tên, số điện thoại, địa chỉ) của người dùng, qua đó đảm bảo tính bảo mật người dùng trên ' \
      'internet.- Bản quyềnBản quyền đối với nội dung của ứng dụng này thuộc về Yanmar Holding Co., Ltd. Nghiêm ' \
      'cấm sao chép, trích dẫn, truyền tải, phân phối, thay đổi, sửa đổi hoặc bổ sung trái phép dưới mọi hình thức. '

article = open("Cong Nghe/article_11.txt", "r", encoding="utf-8")
article = article.read()
article = str(article)[1:-1]

# print(article)
# print(sent_tokenize(str(article)))
print(sent_tokenize(art))



