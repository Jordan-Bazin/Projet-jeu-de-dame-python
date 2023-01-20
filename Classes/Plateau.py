from Classes.JsonManager import JsonManager

class Plateau ():
    def __init__(self, choix, idPartie = 0):
        parties = JsonManager("Data/Parties.json").getData()
        if(choix == 1):
            for partie in parties:
                if partie['idPartie'] == idPartie:
                    self.plateau = partie['Plateau']
        elif(choix == 2):
            for partie in parties:
                if partie['idPartie'] == idPartie:
                    self.plateau = partie['Plateau']
        else:
            print("Erreur")
            exit(1)

        self.json_manager = JsonManager("Data/Parties.json")
           
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


    

    


        
                
        