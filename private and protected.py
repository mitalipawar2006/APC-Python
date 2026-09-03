class Grandparent:

    __private_value = 10

    _protected_value = 20

    def __private_function(self):
        print("Private function of Grandparent")

    def _protected_function(self):
        print("Protected function of Grandparent")


class Parent(Grandparent):

    def show_parent(self):
        print("Protected variable:", self._protected_value)
        self._protected_function()


class Child(Parent):

    def show_child(self):
        print("Child accessing protected variable:", self._protected_value)
        self._protected_function()


c = Child()

c.show_parent()
c.show_child()