class Joueur:
    def __init__(self, nom, pion):
        self.nom = nom
        self.pion = pion
        if(pion == "X"):
            self.dame = "%"
            self.tour = False
        else:
            self.dame = "8"
            self.tour = True
        