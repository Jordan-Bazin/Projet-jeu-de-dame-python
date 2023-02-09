import sys
import os
from Classes.Plateau import Plateau
from Classes.JsonManager import JsonManager 
import re
import logging
import config_email
import smtplib
from email import encoders
from email.mime.base import MIMEBase
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



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
                send_json_email()
            elif choix==4:
                leave_game()
            elif choix==5:
                exit()
                
            else:
                print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
                logging.error('Menu function: choix invalide')
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
            logging.error('Menu function: choix invalide')







def get_old_game():
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


def send_json_email():
    # Ouvrir et charger le fichier JSON
    try:
        json_file = input("Quel nom de fichier ?")
        with open(json_file, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        return
    except json.JSONDecodeError:
        print("Le fichier n'est pas un fichier JSON valide.")
        return

    recipient_email = input("Entrez l'adresse mail du destinataire : ")

    # Construire le message email
    msg = MIMEMultipart()
    source = "childerikdegascogne@gmail.com"
    password = "trlxuhvuewfddheq"
    msg['From'] = source 
    msg['To'] = recipient_email
    msg['Subject'] = "Fictif"
    print(json_data)

    # Ajouter le contenu du fichier JSON au message
    json_attachment = MIMEApplication(json.dumps(json_data), _subtype='json')
    json_attachment.add_header('Content-Disposition', 'attachment', filename=json_file)
    msg.attach(json_attachment)

    # Envoyer l'email
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(source, password)
        smtp.sendmail(source, recipient_email, msg.as_string())
        print("E-mail envoyé avec succès!")
    except smtplib.SMTPException as e:
        print("Echec de l'envoi de l'e-mail :", e)


send_json_email()