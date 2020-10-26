# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
import numpy
import string
import spacy

nlp = spacy.load('vi_spacy_model')
categories = ["Cong Nghe", "Du Lich", "Am Thuc", "Quan Su", "Thoi Trang"]

art0 = open(categories[0] + "/article_11.txt", "r", encoding='utf-8').read()[1:-1]
art1 = open(categories[1] + "/article_11.txt", "r", encoding='utf-8').read()[1:-1]
art2 = open(categories[2] + "/article_11.txt", "r", encoding='utf-8').read()[1:-1]
art3 = open(categories[3] + "/article_11.txt", "r", encoding='utf-8').read()[1:-1]
art4 = open(categories[4] + "/article_11.txt", "r", encoding='utf-8').read()[1:-1]
test = open(categories[0] + "/article_12.txt", "r", encoding='utf-8').read()[1:-1]


def preprocessing_data(anarticle):
    text = re.sub(r'\d+', ' ', anarticle)                   # remove number
    text = text.lower()                                     # lower case
    translator = str.maketrans('', '', string.punctuation)  # remove punctuation
    text = text.translate(translator)
    text = " ".join(text.split())                           # remove whitecase
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_stop:
            tokens.append(str(token))
    return ' '.join(tokens)


art0 = preprocessing_data(art0)
art1 = preprocessing_data(art1)
art2 = preprocessing_data(art2)
art3 = preprocessing_data(art3)
art4 = preprocessing_data(art4)
test = [preprocessing_data(test)]
# data = art0 + art1 + art2 + art3 + art4
article = [art0, art1, art2, art3, art4]


# Sklearn onehot
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(article)
# print(vectorizer.get_feature_names())
onehottrain = X.toarray()
print(onehottrain.shape)


# Sklearn onehot for testing
# testing = CountVectorizer()
T = vectorizer.fit_transform(test)
# print(testing.get_feature_names())
# d5 = array([[2, 0, 0, 1, 0, 0, 0, 1, 0]])
onehottest = T.toarray()
print(onehottest.shape)

clf = MultinomialNB()
clf.fit(onehottrain, categories)


# onehottest = numpy.array(onehottest)
print(onehottest[0])
# TEST
# print('Predicting class:', str(clf.predict(onehottest)[0]))
# print('Probability of d6 in each class:', clf.predict_proba(onehottest))
