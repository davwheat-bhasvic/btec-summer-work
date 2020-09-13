example_string = 'Hello world! How "lovely" this world is.'
print(example_string)

print("Length  :", len(example_string))
print("Replace :", example_string.replace("world", "Earth"))
print("Upper   :", example_string.upper())
print("Lower   :", example_string.lower())

# Remember that indexes start at 0, like 99.99% of all languages
# Position 3 is index 2
print("3rd char:", example_string[2])

print("ind of !:", example_string.index("!"))
print("i of How:", example_string.index("How"))

# This will trigger a ValueError, so 
print("i of poo:", example_string.index("poo"))
