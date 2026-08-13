# file=open("data.txt", "r")
# data=file.read()
# print(data)
# file.close()
# with open("data.txt", "r") as file:
#     data=file.read()
#     print(data) 
with open("data.txt","w") as file:
    file.write("Hello Python")
with open("data.txt","a") as file:
    name=input("Enter your name:")
    file.write("\n"+ name)
print("Name added successfully!")
with open("data.txt","r") as file:
    line=file.readline()
    print(line)
with open("data.txt","r") as file:
    lines=file.readlines()
    print(lines)
with open("data.txt", "r") as file:
    print(file.tell())

    data = file.read(5)
    print(data)

#     print(file.tell())
# with open("data.txt", "r") as file:
#     file.seek(0)
#     data=file.read()
#     print(data)
# with open("data.txt", "r+") as file:
#     print(file.read())

#     file.write("Hello")
with open("data.txt", "w+") as file:
    file.write("Hello Python")
    
    file.seek(0)
    
    data = file.read()
    print(data)
with open("data.txt", "a+") as file:
    file.write("\nWelcome to Python")
    
    file.seek(0)
    
    data = file.read()
    print(data)
