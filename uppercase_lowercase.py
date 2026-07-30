	# Count the number of uppercase and lowercase letters in a string. 
string=str(input("Enter a string:"))
uppercase_count=0
lowercase_count=0
for i in string:
    if i.isalpha():
        if i.isupper():
            uppercase_count+=1
        elif i.islower():
            lowercase_count+=1
print("No. of uppercase letters: ",uppercase_count)
print("No. of lowercase letters:",lowercase_count)