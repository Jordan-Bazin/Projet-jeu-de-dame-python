from Classes.Plateau import Plateau
from Classes.Joueur import Joueur

if __name__ == '__main__':
    p2 = Plateau(2,2)
    p2.afficherPlateau()
    #p2.savePlateau(1)

    joueur1 = Joueur("Joueur 1", "X")
    #bouger un pion    
    test = p2.verifierManger(joueur1)
    print(test)

    #p2.bougerPion(joueur1, 6, 1, 4, 1)
    #p2.afficherPlateau()