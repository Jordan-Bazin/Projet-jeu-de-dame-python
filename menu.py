import sys
import os
from Classes.Plateau import Plateau

import re
import logging

def menu():
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Menu function: Welcome to the checkers game')
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
                logging.error('Menu function: Invalid choice, a number between 1 and 4 must be entered')
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
            logging.error('Menu function: Invalid choice, a number between 1 and 4 must be entered')


def send_mail():
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    try:
        mail = input("A quel adresse voulez-vous envoyer le tableau des scores ? ")
        valid_email(mail)
        # send mail
        logging.info('Send mail function: Mail sent to ' + mail)
        
    except ValueError:
        print("Adresse mail non valide, veuillez saisir une adresse mail valide")
        logging.error("Send mail function: Invalid email address, a valid email address must be entered")
        

def get_old_game(id):
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    try:
        Plateau #blabla
    except FileNotFoundError:
        print("Fichier non trouvé, veuillez saisir un nom de fichier valide")
        logging.error("Get old game function: File not found, a valid file name must be entered")
    except:
        print("Une erreur s'est produite lors de l'ouverture du fichier")
        logging.error("Get old game function: Error opening file")


def get_old_game(id):
    try:
        Plateau #blabla
    except FileNotFoundError:
        logging.error("Fichier non trouvé, veuillez saisir un nom de fichier valide")
    except:
        logging.error("Une erreur s'est produite lors de l'ouverture du fichier")

def get_new_game():
    logging.info("Nouvelle partie")
Plateau

def leave_game():
    logging.info("Bienvenue dans le jeu de dame")
    while True:
        logging.info("Tapez 1 pour sauvegarder la partie puis quitter le jeu")
        logging.info("Tapez 2 pour quitter le jeu sans sauvegarder")
        try:
            choix = int(input("Votre choix : "))
            if choix==1:
                #creation nouveau fichier où sauvegarder la partie
                menu() #quitter le jeu - retour au menu
            elif choix==2: #pas de sauvegarde
                menu()
            else:
                logging.error("Choix non valide")
        except ValueError:
            logging.error("Choix non valide, veuillez saisir un nombre entre 1 et 2")
            logging.info("Vous avez quitter le jeu")



def valid_email(email):
    try:
        # Utilise une expression régulière pour vérifier le format de l'adresse e-mail
        pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$")
        if pattern.match(email) == None:
            raise Exception("Format d'adresse e-mail non valide")
        return True
    except Exception as e:
        logging.error(e)
    return e






