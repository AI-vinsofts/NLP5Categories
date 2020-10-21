# -*- coding: utf-8 -*-
import vi_spacy_model
import time
from pyvi import ViTokenizer, ViPosTagger, ViUtils, ViDiac
docs = (u"Giờ tôi lại lang thang. Tình yêu thì miên man. Ngày xanh cùng mây tung tăng tựa mình bên phím đàn. Nhìn em mình ngơ ngác. Lòng anh chợt hơi khác. Tình yêu này đến đúng lúc thấy ánh sáng vụt qua. Nụ cười tỏa hương nắng. Bình minh và mây trắng. Hình như đều kêu tôi ôi thôi tình yêu đến rồi! Chẳng ai phải thắc. Còn tôi thì đã chắc. Nàng ơi nàng hãy đến chiếm lấy tâm hồn tôi. Mỉm cười lòng chợt bâng khuâng tôi chẳng biết mơ hay thật. Đợi chờ dù ngày hay đêm anh chỉ cần nghĩ cũng thấy vui.")

start = time.time()
nlp = vi_spacy_model.load()
doc = nlp(docs)
arr = []
for token in doc:
    arr.append(token.text)
print("Đây là SpaCcy óc chó")
print(arr)

from underthesea import sent_tokenize, word_tokenize, pos_tag, sentiment
print("Đây là Dưới đáy biển")
print(word_tokenize(docs))
end = time.time() - start
print(end)


