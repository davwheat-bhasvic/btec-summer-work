def translate(string):
    trans = ""

    for char in string:
        if char.lower() in "aeiou":
            trans += "G" if char.isupper() else "g"
        else:
            trans += char

    return trans


print(translate(input("Enter text: ")))
