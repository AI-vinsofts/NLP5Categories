# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn
import numpy
import pandas
import re
import string
import spacy
import os
import preprocessing

nlp = spacy.load('vi_spacy_model')
nlp.max_length = 1300000
categories = os.listdir('Datasetmrhoang')
# ['Bóng đá', 'Giáo dục', 'Kinh doanh', 'Showbiz', 'Xe cộ']

art0 = ""
art1 = ""
art2 = ""
art3 = ""
art4 = ""

for file in os.listdir("Datasetmrhoang/" + categories[0]):
    art0 = art0 + open("Datasetmrhoang/" + categories[0] + "/" + file, "r", encoding='utf-8').read()[1:-1]
for file in os.listdir("Datasetmrhoang/" + categories[1]):
    art1 = art1 + open("Datasetmrhoang/" + categories[1] + "/" + file, "r", encoding='utf-8').read()[1:-1]
for file in os.listdir("Datasetmrhoang/" + categories[2]):
    art2 = art2 + open("Datasetmrhoang/" + categories[2] + "/" + file, "r", encoding='utf-8').read()[1:-1]
for file in os.listdir("Datasetmrhoang/" + categories[3]):
    art3 = art3 + open("Datasetmrhoang/" + categories[3] + "/" + file, "r", encoding='utf-8').read()[1:-1]
for file in os.listdir("Datasetmrhoang/" + categories[4]):
    art4 = art4 + open("Datasetmrhoang/" + categories[4] + "/" + file, "r", encoding='utf-8').read()[1:-1]



art0 = preprocessing.preprocessing_data(art0)
art1 = preprocessing.preprocessing_data(art1)
art2 = preprocessing.preprocessing_data(art2)
art3 = preprocessing.preprocessing_data(art3)
art4 = preprocessing.preprocessing_data(art4)

# data = art0 + art1 + art2 + art3 + art4
article = [art0, art1, art2, art3, art4]

# Sklearn encode
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(article)
# print(vectorizer.get_feature_names())
encodetrain = X.toarray()
print(encodetrain)

nb = MultinomialNB()
nb.fit(encodetrain, categories)

## OPEN AN ARTICLE FROM TEXT.TXT
test = open("text.txt", "r", encoding='utf-8').read()[1:-1]
test = [preprocessing.preprocessing_data(test)]


# Testing encode
testmatx = vectorizer.transform(test)
encodetest = testmatx.toarray()
# print(test)

print('Predicting class:', str(nb.predict(encodetest)[0]))
print('Probability of d6 in each class:', nb.predict_proba(encodetest))
