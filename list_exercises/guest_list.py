guests = ["Maria", "John", "David"]

print(f"Hello {guests[0]}! You are invited to dinner.")
print(f"Hello {guests[1]}! You are invited to dinner.")
print(f"Hello {guests[2]}! You are invited to dinner.")

# Changing the guest list
print(f"\nUnfortunately, {guests[1]} can't make it to dinner.")
guests[1] = "Michael"
print("\nHere is the updated guest list:")
print(f"Hello {guests[0]}! You are invited to dinner.")
print(f"Hello {guests[1]}! You are invited to dinner.")
print(f"Hello {guests[2]}! You are invited to dinner.")


# Adding more guests to the list

print("\nGood news! We found a bigger dinner table, so we can invite more guests.")

guests.insert(0, "Sarah")  # add guest at the beginning of the list
guests.insert(2, "James")  # add guest in the middle of the list
guests.append("Emily")  # add guest at the end of the list

print("\nHere is the updated guest list:")
print(f"Hello {guests[0]}! You are invited to dinner.")
print(f"Hello {guests[1]}! You are invited to dinner.")
print(f"Hello {guests[2]}! You are invited to dinner.")
print(f"Hello {guests[3]}! You are invited to dinner.")
print(f"Hello {guests[4]}! You are invited to dinner.")

print(f"\nSo far, we have decided to invite {len(guests)} guests for dinner.")

print("\nUnfortunately, we can only invite two guests for dinner.\n")
print(guests)

removed_guest = guests.pop()  # remove the last guest
print(f"\nSorry {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()  # remove the last guest
print(f"Sorry {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()  # remove the last guest
print(f"Sorry {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()  # remove the last guest
print(f"Sorry {removed_guest}, we can't invite you to dinner.")

print("\nHere is the final guest list:")
print(f"Hello {guests[0]}! You are still invited to dinner.")
print(f"Hello {guests[1]}! You are still invited to dinner.")

print("\nCurrent guest list:", guests)

del guests[1]  # remove the last guest
del guests[0]  # remove the remaining guest

print("\nThe guest list is now empty:", guests)
