import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original words:")
print(words)

print("After stopword removal:")
print(filtered_words)