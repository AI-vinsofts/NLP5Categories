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

vectorizer = pickle.load(open("vector.pickel", "rb"))
f.close()

def prediction(input):
    test = [preprocessing.preprocessing_data(input)]
    testmatx = vectorizer.transform(test)
    encodetest = testmatx.toarray()
    return str(nb.predict(encodetest)[0])

# PLEASE PASTE AN ARTICLE DOWN HERE
input = 'Vẻ nóng bỏng của người đẹp sinh năm 1990 khiến nhiều người trầm trồ...'
print(prediction(input))
