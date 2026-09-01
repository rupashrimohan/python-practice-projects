shops = ["walmart", "Target", "costco", "Best Buy", "Home Depot"]
# printing the list
print("Printing the list of shops:")
print(shops)

# Accessing the elements of the list using indexing
print("\nAccessing the elements of the list of indexes(0,1,-1):")
print(shops[0].title())
print(shops[1].title())
print(shops[-1].title())

# Using Individual values from the list
print(f"\nMy favorite shop is at index -2: {shops[-2].title()}.")

# Modifying the elements of the list
# del
print("\nModifying the elements of the list:")
print("del removed the value at index 0 of the list.")
del shops[0]  # removes the first element of the list
print(shops)
# pop removed the last element of the list and returns it. It can also remove an element at a specific index if provided.
print("\npop")
removed_shop = shops.pop()
print(f"\nThe last shop I removed from the list is {removed_shop.title()}.")
print(f"\nThe updated list of shops is: {shops}")
# pop(index)
removed_shop = shops.pop(1)
print(f"\nThe shop I removed from the list is at index 1: {removed_shop.title()}.")
print(f"\nThe updated list of shops is: {shops}")

# insert(index, value)
print("\ninsert")
print("\nInserted Kroger at index 1 of the list.")
shops.insert(1, "Kroger")  # inserts the value at the specified index
print(f"\nThe updated list of shops is: {shops}")

# append(value) adds the value to the end of the list
print("\nappend")
print("\nAppended Trader Joe's and Costco to the list of shops:")
shops.append("Trader Joe's")  # adds the value to the end of the list
print(f"\nThe updated list of shops is: {shops}")
shops.append("Costco")
print(f"\nThe updated list of shops is: {shops}")


# remove(value) removes the first occurrence of the value from the list
print("\nremove")
print("\nRemoved costco from the list of shops")
shops.remove("Costco")  # removes the first occurrence of the value from the list
print(f"\nThe updated list of shops is: {shops}")

# Organizing the list
print(f"\nOrganizing the list of shops:{shops}")
print("\nsorted()")
# sorted() sorts the list in alphabetical order without modifying the original list
print(f"\nThe sorted() list of shops is: {sorted(shops)}")

# sorted(list, reverse=True) sorts the list in reverse alphabetical order without modifying the original list
print(
    f"\nThe sorted() list of shops in reverse alphabetical order is: {sorted(shops, reverse=True)}"
)

print("\nsort()")
print(f"\nThe original list of shops is: {shops}")
# sort() sorts the original list in alphabetical order
shops.sort()
print(f"\nThe sort() list of shops is: {shops}")
# sort(reverse=True) sorts the original list in reverse alphabetical order
shops.sort(reverse=True)
print(f"\nThe sort() list of shops in reverse alphabetical order is: {shops}")
# reverse() reverses the order of the list in place
print("\nreverse()")
shops.reverse()
print(f"\nThe reversed list of shops is: {shops}")

print(
    f"\nThe final list of shops is: {shops} and the length of the list is: {len(shops)}"
)
