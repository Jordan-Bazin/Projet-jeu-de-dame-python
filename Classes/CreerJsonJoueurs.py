jsonJoueurs = open("TableauJoueurs.json", "r")
print(jsonJoueurs.read())
jsonJoueurs.close()
jsonJoueurs = open("TableauJoueurs.json", "w")
jsonJoueurs.write('')