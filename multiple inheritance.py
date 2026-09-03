class Father:
    def show_father(self):
        print("it's a father class")
class Mother:
    def show_mother(self):
        print("it's a mother class")
class child(Father,Mother):
    def show_child(self):
        print("it's child class")
c=child()
c.show_father()
c.show_mother()
c.show_child()
