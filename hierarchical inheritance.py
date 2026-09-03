class Animal:

    def eat(self):
        print("Animal can eat")


class Dog(Animal):

    def bark(self):
        print("Dog can bark")


class Cat(Animal):

    def meow(self):
        print("Cat can meow")



d = Dog()
d.eat()
d.bark()


c = Cat()
c.eat()
c.meow()