from Classes.JsonManager import JsonManager

class Plateau ():
    def __init__(self, choix, idPartie = 0):
        self.json = JsonManager("Data/Parties.json")
        self.parties = self.json.getData()

        if(choix == 1): # Création d'un nouveau plateau à partir du template à l'id 0
            self.enCours = False
            for partie in self.parties:
                if partie['idPartie'] == idPartie:
                    self.plateau = partie['Plateau']

        elif(choix == 2): #Génération du plateau à partir d'une partie existante
            self.enCours = True
            try:
                for partie in self.parties:
                    if partie['idPartie'] == idPartie:
                        if partie['Vainqueur'] != "": # Si la partie est terminée
                            raise Exception("La partie est déjà terminée")
                        self.plateau = partie['Plateau']
                #raise Exception("La partie n'existe pas, id introuvable") # Si l'id est introuvable
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
            jsonDataToSave = {
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

            self.parties.append(jsonDataToSave)
            self.json.save(self.parties)
            
        elif(self.enCours == True):  # Sauvegarde d'une partie existante
            for partie in self.parties:
                if partie['idPartie'] == self.idPartie:
                    partie['Plateau'] = self.plateau
                    partie['Vainqueur'] = vainqueur
                    if joueur1.getTour == True:
                        partie['tour'] = joueur1.nom
                    else:
                        partie['tour'] = joueur2.nom
            self.json.save(self.parties)
    
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
            elif(x != nouvelleX and y != nouvelleY):
                if(x < nouvelleX):
                    for i in range(x, nouvelleX):
                        if(self.plateau[i][y] != " "):
                            raise Exception("Il y a un pion sur le chemin")
                else:
                    for i in range(nouvelleX, x):
                        if(self.plateau[i][y] != " "):
                            raise Exception("Il y a un pion sur le chemin")
            elif(x == nouvelleX and y != nouvelleY):
                if(y < nouvelleY):
                    for i in range(y, nouvelleY):
                        if(self.plateau[x][i] != " "):
                            raise Exception("Il y a un pion sur le chemin")
                else:
                    for i in range(nouvelleY, y):
                        if(self.plateau[x][i] != " "):
                            raise Exception("Il y a un pion sur le chemin")
            elif(nouvelleX > len(self.plateau) or nouvelleY > len(self.plateau)):
                raise Exception("Vous ne pouvez pas déplacer votre pion en dehors du plateau")
            elif(self.plateau[nouvelleX][nouvelleY] == joueur.pion):
                raise Exception("La case d'arrivée est déjà occupée par votre pion")
        except Exception as e:
            print(e)
            return False
        return True

    # Vérifie si un pion peut mangé un autre pion
    def verifierManger(self, joueur):
        if(joueur.pion == "X"):
            pionAdeverse = "O"
        else:
            pionAdeverse = "X"
        listeAttaquePossible = []
        attaquePossible = [[0,0],0]
        try:
            for i in range(len(self.plateau) - 1):
                for j in range(len(self.plateau) - 1):
                    if(self.plateau[i][j] == joueur.pion):
                        if((i + 1 < 10 and j + 1 < 10) and (i + 2 < 10 and j + 2 < 10)): # verif deguelasse mais ça marche
                            if(self.plateau[i+1][j+1] == pionAdeverse and self.plateau[i+2][j+2] == " "):
                                attaquePossible = [[i+1, j+1], 1]
                                if((i + 3 < 10 and j + 3 < 10) and (i + 4 < 10 and j + 4 < 10)): # verif deguelasse mais ça marche
                                    if(self.plateau[i+3][j+3] == pionAdeverse and self.plateau[i+4][j+4] == " "):
                                        attaquePossible = [[3+1, j+3], 2]
                                        if((i + 5 < 10 and j + 5 < 10) and (i + 6 < 10 and j + 6 < 10)): # verif deguelasse mais ça marche
                                            if(self.plateau[i+5][j+5] == pionAdeverse and self.plateau[i+6][j+6] == " "):
                                                attaquePossible = [[i+5, j+5], 3]
                        listeAttaquePossible.append(attaquePossible)
        except Exception as e:
            print(e)
            return False
        return listeAttaquePossible
            
    # Déplace un pion sur le plateau et met la case d'origine à vide
    def bougerPion(self, joueur):
        coord = input("Choisissez une case à jouer: ")
        coord = coord.split(" ")
        x = int(coord[0]) + 1
        y = int(coord[1]) + 1
        
        if self.verifierDeplacement(joueur, x, y, x+1, y+1) == True:
            self.plateau[x+1][y+1] = self.plateau[x][y]
            self.plateau[x][y] = " "

            
        
            


    

    


        
                
        