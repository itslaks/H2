# 1) Reverse a list in Python

lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

# 2) Concatenate two lists index-wise

list1 = ["A", "B", "C"]
list2 = ["1", "2", "3"]
result = [a + b for a, b in zip(list1, list2)]
print(result)  # Output: ['A1', 'B2', 'C3']


# 3) Turn every item of a list into its square

nums = [2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared)  # Output: [4, 9, 16, 25]


# 4) Concatenate two lists in the following order

list1 = ["Hello", "Take"]
list2 = ["Dear", "Sir"]
result = [x + y for x in list1 for y in list2]
print(result)  
# Output: ['HelloDear', 'HelloSir', 'TakeDear', 'TakeSir']


# 5) Iterate both lists simultaneously

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

for a, b in zip(list1, list2):
    print(a, b)


# 6) Remove empty strings from the list of strings

str_list = ["Hello", "", "World", "", "Python"]
filtered_list = list(filter(None, str_list))
print(filtered_list)  # Output: ['Hello', 'World', 'Python']


# 7) Exercise 7: Add new item to list after a specified item

def insert_after(lst, target, new_item):
    try:
        idx = lst.index(target) + 1
        lst.insert(idx, new_item)
    except ValueError:
        print("Item not found")

lst = [10, 20, 30, 40]
insert_after(lst, 20, 25)
print(lst)  # Output: [10, 20, 25, 30, 40]


# 8) Extend nested list by adding the sublist

nested_list = [[1, 2], [3, 4]]
sublist = [5, 6]
nested_list[-1].extend(sublist)
print(nested_list)  # Output: [[1, 2], [3, 4, 5, 6]]


# 9) Replace list’s item with new value if found

lst = [10, 20, 30, 40]
old, new = 20, 25
lst = [new if x == old else x for x in lst]
print(lst)  # Output: [10, 25, 30, 40]


# 10) Remove all occurrences of a specific item from a list.

lst = [10, 20, 30, 20, 40, 20]
item_to_remove = 20
lst = [x for x in lst if x != item_to_remove]
print(lst)  # Output: [10, 30, 40]
