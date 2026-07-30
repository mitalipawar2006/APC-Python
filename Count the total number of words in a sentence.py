# Count the total number of words in a sentence. 
string=str(input("Enter a string:"))
words=string.split()
count=0
for word in words:
    count+=1
print("no. of words is:",count)
