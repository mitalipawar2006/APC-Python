A = {
    "name": "Mitali",
    "age": 20,
    "course": "CSE"
}

B = {
    "city": "Kolhapur",
    "college": "DYPCET"
}

print("1. Get:", A.get("name"))

print("2. Keys:", A.keys())

print("3. Values:", A.values())

print("4. Items:", A.items())

A.update(B)
print("5. After update():", A)

A.pop("age")
print("6. After pop():", A)

A.popitem()
print("7. After popitem():", A)

A.setdefault("branch", "Computer Science")
print("8. After setdefault():", A)

C = A.copy()
print("9. Copy of A:", C)

C.clear()
print("10. After clear():", C)