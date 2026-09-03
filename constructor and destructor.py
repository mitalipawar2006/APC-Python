class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor is called")
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Destructor called")
        print("Object destroyed")

s1 = Student("mitali", 20)
del s1