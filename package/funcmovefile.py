# importation de la librairie shutil, ayant des fonctions 
# pour copier, couper, renommer ou supprimer des fichiers
import shutil, os, glob
from os import listdir
from os.path import isfile, join

def movefile(mypath, filetomove, destination):
	# si le dossier de destination n'existe pas, le créer
	#if os.path.isdir(destination) == False:
    #	os.makedirs(destination)
	#shutil.commande (Source, Destination)
	shutil.move(mypath+filetomove, destination)

 	#shutil.move(filetomove, 'test\\') working

 	# On met le programme en pause pour éviter qu'il ne se referme (Windows)
	# os.system("pause")