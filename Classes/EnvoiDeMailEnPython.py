"""
import smtplib

sender_email = "childerikdegascogne@gmail.com"
receiver_email = "nathan.gouarderes@hotmail.fr  "
password = "Nathangou247"
message = "Subject: Test Mail\n\nThis is a test email sent using Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
"""
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.example.com",465)
#Ensuite, connectez-vous au serveur Gmail
server.login("childerikdegascogne@mail.com", "Nathangou247")
#Le message à envoyer
msg = "Hello!" 
#Envoyez le mail
server.sendmail("childerikdegascogne@mail.com", "nathan.gouarderes@hotmail.fr", msg)
server.quit()