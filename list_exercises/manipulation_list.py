places = ["Paris", "Alaska", "Safari", "Japan", "London"]

print(places)
# Sorted() sorts the list in alphebetical order without modifying the original list
print(f"\nSorted in Alphabetical Order: {sorted(places)}\n")
print(f"Original List: {places}\n")
# sorted(list, reverse=True) sorts the list in reverse alphabetical order without modifying the original list
print(f"Sorted in Reverse Alphabetical Order: {sorted(places, reverse=True)}\n")
print(f"Original List: {places}\n")

# reverse() reverses the order of the list in place
places.reverse()
print(f"Reversed Order: {places}\n")
places.reverse()
print(f"Original Order: {places}\n")

# sort() sorts the original list in alphabetical order
places.sort()
print(f"Sorted in Alphabetical Order: {places}\n")

places.sort(reverse=True)
print(f"Sorted in Reverse Alphabetical Order: {places}\n")
