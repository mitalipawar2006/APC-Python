# Replace all occurrences of a given character with another character. 
string=str(input("Enter a string"))
char1=str(input("Enter a character to be replaced"))
char2=str(input("Enter a char to replace a character from the string with:"))
for i in string:
    if i==char1:
        new=string.replace(char1,char2)
print(new)


