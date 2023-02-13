from Classes.Plateau import Plateau
from Classes.Joueur import Joueur
import copy
import menu

if __name__ == '__main__':
    #menu.menu()
    p2 = Plateau(2,2)
    #p2.savePlateau(1)
    
    joueur1 = Joueur("Joueur 1", "O")
    joueur2 = Joueur("Joueur 2", "X")
      
    test = p2.verifierManger(joueur2)
    if(test != []):
        print(test)
        p2.afficherPlateau()
        p2.manger(4,2,2,4)
        p2.afficherPlateau()
    else:
        p2.afficherPlateau()
        print("Choisir un pion à déplacer")
        x, y = input("Entrer les coordonnées de départ du pion à déplacer : ").split()
        nouveauX, nouveauY =  input("Entrer les coordonées d'arriver du pion séléectionné : ").split()
        p2.bougerPion(joueur2,int(x)-1, int(y)-1, int(nouveauX)-1, int(nouveauY)-1)
        p2.afficherPlateau()


    