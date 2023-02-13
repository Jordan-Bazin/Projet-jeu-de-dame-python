import sys
import os
from Classes.Plateau import Plateau
from Classes.JsonManager import JsonManager 
import re
import logging
import config_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from Classes.Plateau import Plateau
from Classes.Joueur import Joueur




def menu():
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Menu function: Welcome to the checkers game')
    print("Bienvenue dans le jeu de dame")
    while True:
        print("Tapez 1 pour lancer une nouvelle partie")
        print("Tapez 2 pour lancer une ancienne partie")
        print("Tapez 3 pour envoyer le tableau des scores par mail")
        try:
            choix = int(input("Votre choix : "))
            if choix==1:
                get_new_game()
            elif choix==2:
                get_old_game()
            elif choix==3:
                send_mail()
            else:
                print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
                logging.error('Menu function: choix invalide')
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
            logging.error('Menu function: choix invalide')


#A tester - pas encore fonctionnel
def read_file_content(file_path):
    json_manager = JsonManager(file_path)
    return json_manager.getData()

def send_mail(mail_destinataire, sujet="Tableau des scores", message=""):
    read_file_content()
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = config_email.config_email
    multipart_message["To"] = mail_destinataire

    multipart_message.attach(MIMEText(message, "plain"))

    serveur_mail = smtplib.SMTP(
        config_email.config_server, config_email.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(config_email.config_email, config_email.config_password)
    serveur_mail.sendmail(config_email.config_email,
                          mail_destinataire, multipart_message.as_string())
    serveur_mail.quit()


def get_old_game(id):
    logging.info("Ancienne partie")
    print("Quelle partie voulez-vous charger ? Donnez l'id de la partie")
    choix = input("ID : ")
    plateau = Plateau(2,id)
    jouer(plateau)

def get_new_game():
    logging.info("Nouvelle partie")
    plateau = Plateau(1)
    joueur1 = input("Entrer le nom du premier joueur :")
    joueur2 = input("Entrer le nom du deuxième joueur :")
    joueur1 = Joueur(joueur1, "X")
    joueur2 = Joueur(joueur2, "O")
    jouer(plateau, joueur1, joueur2)

def jouer(plateau, joueur1, joueur2):
    print("")
    if(joueur1.tour == True):
        print("Tour de " + joueur1.nom + ", il joue avec les "+joueur1.pion)
    else:
        print("Tour de " + joueur2.nom + ", il joue avec les "+joueur2.pion)
    print("Taper 1 pour jouer votre tour")
    print("Taper 2 pour quitter et enregistrer la partie")
    print("Taper 3 pour abandonner la partie")
    choix = int(input("Votre choix : "))
    if(choix == 1):
        jouer_tour(plateau, joueur1, joueur2)
    elif(choix == 2):
        plateau.savePlateau(joueur1, joueur2)
        return 0
    elif(choix == 3):
        if(joueur1.tour == True):
            plateau.savePlateau(joueur1, joueur2, joueur2.nom)
        else:
            plateau.savePlateau(joueur1, joueur2, joueur1.nom)
    else:
        print("Choix non valide, veuillez saisir un nombre entre 1 et 3")
        logging.error('Menu function: choix invalide')
        jouer(plateau, joueur1, joueur2)

def jouer_tour(plateau, joueur1, joueur2):
    if(joueur1.tour == True):
        if(plateau.checkDefaite(joueur1)):
            print("Fin de la partie, "+joueur2.nom+" a gagné !")
            plateau.savePlateau(plateau, joueur1, joueur2, joueur2) # le 4e argument est le joueur qui a gagné
            return 0
        joueur = joueur1
        joueur1.tour = False
        joueur2.tour = True
    else:
        if(plateau.checkDefaite(joueur2)):
            print("Fin de la partie, "+joueur1.nom+" a gagné !")
            plateau.savePlateau(plateau, joueur1, joueur2, joueur1)
            return 0
        joueur = joueur2
        joueur1.tour = True
        joueur2.tour = False

    listePionAManger = plateau.verifierManger(joueur)
    if(listePionAManger != []):
        plateau.afficherPlateau()
        x, y = input("Entrer les coordonnées de départ du pion à déplacer : ").split()
        nouveauX, nouveauY =  input("Entrer les coordonées d'arriver du pion séléectionné : ").split()
        plateau.manger(int(x)-1, int(y)-1, int(nouveauX)-1, int(nouveauY)-1)
        plateau.afficherPlateau()
        jouer(plateau, joueur1, joueur2)
    else:
        plateau.afficherPlateau()
        print("Vous ne pouvez pas manger, vous devez donc déplacer un pion")
        x, y = input("Entrer les coordonnées de départ du pion à déplacer : ").split()
        nouveauX, nouveauY =  input("Entrer les coordonées d'arriver du pion séléectionné : ").split()
        plateau.bougerPion(joueur,int(x)-1, int(y)-1, int(nouveauX)-1, int(nouveauY)-1)
        plateau.afficherPlateau()
        jouer(plateau, joueur1, joueur2)


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
                exit()
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

def finPartie(plateau, joueur):
    print("Fin de la partie, "+joueur.nom+" a gagné !")
    





