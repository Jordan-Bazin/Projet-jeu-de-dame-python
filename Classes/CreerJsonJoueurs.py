import json
import pprint

jsonJoueurs = """[
   {
         "Nom": "Jordan",
         "NombreVictoires": 0
   },
   {
         "Nom": "Thomas",
         "NombreVictoires": 0
   },
   {
         "Nom": "Alexandre",
         "NombreVictoires": 0
   }
]"""


test = {"Bite":7}

data = json.loads(jsonJoueurs)
print("Le type de mon json est ", type(data)) 

for element in data:
      element.update(test)
      if(element['Nom'] == "Jordan"):
            print("AAAAAAAAAAH j'ai trouvé", element['Nom'], '\n')
            print("Voici la personne qui vient de gagner : ",element, '\n')
            element['NombreVictoires'] = element['NombreVictoires'] + 1
      print(element)
            
fichier = open("TableauJoueurs.json", "r")
print("\n\n Le fichier contient ",fichier.read() ,"\n\n")
fichier.close()

with open('TableauJoueurs.json', 'w') as fichier:
      json.dump(data, fichier, indent=2)



print("Le fichier a été écrit")


