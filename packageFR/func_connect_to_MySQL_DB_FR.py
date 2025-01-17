import mysql.connector
import time
from mysql.connector import Error

def getConnectionParameters(filename):

	try:
		# ouvre notre fichier filename et récupère les informations de la première ligne séparées par un espace
		with open(filename, mode='r', encoding='utf-8') as database_file:
			for parameters in database_file:
				host = parameters.split()[0]
				database = parameters.split()[1]
				user = parameters.split()[2]
				password = parameters.split()[3]
		return host, database, user, password

	except IOError:
		#erreur sys.exit (1)
		sys.exit("Erreur: impossible d'accéder à databaseParameters.txt.")


def insertToTableForUsers(warning,usersConcerned,sizeExceeded):

	try:
		#on récupère les informations de connexion à notre BDD dans notre fichier databaseParameters.txt
		host, database, user, password = getConnectionParameters('databaseParameters.txt')
		#on initie la connexion
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password, use_pure=True)
		cursor = connection.cursor(prepared=True)

		#on prépare notre requête en spécifiant des %s comme value, ce qui va nous permettre d'insérer nos variables peu après
		sql_insert_query = """ INSERT INTO `datafromusers` (`warning`,`usersConcerned`,`sizeExceeded`) VALUES (%s,%s,%s)"""
		#on prépare l'insertion de nos valeurs
		insert_tuple = (warning,usersConcerned,sizeExceeded)
		#on exécute le resultat de la query avec les valeurs du script
		result = cursor.execute(sql_insert_query, insert_tuple)
		#on commit les données
		connection.commit()
		print("Les données ont bien étées enregistrées dans la base de données.")

	except mysql.connector.Error as error:
		connection.rollback()

		#erreur sys.exit (1)
		sys.exit("Erreur de paramètres: {}".format(error))

	finally:

		# on ferme la connexion
		if (connection.is_connected()):
			cursor.close()
			connection.close()

def insertToTableForSharedFolder(totalSizeUsed):

	try:
		host, database, user, password = getConnectionParameters('databaseParameters.txt')
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password, use_pure=True)
		cursor = connection.cursor(prepared=True)
		#on prépare notre requête en spécifiant des %s comme value, ce qui va nous permettre d'insérer nos variables peu après
		sql_insert_query = """ INSERT INTO `sizesharedfolder` (`Size`) VALUES (%s)"""
		#on prépare l'insertion de nos valeurs
		insert_tuple = (totalSizeUsed,)
		#on exécute le resultat de la query avec les valeurs du script
		result = cursor.execute(sql_insert_query, insert_tuple)
		#on commit les données
		connection.commit()
		print("Les données ont bien étées enregistrées dans la base de données.")

	except mysql.connector.Error as error:
		connection.rollback()

		#erreur sys.exit (1)
		sys.exit("Erreur de paramètres: {}".format(error))

	finally:
		# on ferme la connexion
		if (connection.is_connected()):
			cursor.close()
			connection.close()