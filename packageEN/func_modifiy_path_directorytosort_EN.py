def getPathDirectoryToSort(filename):

	try:
		# open file and get each value from first line (separated by a space)
		with open(filename, mode='r', encoding='utf-8') as path_file:
			for parameter in path_file:
				path = parameter.split()[0]
		return path

	except IOError:
		print ("Erreur: impossible d'accéder à pathdirectory.txt.")
