import json
jsonJoueurs = {
   "Joueur":[
      {
         "Nom":"Jordan",
         "NombreVictoires":0
      },
      {
         "Nom":"Thomas",
         "NombreVictoires":0
      },
      {
            "Nom":"Alexandre",
            "NombreVictoires":0
      }
   ]
}


jsonOuverture = open("TableauJoueurs.json", "w")
json.dump(jsonJoueurs, jsonOuverture, indent=3)
