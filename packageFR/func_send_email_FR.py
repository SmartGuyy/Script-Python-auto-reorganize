import smtplib, ssl

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_SMTP_informations

	"""
	Retourne 4 valeurs: MY_ADDRESS, PASSWORD, SMTP_ADDRESS et SMTP_PORT contenant les identifiants et adresse pour l'envoi de mail
	lu à partir de filename
	"""
	try:

		with open(filename, mode='r', encoding='utf-8') as SMTP_file:
			for parameter in SMTP_file:
				MY_ADDRESS = parameter.split()[0]
				PASSWORD = parameter.split()[1]
				SMTP_ADDRESS = parameter.split()[2]
				SMTP_PORT = parameter.split()[3]
		return MY_ADDRESS, PASSWORD, SMTP_ADDRESS, SMTP_PORT

	except IOError:
		print ("Erreur: impossible d'accéder à SMTPinformations.txt.")

def get_contacts(filename):
	"""
	Retourne 2 listes: names, emails contenant les noms et adresses email
	lu à partir de filename
	"""
	try:

		names = []
		emails = []
		with open(filename, mode='r', encoding='utf-8') as contacts_file:
			for a_contact in contacts_file:
				names.append(a_contact.split()[0])
				emails.append(a_contact.split()[1])
		return names, emails

	except IOError:
		print ("Erreur: impossible d'accéder à contacts.txt.")

def read_template(filename):
	"""
	Retourne un objet Template object comprennant le contenu 
	du fichié spécifié par filename 
	"""
	
	with open(filename, 'r', encoding='utf-8') as template_file:
		template_file_content = template_file.read()
	return Template(template_file_content)

def sendMail():

	try:
		# récupère les informations pour la connexion et l'envoi de mail par SMTP
		MY_ADDRESS, PASSWORD, SMTP_ADDRESS, SMTP_PORT = get_SMTP_informations('SMTPinformations.txt') # read SMTP informations
		names, emails = get_contacts('mycontacts.txt') # read contacts
		message_template = read_template('message.txt')

		# Mise en place des informations SMTP
		context = ssl.create_default_context()
		s = smtplib.SMTP_SSL(host=SMTP_ADDRESS, port=SMTP_PORT, context=context)
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
	except IOError:
		print ("Erreur: vérifiez vos informations SMTP ou le nom des fichiers.")
	
if __name__ == '__sendMail__':
	sendMail()