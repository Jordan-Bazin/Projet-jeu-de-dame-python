from Classes.Plateau import Plateau
from Classes.Joueur import Joueur
import copy

if __name__ == '__main__':
    p2 = Plateau(2,2)
    #p2.savePlateau(1)

    joueur1 = Joueur("Joueur 1", "O", "8")
    joueur2 = Joueur("Joueur 2", "X", "%")
    #bouger un pion    
    test = p2.verifierManger(joueur2)
    print(test)
    p2.afficherPlateau()

    res = []
    [res.append(x) for x in p2.listeCopiePlateau if x not in res] # suppression des doublons dans la liste des coordonnées de départ des pions qui peuvent manger    

    # voir comment matcher les plateaux modifiés avec les coordonnées de départ et d'arriver des pions qui peuvent manger
    