from Classes.Plateau import Plateau

if __name__ == '__main__':
    p2 = Plateau(2,2)
    p2.afficherPlateau()
    #p2.savePlateau(1)
    p2.bougerPion(3,0,4,1)
    print(" ")
    p2.afficherPlateau()