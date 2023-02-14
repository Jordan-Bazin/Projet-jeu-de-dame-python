import sys
import os
from Classes.Plateau import Plateau
from Classes.JsonManager import JsonManager 
import re
import json
import logging
import config_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from Classes.Plateau import Plateau
from Classes.Joueur import Joueur
from Classes.CreerJsonJoueurs import Score




def menu():
    logging.basicConfig(filename='game_logs.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Menu function: Welcome to the checkers game')
    print("Bienvenue dans le jeu de dame")
    while True:
        print("Tapez 1 pour lancer une nouvelle partie")
        print("Tapez 2 pour lancer une ancienne partie")
        print("Tapez 3 pour envoyer le tableau des scores par mail")
        print("Tapez 4 pour envoyer le tableau des scores par mail")
        print("Tapez 5 pour quitter le jeu sans sauvergarder")
        try:
            choix = int(input("Votre choix : "))
            if choix==1:
                get_new_game()
            elif choix==2:
                get_old_game()
            elif choix==3:
                send_json_email()
            elif choix==4:
                tableauScore()
            elif choix==5:
                logging.info('Menu function: Quitting the game')
                print("Merci d'avoir joué, à bientôt !")
                sys.exit()
            else:
                print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
                logging.error('Menu function: choix invalide')
        except ValueError:
            print("Choix non valide, veuillez saisir un nombre entre 1 et 4")
            logging.error('Menu function: choix invalide')

def tableauScore():
    logging.info("Tableau des scores")
    score = Score()

def send_json_email():
    # Ouvrir et charger le fichier JSON
    try:
        with open("json.json", 'r') as f:
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
    json_attachment.add_header('Content-Disposition', 'attachment', filename="Tableau des scores")
    msg.attach(json_attachment)

    # Envoyer l'email
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(source, password)
        smtp.sendmail(source, recipient_email, msg.as_string())
        print("E-mail envoyé avec succès!")
        print("\n")
        print("Retour au menu")
    except smtplib.SMTPException as e:
        print("Echec de l'envoi de l'e-mail :", e)

def get_old_game():
    logging.info("Ancienne partie")
    print("Quelle partie voulez-vous charger ? Donnez l'id de la partie")
    id = int(input("ID : "))
    plateau = Plateau(2,id)
    jouer(plateau)

def get_new_game():
    logging.info("Nouvelle partie")
    plateau = Plateau(1)
    jouer(plateau)

def jouer(plateau):
    print("")
    if(plateau.joueur1.tour == True):
        if(plateau.checkDefaite(plateau.joueur1)):
            print("Fin de la partie, "+plateau.joueur2.nom+" a gagné !")
            plateau.savePlateau(plateau.joueur2.nom) # le 4e argument est le joueur qui a gagné
            return 0
        print("Tour de " + plateau.joueur1.nom + ", il joue avec les "+plateau.joueur1.pion)
    else:
        if(plateau.checkDefaite(plateau.joueur2)):
            print("Fin de la partie, "+plateau.joueur1.nom+" a gagné !")
            plateau.savePlateau(plateau.joueur1.nom)
            return 0
        print("Tour de " + plateau.joueur2.nom + ", il joue avec les "+plateau.joueur2.pion)

    print("Taper 1 pour jouer votre tour")
    print("Taper 2 pour quitter et enregistrer la partie")
    print("Taper 3 pour abandonner la partie")
    print("Taper 4 pour revenir au menu")
    choix = int(input("Votre choix : "))
    if(choix == 1):
        jouer_tour(plateau)
    elif(choix == 2):
        plateau.savePlateau()
        return 0
    elif(choix == 3):
        if(plateau.joueur1.tour == True):
            plateau.savePlateau(plateau.joueur2.nom)
        else:
            plateau.savePlateau(plateau.joueur1.nom)
    elif(choix == 4):
        return 0
    else:
        print("Choix non valide, veuillez saisir un nombre entre 1 et 3")
        logging.error('Menu function: choix invalide')
        jouer(plateau)

def jouer_tour(plateau):
    if(plateau.joueur1.tour == True):
        joueur = plateau.joueur1
        plateau.joueur1.tour = False
        plateau.joueur2.tour = True
    else:
        joueur = plateau.joueur2
        plateau.joueur1.tour = True
        plateau.joueur2.tour = False

    listePionAManger = plateau.verifierManger(joueur)
    if(listePionAManger != []):
        plateau.afficherPlateau()
        x, y = input("Entrer les coordonnées de départ du pion à déplacer : ").split()
        nouveauX, nouveauY =  input("Entrer les coordonées d'arriver du pion sélectionné : ").split()
        plateau.manger(int(x)-1, int(y)-1, int(nouveauX)-1, int(nouveauY)-1)
        plateau.afficherPlateau()
        jouer(plateau)
    else:
        plateau.afficherPlateau()
        print("Vous ne pouvez pas manger, vous devez donc déplacer un pion")
        x, y = input("Entrer les coordonnées de départ du pion à déplacer : ").split()
        nouveauX, nouveauY =  input("Entrer les coordonées d'arriver du pion sélectionné : ").split()
        plateau.bougerPion(joueur,int(x)-1, int(y)-1, int(nouveauX)-1, int(nouveauY)-1)
        plateau.afficherPlateau()
        jouer(plateau)            

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





