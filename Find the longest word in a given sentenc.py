# Find the longest word in a given sentence. 
string=str(input("Enter a string"))
words=string.split()
longest_word=words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("The longest word is:", longest_word)

