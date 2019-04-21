# importing the shutil library, having functions to copy, cut, rename or delete files
import shutil, os
from os import listdir
from os.path import isfile, join

def movefile(filetomove, destination):

	try:
	
		# if folder doesn't exist, creates it
		if os.path.isdir(destination) == False: os.makedirs(destination);
		
		# move file with : shutil.move (Source, Destination)
		shutil.move(filetomove, destination)

	except IOError:
		#error sys.exit (1)
		sys.exit("Error: cannot move file.")
	