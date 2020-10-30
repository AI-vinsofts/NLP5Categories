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

# PLEASE PASTE AN ARTICLE IN THE LINE DOWN BELOW INSIDE THE ' '
test = '"Mỹ nhân cảnh nóng" khiến tình cũ Chi Pu say đắm vì quá gợi cảm là ai?...'
test = [preprocessing.preprocessing_data(test)]

# Testing encode
testmatx = vectorizer.transform(test)
encodetest = testmatx.toarray()
print('Predicting class:', str(nb.predict(encodetest)[0]))
print('Probability of d6 in each class:', nb.predict_proba(encodetest))
