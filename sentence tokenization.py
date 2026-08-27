import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt_tab')

text = input("Enter a paragraph: ")

sentences = sent_tokenize(text)

print("Sentences:")
for sentence in sentences:
    print(sentence)