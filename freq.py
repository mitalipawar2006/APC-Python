# Find the number of times a specified character appears in a string
string=str(input("Enter a string:"))
freq={}
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
