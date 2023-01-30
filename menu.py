import sys
import os
from Classes.Plateau import Plateau
import re



def menu():
    print("Bienvenue dans le jeu de dame")
    while True:
        print("Tapez 1 pour lancer une nouvelle partie")
        print("Tapez 2 pour lancer une ancienne partie")
        print("Tapez 3 pour envoyer le tableau des scores par mail")
        print("Tapez 4 pour quitter le jeu")
        try:
            choix = int(input("Votre choix : "))
            if choix==1:
                get_new_game()
            elif choix==2:
                get_old_game()
            elif choix==3:
                send_mail()
            elif choix==4:
                leave_game()
                break
            else:
                print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 4")



def send_mail():
    try:
        mail = input("A quel adresse voulez-vous envoyer le tableau des scores ? ")
        valid_email(mail)
        # send mail
    except ValueError:
        print("Adresse mail non valide, veuillez saisir une adresse mail valide")
        
        
def get_old_game(id):
    try:
        Plateau = open("save.txt", "r")
    except FileNotFoundError:
        print("Fichier non trouvé, veuillez saisir un nom de fichier valide")
    except:
        print("Une erreur s'est produite lors de l'ouverture du fichier")


def get_new_game():
    print("Nouvelle partie")
    Plateau
    
def leave_game():
    print("Bienvenue dans le jeu de dame")
    while True:
        print("Tapez 1 pour sauvegarder la partie puis quitter le jeu")
        print("Tapez 2 pour quitter le jeu sans sauvegarder")
        try:
            choix = int(input("Votre choix : "))
            if choix==1:
                #creation nouveau fichier où sauvegarder la partie
                #quitter le jeu
                menu()
            elif choix==2:
                menu()
            else:
                print("Choix non valide, veuillez saisir un nombre entre 1 et 2")
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 2")
print("Vous avez quitter le jeu")   

def valid_email(email):
  try:
    # Utilise une expression régulière pour vérifier le format de l'adresse e-mail
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if pattern.match(email) == None:
      raise Exception("Format d'adresse e-mail non valide")
    return True
  except Exception as e:
    return e


menu()