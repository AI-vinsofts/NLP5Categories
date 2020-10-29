import re
import string
import spacy

nlp = spacy.load('vi_spacy_model')
# PREPROCESSING FUNCTION
def preprocessing_data(text):
    text = re.sub(r'\d+', ' ', text)                         # remove number
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
