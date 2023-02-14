import json
import random
import os


class Joueurs:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '\TableauJoueurs.json'
    def __init__(self, nom, nombreVictoires, joueursBattus, Joue):
        self.nom = nom
        self.nombreVictoires = nombreVictoires
        self.joueursBattus = joueursBattus
        self.joue = Joue
    
    def description(self):
        print("Le joueur ", self.nom, "a gagné ", self.nombreVictoires, "fois et a battu ", self.joueursBattus)

    def testerJson(self):
        if(os.path.exists(self.file_path)):
            print("Le fichier existe")
            return 1
        else:
            print("Le fichier n'existe pas")
            return 0
    
    def afficherVictoires(self):
        with open(self.file_path) as fichier:
            data = json.load(fichier)
            for element in data:
                print("Le joueur", element["Nom"], "a fait", element["NombreVictoires"], "victoires")
    
    
    def ecrireJson(self):
        nombrePif = random.randint(0,1)
        i = 1
        print(nombrePif)
        try:
            
            with open(self.file_path) as fichier:
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
        except:
            print("Le fichier n'existe pas")

        with open(self.file_path, "w") as fichier:
            json.dump(test, fichier)

    def compter_battus(self):
        with open(self.file_path) as fichier:
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
            
    def ecrireJoueurs(self):
        with open(self.file_path, "r+") as fichier:
            contenu = fichier.read()
            print("Le contenu \n\n", contenu, "\n\n")
            data = json.loads(contenu)
            nom = input("Entrez votre nom : ")
            nouveauxJoueurs = {"Nom": nom, "NombreVictoires": 0, "JoueursBattus": [], "NombreDefaites": 0}
            fichier.truncate(0)
            fichier.seek(0)
            data.append(nouveauxJoueurs)
            json.dump(data, fichier)
            
    def victoireDynamique(self):
        with open(self.file_path, "r+") as fichier:
            data = json.load(fichier)
            nombrePif = random.randint(0, len(data))
            nombreDefaite = random.randint(0, len(data))
            for i in range(0, len(data)):
                print(data[i]["Nom"])
                if(nombrePif == i):
                    data[i]["NombreVictoires"] += 1
                    print("Le joueur ", data[i]["Nom"], "est vainqueur. Il a fait", data[i]["NombreVictoires"], "victoires")
                    nomVainqueur = data[i]["Nom"]
            for j in range(0, len(data)):
                if(nombreDefaite == j):
                    data[j]["NombreDefaites"] += 1
                    print("Le joueur", data[j]["Nom"], "a ete battu par", nomVainqueur)
                    nomPerdant = data[j]["Nom"]
            for i in range(0, len(data)):
                if(nomVainqueur == data[i]["Nom"]):
                    data[i]["JoueursBattus"] += [nomPerdant]
                           
            print("La longueur de data est ",len(data), "et la valeur du chiffre random est ", nombrePif)
            fichier.truncate(0)
            fichier.seek(0)
            json.dump(data, fichier)
            
    def testerJson(self):
        try:
            with open(self.file_path) as fichier:
                data = json.load(fichier)
                return 1
        except:
            return 0
        
                

joueurs = Joueurs("nom", 0, "joueursBattus", True)

if (joueurs.testerJson() == 0):
    print("Le fichier n'existe pas")
else:
    #joueurs.afficherVictoires()
    #joueurs.compter_battus()
    #joueurs.ecrireJson()
    #joueurs.ecrireJoueurs()
    joueurs.victoireDynamique()
    
    

#joueurs.ecrireJoueurs()
#joueurs.afficherVictoires()
#Joueurs.compter_battus()
#joueurs.ecrireJson()