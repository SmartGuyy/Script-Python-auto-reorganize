import os.path, time, sys, datetime
from os import listdir
from os.path import isfile, join

#pour créer la liste si elle n'existe pas déjà
from collections import defaultdict

from package.func_move_file import movefile
from package.func_list_files import getListOfFiles

# on utilise ici Windows Security API
# il faut bien installer au préalable pypiwin32
import win32api, win32con, win32security

#initialisation d'une nouvelle liste (pour avoir la taille totale qu'utilise un utilisateur)
a = defaultdict(list)

#date d'aujourd'hui 
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

try:
	sys.stdout = open("log-"+date+".txt", "w")

except IOError:
	print ("Erreur: impossible de trouver le fichier ou les données.")

#le dossier qui sera trié
myPath = 'directorytosort/'
# on récupère chaque fichier dans ce dossier et ses sous dossiers et on le stocke dans un tableau
fichiersDansDossier = getListOfFiles(myPath)
# on récupère le nombre de fichiers dans le dossier mypath
nombreDeFichiers = len (fichiersDansDossier)
# on initialise la variable d'indentation à 0
i = 0
#on récupère l'heure actuelle
timeNow = time.time()
#nombre de secondes dans 2 semaines
twoWeeksAgo = timeNow - 60*60*24*14
#on écrit l'heure actuelle pour le fichier log
print (date)
#on créer une liste vide pour rentrer les noms d'utilisateurs un à un
list = []
#on initialise la variable qui comptera l'espace utilisé par l'utilisateur dans le dossier et sous dossiers
sizeUsed = 0
# vérifier que la liste n'est pas vide
if not nombreDeFichiers:
	print ("Il n'y a pas de fichiers à trier.")
	# On met le programme en pause pour éviter qu'il ne se referme (Windows)
	os.system("pause")

# tant que l'incrémentation est inférieure au nombre de fichiers,
# récupère et trie les fichiers un par un

while i < nombreDeFichiers:
	
	# on récupère les informations sur le fichier
	statInfo = os.stat(fichiersDansDossier[i])
	sd = win32security.GetFileSecurity (fichiersDansDossier[i], win32security.OWNER_SECURITY_INFORMATION)
	owner_sid = sd.GetSecurityDescriptorOwner ()
	
	# on récupère les valeurs de nom d'utilisateur et de domaine du fichier
	name, domain, type = win32security.LookupAccountSid (None, owner_sid)
	# secondes passées depuis la création du fichier
	fileCreationTime = os.path.getctime(fichiersDansDossier[i])

	# nombre d'heures avant expiration converti en int pour enlever decimales
	daysBeforeExpiration = int((fileCreationTime - twoWeeksAgo)/3600) 

	print ("\n") # on ajoute une ligne vide pour espacer le tout
	print ("Fichier suivant :")
	print (fichiersDansDossier[i])
	print ("Dernière modification le: %s" % time.ctime(os.path.getmtime(fichiersDansDossier[i])))
	print ("Créé le: %s" % time.ctime(os.path.getctime(fichiersDansDossier[i])) )
	print ("Le propriétaire du fichier est %s\\%s" % (domain, name))
	
	if fileCreationTime < twoWeeksAgo :
		print ("Le fichier est vieux de plus de 2 semaines, il a donc été déplacé vers le dossier d'archivage de son créateur.")
		
		# on appelle notre fonction movefile de notre fichier func_move_file
		movefile(fichiersDansDossier[i], "archives\\"+name)

	else :
		
		print ("Le fichier est récent et sera archivé dans " + str(daysBeforeExpiration) + " heures.")
	
	# on ajoute le nom d'utilisateur dans notre liste si il n'existe pas déjà
	# on récupère la taille du fichier, si le nom existe déjà alors sizeUsed est incrémenté de la taille du nouveau fichier
	# ! trouver une solution pour que chaque user ait son sizeUsed...

	if name not in list:
		list.append(name)
		sizeUsed = statInfo.st_size
		print (sizeUsed)

	else:
		sizeUsed += statInfo.st_size
		print (sizeUsed)
	
	statInfo = 0
	i += 1

print ("L'utilisateur " + name + " utilise " + str(sizeUsed) + " octets sur ce serveur de fichier.")