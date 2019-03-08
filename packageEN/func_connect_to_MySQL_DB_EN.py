import mysql.connector
import time
from mysql.connector import Error

def getConnectionParameters(filename):

	try:
		# open file and get each value from first line (separated by a space)
		with open(filename, mode='r', encoding='utf-8') as database_file:
			for parameters in database_file:
				host = parameters.split()[0]
				database = parameters.split()[1]
				user = parameters.split()[2]
				password = parameters.split()[3]
		return host, database, user, password

	except IOError:
		print ("Erreur: impossible d'accéder à databaseParameters.txt.")


def insertToTableForUsers(warning,usersConcerned,sizeExceeded):

	try:
		# get information for database connexion in databaseParameters.txt
		host, database, user, password = getConnectionParameters('databaseParameters.txt')

		# initiating connexion to database and preparing to run query
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password, use_pure=True)
		cursor = connection.cursor(prepared=True)
		# preparing our query by specifying '%s' as value, which will allow us to insert our variables soon after
		sql_insert_query = """ INSERT INTO `datafromusers` (`warning`,`usersConcerned`,`sizeExceeded`) VALUES (%s,%s,%s)"""
		# preparing the insertion of our values
		insert_tuple = (warning,usersConcerned,sizeExceeded)
		# we run the result of the query with the values of the script
		result = cursor.execute(sql_insert_query, insert_tuple)
		# commit data
		connection.commit()
		print("All the data were correctly registered in database.")

	except mysql.connector.Error as error:
		connection.rollback()
		print("Error of parameters: {}".format(error))

	finally:
		# closing database connection.
		if (connection.is_connected()):
			cursor.close()
			connection.close()

def insertToTableForSharedFolder(totalSizeUsed):

	try:
		# get information for database connexion in databaseParameters.txt
		host, database, user, password = getConnectionParameters('databaseParameters.txt')
		
		# initiating connexion to database and preparing to run query
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password, use_pure=True)
		cursor = connection.cursor(prepared=True)
		# preparing our query by specifying '%s' as value, which will allow us to insert our variables soon after
		sql_insert_query = """ INSERT INTO `sizesharedfolder` (`Size`) VALUES (%s)"""
		# preparing the insertion of our values
		insert_tuple = (totalSizeUsed,)
		# we run the result of the query with the values of the script
		result = cursor.execute(sql_insert_query, insert_tuple)
		# commit data
		connection.commit()
		print("All the data were correctly registered in database.")

	except mysql.connector.Error as error:
		connection.rollback()
		print("Error of parameters: {}".format(error))

	finally:
		# closing database connection.
		if (connection.is_connected()):
			cursor.close()
			connection.close()