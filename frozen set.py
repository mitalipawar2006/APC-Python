# Frozen Set in Python

A = frozenset({10, 20, 30, 40})
B = frozenset({30, 40, 50, 60})
C = frozenset({10, 20})

# 1. union()
print("1. Union:", A.union(B))

# 2. intersection()
print("2. Intersection:", A.intersection(B))

# 3. difference()
print("3. Difference:", A.difference(B))

# 4. symmetric_difference()
print("4. Symmetric Difference:", A.symmetric_difference(B))

# 5. issubset()
print("5. Is C a subset of A?:", C.issubset(A))

# 6. issuperset()
print("6. Is A a superset of C?:", A.issuperset(C))

# 7. isdisjoint()
D = frozenset({70, 80})
print("7. Are A and D disjoint?:", A.isdisjoint(D))

# 8. copy()
E = A.copy()
print("8. Copy of A:", E)

# 9. len()
print("9. Length of A:", len(A))

# 10. membership using 'in'
print("10. Is 20 present in A?:", 20 in A)