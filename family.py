# Defining a dictionary with family names as keys and their respective houses as values
family = {
    "Chloe": "Bhongweni",
    "Thandolwethu": "Tolo",
    "Luvuyo": "Bhongweni",
    "Melissa": "Bhongweni",
    "Iets": "Tolo",
    "Andiswa":  "Tolo",
    "Nobuhle":  "Rhadebe"
}

# Iterating over each person in the dictionary
for person in family:
    # Printing each person's name and their corresponding house, separated by a comma and space
    print(person, family[person], sep=", ")
