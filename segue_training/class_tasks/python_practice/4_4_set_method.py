#eg 1 
# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# add()
set1.add(7)
print("After add():", set1)

# clear()
set1.clear()
print("After clear():", set1)

# copy()
set1 = {1, 2, 3, 4}
copy_set = set1.copy()
print("After copy():", copy_set)

# difference()
print("difference():", set1.difference(set2))
print("Using - :", set1 - set2)

# difference_update()
set1.difference_update(set2)
print("After difference_update():", set1)

# discard()
set1 = {1, 2, 3, 4}
set1.discard(2)
print("After discard():", set1)

# intersection()
print("intersection():", set1.intersection(set2))
print("Using & :", set1 & set2)

# intersection_update()
set1.intersection_update(set2)
print("After intersection_update():", set1)

# isdisjoint()
set1 = {1, 2}
print("isdisjoint():", set1.isdisjoint(set2))

# issubset()
print("issubset():", set1.issubset(set2))
print("Using <= :", set1 <= set2)
print("Using < :", set1 < set2)

# issuperset()
print("issuperset():", set2.issuperset(set1))
print("Using >= :", set2 >= set1)
print("Using > :", set2 > set1)

# pop()
set1 = {1, 2, 3}
set1.pop()
print("After pop():", set1)

# remove()
set1.remove(3)
print("After remove():", set1)

# symmetric_difference()
set1 = {1, 2, 3, 4}
print("symmetric_difference():", set1.symmetric_difference(set2))
print("Using ^ :", set1 ^ set2)

# symmetric_difference_update()
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update():", set1)

# union()
set1 = {1, 2, 3}
print("union():", set1.union(set2))
print("Using | :", set1 | set2)

# update()
set1.update(set2)
print("After update():", set1)



