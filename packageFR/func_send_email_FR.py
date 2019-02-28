import smtplib, ssl

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'YOUREMAILHERE'
PASSWORD = 'YOURPASSWORDHERE'

def get_contacts(filename):
    """
    Retourne 2 listes: names, emails contenant les noms et adresses email
    lu à partir de filename
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Retourne un objet Template object comprennant le contenu 
    du fichié spécifié par filename 
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def sendMail():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # Mise en place des informations SMTP
    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port='465', context=context)
    s.login(MY_ADDRESS, PASSWORD)

    # Pour chaque contact dans le fichier mycontacts.txt, envoie un mail
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # créer un message vide

        # ajouter le nom de la personne actuelle (dansla boucle) au modèle du message
        message = message_template.substitute(PERSON_NAME=name.title())

        # on écrit le message
        print(message)

        # les paramètres obligatoires pour un message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # on attache le texte
        msg.attach(MIMEText(message, 'plain'))
        
        # on envoie le message par la connexion SMTP configurée au préalable
        s.send_message(msg)
        del msg
        
    # On déconnecte la session SMTP et on quitte.
    s.quit()
    
if __name__ == '__sendMail__':
    sendMail()