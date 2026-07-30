# Convert the first letter of every word to uppercase. 
sentence=str(input("Enter a string:"))
words=sentence.split()       
for word in words:
    print(word.capitalize(),end=" ")