import os

print(os.getcwd())

if not os.path.exists("newdir"):
    os.mkdir("newdir")
    # os.makedirs("A/B/C")
    print("Directory created")
else:
    print("Directory already exists")

print(os.listdir())
# os.rmdir("newdir")


# os.rename("newdir", "myfolder")



if os.path.isdir("myfolder"):
    print("It is a directory")
else:
    print("It is not a directory")


path = os.path.join("myfolder", "data.txt")

print(path)