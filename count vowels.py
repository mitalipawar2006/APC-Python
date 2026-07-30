	# Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
string=input("Enter a string: ")
vowels=0
consonants=0
digits=0
spaces=0
special_characters=0
for i in string:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowels+=1
        else:
            consonants+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        special_characters+=1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", special_characters)
