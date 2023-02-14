import json
import random
import os
from Classes.JsonManager import JsonManager

class Score:
    #absolute_path = os.path.dirname(os.path.abspath(__file__))
    #absolutePathParties = os.path.dirname(os.path.abspath(__file__))
    #filePathParties = 'Data\Parties.json'
    #file_path = absolute_path + '\TableauJoueurs.json'
    
    def __init__(self, nom, pion):
        self.jsonData = JsonManager('Data/Parties.json')
        self.parties = self.jsonData.data
        
    def score(self):
        print("aled")

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
        
        
    def afficherPartiesJson(self):
        with open(self.filePathParties) as fichier:
            data = json.load(fichier)
            for element in data:
                vainquer = element["Vainqueur"]
                tableau = element
                idPartie = element["idPartie"]
                joueur1 = element["Joueur1"]
                joueur2 = element["Joueur2"]
                print(vainquer)
            print("\n\n Le tableau de parties vaut : \n", tableau, "\n\n")
            print("\n l'id de la partie vaut : \n", idPartie, "\n\n")
            print("\n le joueur 1 vaut : \n", joueur1, "\n\n")
            print("\n le joueur 2 vaut : \n", joueur2, "\n\n")
            
    def getIdPartie(self):
        with open(self.filePathParties) as fichier:
            data = json.load(fichier)
            for element in data:
                idPartie = element["idPartie"]
            return idPartie
        
    def getJoueur1(self):
        with open(self.filePathParties) as fichier:
            data = json.load(fichier)
            for element in data:
                joueur1 = element["Joueur1"]
            return joueur1
        
    def getIdJoueur2(self):
        with open(self.filePathParties) as fichier:
            data = json.load(fichier)
            for element in data:
                joueur2 = element["Joueur2"]
            return joueur2
        
    def getVainqueur(self):
        with open(self.filePathParties) as fichier:
            data = json.load(fichier)
            for element in data:
                vainqueur = element["Vainqueur"]
            return vainqueur
                
    def tableauScore(self):
        for partie in self.jsonData:
            print(partie)
            #joueurs.afficherVictoires()
            #joueurs.compter_battus()
            #joueurs.ecrireJson()
            #joueurs.ecrireJoueurs()
            #joueurs.victoireDynamique()

#joueurs = Joueurs("nom", "x")

#if (joueurs.testerJson() == 0):
    #print("Le fichier n'existe pas")
#else:
    #joueurs.afficherVictoires()
    #joueurs.compter_battus()
    #joueurs.ecrireJson()
    #joueurs.ecrireJoueurs()
    #joueurs.victoireDynamique()
    #joueurs.afficherPartiesJson()
    #print(joueurs.getIdPartie())
    #print(joueurs.getJoueur1())
    #print(joueurs.getIdJoueur2())
    #print(joueurs.getVainqueur())
    #print("Le fichier existe")
    