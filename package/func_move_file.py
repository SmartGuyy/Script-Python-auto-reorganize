# importation de la librairie shutil, ayant des fonctions 
# pour copier, couper, renommer ou supprimer des fichiers
import shutil, os, glob
from os import listdir
from os.path import isfile, join

def movefile(filetomove, destination):
	
	# si le dossier de destination n'existe pas, le créer
	if os.path.isdir(destination) == False: os.makedirs(destination);
	
	# on déplace le fichier de la manière suivante : shutil.move (Source, Destination)
	shutil.move(filetomove, destination)

 	