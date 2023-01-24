from Classes.JsonManager import JsonManager

class Plateau ():
    def __init__(self, choix, idPartie = 0):
        self.json = JsonManager("Data/Parties.json")
        self.parties = self.json.getData()
        print(self.parties)
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
                        partie['tour'] = joueur1.getNom()
                    else:
                        partie['tour'] = joueur2.getNom()
            self.json.save(self.parties)

    # Déplace un pion sur le plateau et met la case d'origine à vide
    def bougerPion(self, x, y, nouvelleX, nouvelleY):
        try:
            if(self.plateau[x][y] == " "):
                raise Exception("La case d'origine est vide")
            self.plateau[nouvelleX][nouvelleY] = self.plateau[x][y]
            self.plateau[x][y] = " "
        except Exception as e:
            print(e)
            
        
            


    

    


        
                
        