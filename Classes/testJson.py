import json

with open("TableauJoueurs.json") as fichier:
    data = json.load(fichier)
    print(data)
    test = data
    print("Mon test vaut \n", test, "\n")
    for element in test:
        if(element["Nom"] == "Bob"):
            element["Bite"] = element["Bite"] + 1

print("test vaut \n", test, "\n")
print("data vaut \n", data, "\n")

with open("TableauJoueurs.json", "w") as fichier:
    json.dump(test, fichier)
"""
[
    {
        "Nom": "AAAAAAAAAAAAH",
        "Bite": 5
    },
    {
        "Nom": "Bob",
        "Bite": 58
    }
]
"""