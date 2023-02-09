import json
import random
class Joueurs:
    def __init__(self, nom, nombreVictoires, joueursBattus, Joue):
        self.nom = nom
        self.nombreVictoires = nombreVictoires
        self.joueursBattus = joueursBattus
        self.joue = Joue
    
    def description(self):
        print("Le joueur ", self.nom, "a gagné ", self.nombreVictoires, "fois et a battu ", self.joueursBattus)

#nom = input("Entrez votre nom : ")
#nouveauxJoueurs = {"Nom": nom, "NombreVictoires": 0, "JoueursBattus": [], NombreDefaites: 0}
    
    def afficherVictoires():
        with open("TableauJoueurs.json") as fichier:
            data = json.load(fichier)
            for element in data:
                print("Le joueur", element["Nom"], "a fait", element["NombreVictoires"], "victoires")
    
    
    def ecrireJson():
        nombrePif = random.randint(0,1)
        i = 1
        print(nombrePif)
        with open("TableauJoueurs.json") as fichier:
            data = json.load(fichier)
            test = data
            for element in test:

                if(element["Nom"] == "Bob" and nombrePif == 1):
                    element["NombreVictoires"] = element["NombreVictoires"] + 1
                print("Les joueurs battus par " + element["Nom"],  "sont : " )
                if(i == 1):
                    if(element["Nom"] == "Bob"):
                        element["JoueursBattus"] = element["JoueursBattus"] + ["Gohrien"]

                if(element["Nom"] == "AAAAAAAAAAAAH" and nombrePif == 0):
                    element["NombreVictoires"] += 1
                    #print("Les joueurs battus par " + element["Nom"] + " sont : ")
                        
                
                print("\n",element["JoueursBattus"], "\n")
                

        print("test vaut \n", test, "\n")

        with open("TableauJoueurs.json", "w") as fichier:
            json.dump(test, fichier)

    def compter_battus():
        with open("TableauJoueurs.json") as fichier:
            data = json.load(fichier)
        for element in data:
            battus = element["JoueursBattus"]
            dicJoueursBattus = {}
            for battu in battus:
                if(battu in dicJoueursBattus.keys()):
                    dicJoueursBattus [battu] += 1
                else:
                    dicJoueursBattus [battu] = 1
            print(dicJoueursBattus)
            for key in dicJoueursBattus:
                print("Le joueur",key, "a ete battu", dicJoueursBattus[key], "fois par", element["Nom"])
                
                
                #nombre = battus.count(battu)
                #print("Le joueur", battu, "a été battu", nombre, "fois par", element["Nom"])        
            
    def test_compter_battus():
    
        expected_output = "Le joueur Gorhien a ete battu 1 fois par Bob"
    
    
        result = Joueurs.compter_battus()
    
    
        assert result == expected_output

Joueurs.afficherVictoires()
#Joueurs.compter_battus()
#Joueurs.ecrireJson()


"""if(element["Nom"] == "Bob"):
                    element["NombreVictoires"] = element["NombreVictoires"] + 1
                print("Les joueurs battus par " + element["Nom"],  "sont : " )
                if(i == 1):
                    if(element["Nom"] == "Bob"):
                        element["JoueursBattus"] = element["JoueursBattus"] + ["Gohrien"]"""
