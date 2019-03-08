import smtplib, ssl

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_SMTP_informations

	"""
	Returns 4 values: MY_ADDRESS, PASSWORD, SMTP_ADDRESS and SMTP_PORT containing the identifiers and address for sending mail
	read from filename
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
		print ("Error: cannot get in SMTPinformations.txt.")

def get_contacts(filename):
	"""
	Return two lists names, emails containing names and email addresses
	read from a file specified by filename.
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
		print ("Error: cannot get contacts in contacts.txt.")

def read_template(filename):
	"""
	Returns a Template object comprising the contents of the 
	file specified by filename.
	"""
	
	with open(filename, 'r', encoding='utf-8') as template_file:
		template_file_content = template_file.read()
	return Template(template_file_content)

def sendMail():

	try:
		# get informations from txt files to send email
		MY_ADDRESS, PASSWORD, SMTP_ADDRESS, SMTP_PORT = get_SMTP_informations('SMTPinformations.txt') # read SMTP informations
		names, emails = get_contacts('mycontacts.txt') # read contacts
		message_template = read_template('message.txt')

		# set up the SMTP server
		context = ssl.create_default_context()
		s = smtplib.SMTP_SSL(host=SMTP_ADDRESS, port=SMTP_PORT, context=context)
	   # s.starttls()
		s.login(MY_ADDRESS, PASSWORD)

		# For each contact, send the email:
		for name, email in zip(names, emails):
			msg = MIMEMultipart()       # create a message

			# add in the actual person name to the message template
			message = message_template.substitute(PERSON_NAME=name.title())

			# Prints out the message body for our sake
			print(message)

			# setup the parameters of the message
			msg['From']=MY_ADDRESS
			msg['To']=email
			msg['Subject']="This is TEST"
			
			# add in the message body
			msg.attach(MIMEText(message, 'plain'))
			
			# send the message via the server set up earlier.
			s.send_message(msg)
			del msg
			
		# Terminate the SMTP session and close the connection
		s.quit()
	except IOError:
		print ("Error: sopmething is wrong with sendMail function.")
	
if __name__ == '__sendMail__':
	sendMail()