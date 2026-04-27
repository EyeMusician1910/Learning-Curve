#Sentence Tokenizer
from nltk.tokenize import sent_tokenize

text = "Bury the lightning deep within. Cast aside, there's no coming home"
print(sent_tokenize(text))
import nltk.data

# Loading PunktSentenceTokenizer using English pickle file
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
print(tokenizer.tokenize(text))

#Words Tokenizer
from nltk.tokenize import word_tokenize

text = "Bury the lightning deep within. Cast aside, there's no coming home"
print(word_tokenize(text))

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(text))

#Using WordPunktokenizer
from nltk.tokenize import WordPunctTokenizer

tokenizer = WordPunctTokenizer()
tokenizer.tokenize("Bury the lightning deep within. Cast aside, there's no coming home")