import os
from os import listdir
from os.path import isfile, join
'''
	For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):

	try:

		# create a list of file and sub directories 
		# names in the given directory 
		listOfFile = os.listdir(dirName)
		allFiles = list()
		# Iterate over all the entries
		for entry in listOfFile:
			# Create full path
			fullPath = os.path.join(dirName, entry)
			# If entry is a directory then get the list of files in this directory 
			if os.path.isdir(fullPath):
				allFiles = allFiles + getListOfFiles(fullPath)
			else:
				allFiles.append(fullPath)
					
		return allFiles

	except IOError:
		#error sys.exit (1)
		sys.exit("Error: cannot get list of files.")