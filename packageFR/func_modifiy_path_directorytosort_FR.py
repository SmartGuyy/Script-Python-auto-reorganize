def getPathDirectoryToSort(filename):

	try:
		# ouvre notre fichier filename et récupère les informations de la première ligne
		with open(filename, mode='r', encoding='utf-8') as path_file:
			for parameter in path_file:
				path = parameter.split()[0]
		return path

	except IOError:
		print ("Erreur: impossible d'accéder à pathdirectory.txt.")
