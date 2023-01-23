import sys
import os
from Classes.Plateau import Plateau


#Création d'un menu
def menu():
    
    print("Bienvenue dans le jeu de dame")
    
    print("Tapez 1 pour lancer une nouvelle partie")
    print("Tapez 2 pour lancer une ancienne partie")
    print("Tapez 3 pour envoyer le tableau des scores par mail")
    print("Tapez 4 pour quitter le jeu")
    choix = input("Votre choix : ")
    match choix:
        case "1":
            get_new_game()
        case "2":
            get_old_game()
        case "3":
            send_mail()
        case "4":
            leave_game()


def get_new_game():
    print("Nouvelle partie")
    Plateau

def get_old_game():
    print("Ancienne partie")

def send_mail():
    print("A quel adresse voulez-vous envoyer le tableau des scores ?")

def leave_game():
    #Appeler la fonction pour sauvegarder s'il le veut 
    menu()


menu()