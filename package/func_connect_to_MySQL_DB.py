import mysql.connector
import time
from mysql.connector import Error

def insertToTableForUsers(warning,usersConcerned,sizeExceeded):

	try:
		connection = mysql.connector.connect(host='localhost', database='projet6', user='root', password='toor', use_pure=True)
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
		print("Erreur de paramètres: {}".format(error))

	finally:
		# closing database connection.
		if (connection.is_connected()):
			cursor.close()
			connection.close()

def insertToTableForSharedFolder(totalSizeUsed):

	try:
		connection = mysql.connector.connect(host='localhost', database='projet6', user='root', password='toor', use_pure=True)
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
		print("Erreur de paramètres: {}".format(error))

	finally:
		# closing database connection.
		if (connection.is_connected()):
			cursor.close()
			connection.close()