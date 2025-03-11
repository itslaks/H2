items = []

while True:
    item = input("Enter an item (type 'exit' to stop): ")
    if item.lower() == 'exit':
        break
    items.append(item)

print("\nYou entered:")
print(items)


