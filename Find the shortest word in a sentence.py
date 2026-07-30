# Find the shortest word in a sentence
string=str(input("Enter a string:"))
words=string.split()
shortest_word=words[0]
for word in words:
    if len(word)<len(shortest_word):
        shortest_word=word
print("Shortest word is",shortest_word)