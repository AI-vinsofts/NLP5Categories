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

# Preprocessing function
def preprocessing_data(anarticle):
    text = re.sub(r'\d+', ' ', anarticle)                   # remove number
    text = text.lower()                                     # lower case
    translator = str.maketrans('', '', string.punctuation)  # remove punctuation
    text = text.translate(translator)
    text = " ".join(text.split())
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

# data = art0 + art1 + art2 + art3 + art4
article = [art0, art1, art2, art3, art4]

# Sklearn encode
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(article)
# print(vectorizer.get_feature_names())
encodetrain = X.toarray()
print(encodetrain)

test = open("Test/Bóng đá/article_379.txt", "r", encoding='utf-8').read()[1:-1]
test = [preprocessing_data(test)]

# Testing encode
testmatx = vectorizer.transform(test)
encodetest = testmatx.toarray()
# print(test)

nb = MultinomialNB()
nb.fit(encodetrain, categories)
print('Predicting class:', str(nb.predict(encodetest)[0]))
print('Probability of d6 in each class:', nb.predict_proba(encodetest))

# Evaluate Testdataset
y_test = []
y_pred = []
top1 = 0
test0 = ""
for i in range(len(categories)):
    for file in os.listdir("Test/" + categories[i]):
        test = open("Test/" + categories[i] + "/" + file, "r", encoding='utf-8').read()[1:-1]
        test = [preprocessing_data(test)]
        # Testing encode
        testmatx = vectorizer.transform(test)
        encodetest = testmatx.toarray()
        if categories[i] == nb.predict(encodetest)[0] :
            top1 = top1 + 1
        y_test.append(categories[i])
        y_pred.append(nb.predict(encodetest)[0])

print("Top 1 Accuracy: " + str(top1/len(y_test)*100.))

# Plot Confusion matrix
array = confusion_matrix(y_test,y_pred)
df_cm = pandas.DataFrame(array, index=categories, columns=categories)

df_norm_col = df_cm.astype('float') / df_cm.sum(axis=1)[:, numpy.newaxis]

seaborn.set(font_scale=1.5) # for label size
seaborn.heatmap(df_norm_col, annot=True, annot_kws={"size": 20}, cmap="Blues") # font size
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.savefig('C:/Users/Hoan/PycharmProjects/NLPresearch/ConfusionMatrix.png', dpi=50)
plt.show()
