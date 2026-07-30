# Remove all spaces from the input string. 
string=str(input("Enter a string:"))
for i in string:
    if i.isspace():
        new=string.replace(" ","")
print(new)

