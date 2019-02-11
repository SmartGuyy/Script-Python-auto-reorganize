import os.path, time, sys, datetime
from os import listdir
from os.path import isfile, join

from package.func_move_file import movefile
from package.func_list_files import getListOfFiles

# on utilise ici Windows Security API
# il faut bien installer au préalable pypiwin32
import win32api, win32con, win32security

sys.stdout = open("log.txt", "w")

#le dossier qui sera trié
mypath = 'directorytosort/'
# on récupère chaque fichier dans ce dossier et ses sous dossiers et on le stocke dans un tableau
fichiersdansdossier = getListOfFiles(mypath)
# on récupère le nombre de fichiers dans le dossier mypath
nombredefichiers = len (fichiersdansdossier)
# on initialise la variable d'indentation à 0
i = 0
#on récupère l'heure actuelle
timenow = time.time()
#nombre de secondes dans 2 semaines
twoweeksago = timenow - 60*60*24*14
#on écrit l'heure actuelle pour le fichier log
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M"))
# vérifier que la liste n'est pas vide
if not nombredefichiers:
	print ("Il n'y a pas de fichiers à trier.")
	# On met le programme en pause pour éviter qu'il ne se referme (Windows)
	os.system("pause")

# tant que l'incrémentation est inférieure au nombre de fichiers,
# récupère et trie les fichiers un par un
while i < nombredefichiers:
	
	# on récupère les informations sur le fichier
	sd = win32security.GetFileSecurity (fichiersdansdossier[i], win32security.OWNER_SECURITY_INFORMATION)
	owner_sid = sd.GetSecurityDescriptorOwner ()
	
	# on récupère les valeurs de nom d'utilisateur et de domaine du fichier
	name, domain, type = win32security.LookupAccountSid (None, owner_sid)

	# secondes passées depuis la création du fichier
	filecreationtime = os.path.getctime(fichiersdansdossier[i])

	# nombre d'heures avant expiration converti en int pour enlever decimales
	daysbeforeexpiration = int((filecreationtime - twoweeksago)/3600) 

	print ("\n") # on ajoute une ligne vide pour espacer le tout
	print ("Fichier suivant :")
	print (fichiersdansdossier[i])
	print ("Dernière modification le: %s" % time.ctime(os.path.getmtime(fichiersdansdossier[i])))
	print ("Créé le: %s" % time.ctime(os.path.getctime(fichiersdansdossier[i])) )
	print ("Le propriétaire du fichier est %s\\%s" % (domain, name))
	
	if filecreationtime < twoweeksago :
		print ("Le fichier est vieux de plus de 2 semaines, il a donc été déplacé vers le dossier d'archivage de son créateur.")
		
		# ATTENTION : le dossier de destination DOIT être créer avant de lancer le script pour chaque utilisateur.
		movefile(fichiersdansdossier[i], "archives\\"+name)

	else :
		print ("Le fichier est récent et sera archivé dans " + str(daysbeforeexpiration) + " heures.")
	
	i += 1
