# import mymodule

# print(mymodule.add(10, 5))
# print(mymodule.subtract(10, 5))
# print(mymodule.x)
from mymodule import add
print(add(10, 5))
from mypackage.mathmodule import multiply
print(multiply(10, 5))
from mypackage.message import greet
print(greet("Mitali"))