A = {1, 2, 3}
B = {3, 4, 5}


result = A ^ B


result = A.symmetric_difference(B)

print(result)  




set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

set1.add(7)
set1.remove(2)

print("Updated Set1:", set1)
