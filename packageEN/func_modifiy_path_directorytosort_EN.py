def getPathDirectoryToSort(filename):

	try:
		# open file and get each value from first line (separated by a space)
		with open(filename, mode='r', encoding='utf-8') as path_file:
			for parameter in path_file:
				path = parameter.split()[0]
		return path

	except IOError:
		#error sys.exit (1)
		sys.exit("Error: cannot access to pathdirectory.txt.")
