# Set in Python

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
C = {10, 20}

# 1. add()
A.add(50)
print("1. After add():", A)

# 2. update()
A.update([60, 70])
print("2. After update():", A)

# 3. remove()
A.remove(70)
print("3. After remove():", A)

# 4. discard()
A.discard(60)
print("4. After discard():", A)

# 5. union()
print("5. Union:", A.union(B))

# 6. intersection()
print("6. Intersection:", A.intersection(B))

# 7. difference()
print("7. Difference:", A.difference(B))

# 8. symmetric_difference()
print("8. Symmetric Difference:", A.symmetric_difference(B))

# 9. issubset()
C = {10, 20}
print("9. Is C a subset of A?:", C.issubset(A))

# 10. issuperset()
print("10. Is A a superset of C?:", A.issuperset(C))