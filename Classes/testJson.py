import json
from CreerJsonJoueurs import Joueurs

#test la fonction ecrireJson() du fichier CreerJsonJoueurs.py en verifiant que le fichier TableauJoueurs.json a bien ete modifie

def test_ecrireJson():
    
    expected_output = "Les joueurs battus par Bob sont : "
    
    result = Joueurs.ecrireJson()
    
    assert result == expected_output

#test la fonction compter_battus() du fichier CreerJsonJoueurs.py en verifiant que le dictionnaire dicJoueursBattus contient bien le bon nombre de joueurs battus par Bob

def test_compter_battus():
    
    expected_output = {'Gohrien': 1}
    
    result = Joueurs.compter_battus()
    
    assert result == expected_output

def test_afficherVictoires():
    
    expected_output = "Bob a gagne 1 fois"
    
    result = Joueurs.afficherVictoires()
    
    assert result == expected_output