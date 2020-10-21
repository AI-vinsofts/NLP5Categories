from underthesea import sent_tokenize, word_tokenize, pos_tag, chunk, ner, classify, sentiment

text = "Trở lại với vấn đề chính, Keanu cho biết anh sẽ đưa hình ảnh meme của chính mình vào trong bộ truyện tranh BRZRKR, một dự án hợp tác giữa anh với Matt Kindt, Bill Crabtree, Clem Robin & Ron Garney. Dự án này sau đó đã được kêu gọi vốn trên Kickstarter vào ngày 1/9 vừa qua với mục tiêu 50.000 USD, nhưng con số thực tế mà họ nhận được là gần 1,5 triệu USD đến từ sự ủng hộ của 14.571 fan hâm mộ."
sentences = sent_tokenize(text)

for sentence in sentences:
    print(sentence)

print(word_tokenize(sentences[1], format=text))
print(sentiment(sentences[1]))