alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}

alien_0["speed"] = "fast"

if alien_0["speed"] == "easy":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"The x_poisition of the alien is {alien_0['x_position']}")

# remove a key value pair
del alien_0["y_position"]

print(alien_0)

# get()
points = alien_0.get("points", "no point value exists in alien0")

print(points)
