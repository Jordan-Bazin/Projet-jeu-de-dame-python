import smtplib
from email.mime.text import MIMEText

email_address = "childerikdegascogne@gmail.com"
email_password = "Nathangou247"
to_email = "childerikdegascogne@gmail.com"
subject = "Subject Line"
email_text = "This is the body of the email."

msg = MIMEText(email_text)
msg["Subject"] = subject
msg["From"] = email_address
msg["To"] = to_email

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_address, email_password)
    smtp.send_message(msg)