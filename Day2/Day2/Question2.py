# Create the dictionary
planet_size = {"Earth": 40075, "Saturn": 378675, "Jupiter": 439264}
# Print the dictionary
print(planet_size)
# Print the type
print(type(planet_size))

print(planet_size["Earth"])
# get() function
print(planet_size.get("Saturn"))

# Update the planet_size Earth and print
planet_size["Earth"] = 40095
print(planet_size)

planet_size["Sun"] = 542844
print(planet_size)

# Delete an item then print
del planet_size["Jupiter"]
print(planet_size)

del planet_size