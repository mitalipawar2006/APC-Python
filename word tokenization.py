import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

print("Tokens:")
for token in tokens:
    print(token)