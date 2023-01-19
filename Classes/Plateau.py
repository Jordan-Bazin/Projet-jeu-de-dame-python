from Classes.JsonManager import JsonManager

class Plateau ():
    def __init__(self, choix, idPartie = 0):
        if(choix == 1):
            self.plateau = [10*[0],10*[0],10*[0],10*[0],10*[0],10*[0],10*[0],10*[0],10*[0],10*[0]]
        elif(choix == 2):
            self.idPartie = idPartie
        else:
            print("Erreur")
            exit(1)

        self.json_manager = JsonManager("Data/Parties.json")
           
    def afficherPlateau(self):
        for i in range(0, 11): # Affichage les chiffres en haut
            print(str(i) + " | ", end="")
        print("\n")

        for i in range(1, 11):
            print(str(i) + " | ", end="") # Affichage les chiffres à gauche
            for j in range(0, 10):
                print(str(self.plateau[i-1][j]) + " | ", end="")
            print("\n")

    def getTableauFromJson(self):
        self.plateau = self.json_manager.getData()[0]['Plateau']
        print(self.plateau)
        self.afficherPlateau()

    

    


        
                
        