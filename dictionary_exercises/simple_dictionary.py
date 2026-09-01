alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print(alien_0)

alien_0["x-cord"] = 0
alien_0["y-cord"] = 25

print(alien_0)

# modifying value

print(f"The color of the alien is {alien_0['color']}")

alien_0["color"] = "yellow"
print(f"The color of the alien now is {alien_0['color']}")
