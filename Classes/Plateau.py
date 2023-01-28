from Classes.JsonManager import JsonManager
from Classes.Joueur import Joueur
from Classes.Colors import Colors

class Plateau ():
    def __init__(self, choix, idPartie = 0):
        self.json = JsonManager("Data/Parties.json") # objet json pour instancier avec le path du fichier json des parties 
        self.parties = self.json.getData() # Récupère les données des parties du fichier json
        self.plateau = [] # Tableau du plateau
        self.listePionManger = [] # Tableau des pions à manger

        if(choix == 1): # Création d'un nouveau plateau à partir du template à l'id 0
            self.enCours = False
            for partie in self.parties:
                if partie['idPartie'] == idPartie:
                    self.plateau = partie['Plateau']
            if(self.plateau == []):
                raise Exception("Le template à l'id 0 est introuvable")
        elif(choix == 2): #Génération du plateau à partir d'une partie existante
            self.enCours = True
            try:
                for partie in self.parties:
                    if partie['idPartie'] == idPartie: # Recherche de la partie à l'id indiqué
                        if partie['Vainqueur'] != "": # Si la partie est terminée
                            raise Exception("La partie est déjà terminée")
                        self.plateau = partie['Plateau']
                if(self.plateau == []):
                    raise Exception("La partie n'existe pas, id introuvable")
            except Exception as e:
                print(e)
                exit(1)
        else:
            print("Erreur")
            exit(1)
        self.idPartie = idPartie
           
    def afficherPlateau(self):
        for i in range(0, 11): # Affichage les chiffres en haut
            if(i == 10):
                print(str(i) + "| ")
            else:
                print(str(i) + " | ", end="")



        for i in range(1, 11):
            for k in range(0, 21): # Affichage des lignes du plateau
                print("--", end="")    
            print("\n", end="")
            if(i == 10):                        # Affichage les chiffres à gauche
                print(str(i) + "| ", end="")
            else:
                print(str(i) + " | ", end="")
            for j in range(0, 10):              # Affiche les cases du plateau
                if(j == 10):
                    print(str(self.plateau[i-1][j]) + " | ")
                else:
                    print(str(self.plateau[i-1][j]) + " | ", end="")
            print("\n", end="")


    def savePlateau(self,joueur1, joueur2, vainqueur = ""):
        if(self.enCours == False): # Sauvegarde d'une nouvelle partie               
            idPartie = len(self.parties) - 1
            jsonDataToSave = { # Dictionnaire temporaire pour sauvegarder les données
                "idPartie": idPartie,
                "Joueur1": joueur1.getNom(),
                "Joueur2": joueur2.getNom(),
                "Vainqueur": vainqueur,
                "Plateau": self.plateau
            }
            if joueur1.getTour == True:
                jsonDataToSave = {"Tour": joueur1.getNom()}
            else:
                jsonDataToSave = {"Tour" :joueur2.getNom()}

            self.parties.append(jsonDataToSave) # Ajout du dictionnaire temporaire dans la liste des parties
            self.json.save(self.parties) # Sauvegarde dans le fichier json
            
        elif(self.enCours == True):  # Sauvegarde d'une partie existante
            for partie in self.parties: # Remplace les valeurs changeantes dans le tableau des parties
                if partie['idPartie'] == self.idPartie:
                    partie['Plateau'] = self.plateau
                    partie['Vainqueur'] = vainqueur
                    if joueur1.getTour == True:
                        partie['tour'] = joueur1.nom
                    else:
                        partie['tour'] = joueur2.nom
            self.json.save(self.parties) # Sauvegarde dans le fichier json
    
    # Vérifie si le pion peut être déplacé
    def verifierDeplacement(self, joueur, x, y, nouvelleX, nouvelleY):
        try:
            if(self.plateau[x][y] == " "):
                raise Exception("La case d'origine est vide")
            elif(self.plateau[x][y] != joueur.pion):
                raise Exception("Ce n'est pas votre pion")
            elif(self.plateau[nouvelleX][nouvelleY] != " "):
                raise Exception("La case d'arrivée n'est pas vide")
            elif(x == nouvelleX and y == nouvelleY):
                raise Exception("Vous ne pouvez pas rester sur la même case")
            elif(x == nouvelleX or y == nouvelleY):
                raise Exception("Vous ne pouvez déplacer votre pion qu'en diagonale")
            elif(nouvelleX > len(self.plateau) or nouvelleY > len(self.plateau)):
                raise Exception("Vous ne pouvez pas déplacer votre pion en dehors du plateau")
        except Exception as e:
            print(e)
            return False
        return True

    def verifierMangerHaut(self, i, j, cpt = 0):
        pionAdverse = 'O'
        listeAttaquePossible = []
        attaquePossible = []

        if((i + 1 < 10 and j + 1 < 10) and (i + 2 < 10 and j + 2 < 10)): # verif deguelasse mais ça marche
            if(self.plateau[i+1][j+1] == pionAdverse and self.plateau[i+2][j+2] == " "): # verifie si on peut manger le pion en diagonale haut droite 
                attaquePossible = [[i, j], 2, "++"]
        if(attaquePossible != []):
            listeAttaquePossible.append(attaquePossible)
        attaquePossible = []
        if((i + 1 < 10 and j - 1 >= 0) and (i + 2 < 10 and j - 2 >= 0)): # verif deguelasse mais ça marche
            if(self.plateau[i+1][j-1] == pionAdverse and self.plateau[i+2][j-2] == " "): # verifie si on peut manger le pion en diagonale haut gauche 
                attaquePossible = [[i, j], 2, "+-"]
        if(attaquePossible != []):
            listeAttaquePossible.append(attaquePossible)
        attaquePossible = []
        
        if(listeAttaquePossible != []):
            listeCoordPossible = []
            if(listeAttaquePossible != []):
                for i in range(len(listeAttaquePossible)):
                    if(listeAttaquePossible[i][2] == "++"):
                        x = listeAttaquePossible[i][0][0]
                        y = listeAttaquePossible[i][0][1]
                        nouvelleX = listeAttaquePossible[i][0][0] + listeAttaquePossible[i][1]
                        nouvelleY = listeAttaquePossible[i][0][1] + listeAttaquePossible[i][1]
                        tab = [x, y, nouvelleX, nouvelleY]
                        listeCoordPossible.append(tab)
                    elif(listeAttaquePossible[i][2] == "+-"):
                        x = listeAttaquePossible[i][0][0]
                        y = listeAttaquePossible[i][0][1]
                        nouvelleX = listeAttaquePossible[i][0][0] + listeAttaquePossible[i][1]
                        nouvelleY = listeAttaquePossible[i][0][1] - listeAttaquePossible[i][1]
                        tab = [x, y, nouvelleX, nouvelleY]
                        listeCoordPossible.append(tab)
                    else: 
                        print("erreur")

            for coord in listeCoordPossible:
                test = self.verifierMangerHaut(coord[2], coord[3], cpt+1)
                if(test == None):
                    tmpTab = [coord[2],coord[3], cpt]
                    self.listePionManger.append(tmpTab)
                elif(cpt == 0):
                    return coord[0], coord[1]
            return coord[0], coord[1]
        else:
            return None

    def verifierMangerBas(self, i, j, cpt = 0):
        pionAdverse = 'X'
        listeAttaquePossible = []
        attaquePossible = []

        if((i - 1 >= 0 and j + 1 < 10) and (i - 2 >= 0 and j + 2 < 10)): # verif deguelasse mais ça marche
            if(self.plateau[i-1][j+1] == pionAdverse and self.plateau[i-2][j+2] == " "): # verifie si on peut manger le pion en diagonale bas droite 
                attaquePossible = [[i, j], 2, "-+"]
        if(attaquePossible != []):
            listeAttaquePossible.append(attaquePossible)
        attaquePossible = []
        if((i - 1 >= 0 and j - 1 >= 0) and (i - 2 >= 0 and j - 2 >= 0)): # verif deguelasse mais ça marche
            if(self.plateau[i-1][j-1] == pionAdverse and self.plateau[i-2][j-2] == " "): # verifie si on peut manger le pion en diagonale bas gauche
                attaquePossible = [[i, j], 2, "--"]         
        if(attaquePossible != []):
            listeAttaquePossible.append(attaquePossible)
        attaquePossible = []
        
        if(listeAttaquePossible != []):
            listeCoordPossible = []
            if(listeAttaquePossible != []):
                for i in range(len(listeAttaquePossible)):
                    if(listeAttaquePossible[i][2] == "--"):
                        x = listeAttaquePossible[i][0][0]
                        y = listeAttaquePossible[i][0][1]
                        nouvelleX = listeAttaquePossible[i][0][0] - listeAttaquePossible[i][1]
                        nouvelleY = listeAttaquePossible[i][0][1] - listeAttaquePossible[i][1]
                        tab = [x, y, nouvelleX, nouvelleY]
                        listeCoordPossible.append(tab)
                    elif(listeAttaquePossible[i][2] == "-+"):
                        x = listeAttaquePossible[i][0][0]
                        y = listeAttaquePossible[i][0][1]
                        nouvelleX = listeAttaquePossible[i][0][0] - listeAttaquePossible[i][1]
                        nouvelleY = listeAttaquePossible[i][0][1] + listeAttaquePossible[i][1]
                        tab = [x, y, nouvelleX, nouvelleY]
                        listeCoordPossible.append(tab)
                    else: 
                        print("erreur")
    
            for coord in listeCoordPossible:
                test = self.verifierMangerBas(coord[2], coord[3], cpt+1)
                if(test == None):
                    tmpTab = [coord[2],coord[3], cpt]
                    self.listePionManger.append(tmpTab)
                elif(cpt == 0):
                    return coord[0], coord[1]
            return True
        else:
            return None    

    # Vérifie si un pion peut mangé un autre pion
    def verifierManger(self, joueur):
        listeAttaquePossible = []
        baseCoord = []
        try:
            for i in range(len(self.plateau)):
                for j in range(len(self.plateau)): # pour chaque case du plateau on vérifie si un pion peut manger un ou plusieurs pions
                    if(self.plateau[i][j] == joueur.pion and (joueur.pion == "X" or (joueur.pion == "*" or joueur.pion == "@"))): # test pour les pions "O"
                        baseCoord.append(self.verifierMangerHaut(i, j)) # sauvegarde des coordonnées du pion qui peut manger pour la coloration
                        if(self.listePionManger != [] or self.listePionManger != None):
                            for coords in self.listePionManger:
                                listeAttaquePossible.append(coords) # sauvegarde des coordonnées destions des pions qui peuvent manger
                        self.listePionManger = []
                    if(self.plateau[i][j] == joueur.pion and (joueur.pion == "O" or (joueur.pion == "*" or joueur.pion == "@"))): # test pour les pions "X"
                        baseCoord.append(self.verifierMangerBas(i, j))
                        if(self.listePionManger != [] or self.listePionManger != None):
                            for coords in self.listePionManger:
                                listeAttaquePossible.append(coords)     
                        self.listePionManger = []
        except Exception as e:
            print(e)
            return False
        
        max = 0
        listeAttaquePlusForte = []
        for i in range(len(listeAttaquePossible)): # recherche de la liste d'attaque la plus forte
            if(listeAttaquePossible[i][2] == max): # Le nombre de pions mangés est le 3ème élément de la liste
                listeAttaquePlusForte.append(listeAttaquePossible[i])
            if(listeAttaquePossible[i][2] > max):
                listeAttaquePlusForte = []
                listeAttaquePlusForte.append(listeAttaquePossible[i])
                max = listeAttaquePossible[i][2]
         
        colors = Colors()
        for coord in listeAttaquePlusForte:
            self.plateau[coord[0]][coord[1]] = colors.FAIL + u"\u2588" + colors.ENDC # Coloration des zones destinations possibles
        for coord in baseCoord:
            if(coord != None):
                if(coord != True): # Je ne sais pas pourquoi mais je ne peux pas mettre un "or" pour tester si c'est à True donc je fais en 2 fois
                    print(coord)
                    self.plateau[coord[0]][coord[1]] = colors.FAIL + joueur.pion + colors.ENDC #coloration des pions qui peuvent manger
        return listeAttaquePlusForte
            
    # Déplace un pion sur le plateau et met la case d'origine à vide
    def bougerPion(self, joueur, x, y, nouvelleX, nouvelleY):        
        if self.verifierDeplacement(joueur, x, y, nouvelleX, nouvelleY) == True:
            self.plateau[nouvelleX][nouvelleY] = self.plateau[x][y]
            self.plateau[x][y] = " "

            
        
            


    

    


        
                
        