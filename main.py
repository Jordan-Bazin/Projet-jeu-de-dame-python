from Classes.Plateau import Plateau
from Classes.Joueur import Joueur
import copy

if __name__ == '__main__':
    p2 = Plateau(2,2)
    #p2.savePlateau(1)

    joueur1 = Joueur("Joueur 1", "O", "8")
    joueur2 = Joueur("Joueur 2", "X", "%")
    #bouger un pion    
    test = p2.verifierManger(joueur1)
    if(test != []):
        print(test)
    p2.afficherPlateau()
    print(p2.listeCopiePlateau)


    