!pip install nltk

corpus="""Hello Welcome,to Krish Naik's NLP Tutorials.
Please do watch the entire course! to become expert in NLP.
"""
print(corpus)

##  Tokenization
## Sentence-->paragraphs
from nltk.tokenize import sent_tokenize

docs=sent_tokenize(corpus)

type(docs)

for sent in docs:
    print(sent)
from nltk.tokenize import word_tokenize

for sent in docs:
    print(word_tokenize(sent))
from nltk.tokenize import wordpunct_tokenize

wordpunct_tokenize(corpus)





