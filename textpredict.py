# -*- coding: utf-8 -*-
import spacy
import os
import preprocessing
import pickle

nlp = spacy.load('vi_spacy_model')
nlp.max_length = 1300000
categories = ['Bóng đá', 'Giáo dục', 'Kinh doanh', 'Showbiz', 'Xe cộ']

f = open('NLPnaivebayes.pickle', 'rb')
nb = pickle.load(f)

# load pickle
vectorizer = pickle.load(open("vector.pickel", "rb"))
f.close()
# OPEN AN ARTICLE FROM TEXT.TXT
test = open("text.txt", "r", encoding='utf-8').read()[1:-1]
test = [preprocessing.preprocessing_data(test)]

# Testing encode
testmatx = vectorizer.transform(test)
encodetest = testmatx.toarray()
print('Predicting class:', str(nb.predict(encodetest)[0]))
print('Probability of d6 in each class:', nb.predict_proba(encodetest))
