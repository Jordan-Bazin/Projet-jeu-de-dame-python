import json

class Joueur:
      def __init__(self, nom, nombreVictoires, joueursBattus, joue):
            self.nom = nom
            self.nombreVictoire = nombreVictoires
            self.joueursBattus = joueursBattus
            self.joue = joue
            
            
            
            
            
            
            
def ecrireJson():
        i = 1
        with open("TableauJoueurs.json") as fichier:
            data = json.load(fichier)
            test = data
            for element in test:

                if(element["Nom"] == "Bob"):
                    element["NombreVictoires"] = element["NombreVictoires"] + 1
                print("Les joueurs battus par " + element["Nom"],  "sont : " )
                if(i == 1):
                    if(element["Nom"] == "Bob"):
                        element["JoueursBattus"] = element["JoueursBattus"] + ["Gohrien"]

                    
                        
                
                print("\n",element["JoueursBattus"], "\n")
                

        print("test vaut \n", test, "\n")

        with open("TableauJoueurs.json", "w") as fichier:
            json.dump(test, fichier)