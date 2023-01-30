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

def menu():
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Menu function: Welcome to the checkers game')
    print("Bienvenue dans le jeu de dame")
    while True:
        print("Tapez 1 pour lancer une nouvelle partie")
        print("Tapez 2 pour lancer une ancienne partie")
        print("Tapez 3 pour envoyer le tableau des scores par mail")
        print("Tapez 4 pour sauvegarder/quitter le jeu")
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
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    try:
        Plateau #blabla
    except FileNotFoundError:
        print("Fichier non trouvé, veuillez saisir un nom de fichier valide")
        logging.error("Fichier non trouvé, veuillez saisir un nom de fichier valide")
    except:
        print("Une erreur s'est produite lors de l'ouverture du fichier")
        logging.error("Fichier non trouvé, veuillez saisir un nom de fichier valide")




def get_old_game(id):
    logging.info("Ancienne partie")
    print("Quelle partie voulez-vous charger ? Donnez l'id de la partie")
    choix = input("Votre choix : ")
    try:
        #Lancement de la partie avec le bon id
        Plateau #blabla
    except FileNotFoundError:
        print("Fichier non trouvé, veuillez saisir un nom de fichier valide")
        logging.error("Fichier non trouvé")




def get_new_game():
    logging.info("Nouvelle partie")
    try:
        Plateau #blabla
    except FileNotFoundError:
        logging.error("Fichier non trouvé, veuillez saisir un nom de fichier valide")
    except:
        logging.error("Une erreur s'est produite lors de l'ouverture du fichier")





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






