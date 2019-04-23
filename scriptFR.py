# pour récupérer le temps et les informations sur les fichiers
import os.path, time, sys, datetime
from os import listdir
from os.path import isfile, join

# pour créer une alert box
import ctypes   

# on importe nos fonctions maison
from packageFR.func_move_file_FR import movefile
from packageFR.func_list_files_FR import getListOfFiles
from packageFR.func_send_email_FR import sendMail
from packageFR.func_connect_to_MySQL_DB_FR import insertToTableForUsers, insertToTableForSharedFolder
from packageFR.func_modifiy_path_directorytosort_FR import getPathDirectoryToSort
# on utilise ici Windows Security API
# il faut bien installer au préalable pypiwin32
import win32api, win32con, win32security

# date d'aujourd'hui 
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

# on récupère tout les print dans un fichier log avec la date d'aujourd'hui
try:
	sys.stdout = open("log-"+date+".txt", "w")

except IOError:
	#erreur sys.exit (1)
	sys.exit("Erreur: impossible de créer le fichier log.")

# le dossier qui sera trié
myPath = getPathDirectoryToSort('pathdirectory.txt')
# on récupère chaque fichier dans ce dossier et ses sous dossiers et on le stocke dans un tableau
fichiersDansDossier = getListOfFiles(myPath)
# on récupère le nombre de fichiers dans le dossier mypath
nombreDeFichiers = len (fichiersDansDossier)


# on récupère l'heure actuelle
timeNow = time.time()
# nombre de secondes dans 2 semaines
twoWeeksAgo = timeNow - 60*60*24*14
# on écrit l'heure actuelle pour le fichier log
print (date)

# on créer une liste vide pour rentrer les noms d'utilisateurs un à un
nameList = []
# on initialise la variable qui comptera l'espace utilisé par l'utilisateur dans le dossier et sous dossiers 
# puis on créer un dictionnaire pour stocker dans l'ordre l'espace utilisé total par utilsateur
sizeUsed = 0
sizeUsedPerUser = {}

# vérifier que la liste n'est pas vide
if not nombreDeFichiers:
	print ("Il n'y a pas de fichiers à trier.")
	# On met le programme en pause pour éviter qu'il ne se referme (Windows)
	os.system("pause")

# on initialise la variable d'indentation de la boucle à 0
i = -1
# on initialise le poids total du dossier
totalSizeUsed = 0


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
		#formule pour supprimer le nom du fichier après le dernier slash
		getPathOnly = "/".join(fichiersDansDossier[i].split("/")[:-1])
		# on appelle notre fonction movefile de notre fichier func_move_file
		
		try :
			movefile(fichiersDansDossier[i], "archives\\"+name+"\\"+getPathOnly)

		except :
			sys.exit("Erreur: le fichier n'a pas pu être déplacé.")

		print ("Le fichier est vieux de plus de 2 semaines, il a donc été déplacé vers le dossier d'archivage de son créateur.")

	else :
		
		print ("Le fichier est récent et sera archivé dans " + str(daysBeforeExpiration) + " heures.")

	# on ajoute le nom d'utilisateur dans notre liste si il n'existe pas déjà
	# on récupère la taille du fichier, si le nom existe déjà alors sizeUsed est incrémenté de la taille du nouveau fichier
	if name not in nameList:
		nameList.append(name)
		sizeUsed = statInfo.st_size
		sizeUsedPerUser.update({name:sizeUsed})

	else:
		sizeUsed = statInfo.st_size
	
		for names, size in sizeUsedPerUser.items():
			if names == name:
				sizeUsedPerUser[name] += sizeUsed
			
	# on incrémente la boucle pour passer au fichier suivant
	i += 1
	print ("La taille du fichier est de "+str(sizeUsed/1000)+" Ko ou "+str(sizeUsed/1000000)+"Mo")

# fin de boucle --> résultat final par utilisateur

# pour chaque clé dans le dictionnaire sizeUsedPerUser, écrit le nom et sa valeur.
for key in sizeUsedPerUser:
	print ("\n") # on ajoute une ligne vide pour espacer le tout
	print ("L'utilisateur " + key + " utilise " + str(int(sizeUsedPerUser[key]/1000)) + " Ko ou " + str(int(sizeUsedPerUser[key]/1000000)) + " Mo.")
	
	#on récupère le poids total du dossier et on le convertit en Gigas
	totalSizeUsed += float((sizeUsedPerUser[key]/1000000000))

	if (sizeUsedPerUser[key]/1000000000) > 1: #supérieur à 1 Go 
		print ("Alerte : l'utilisateur " + key + " utilise plus d'1 Giga de stockage sur le dossier entier.")
		#sendMail()
		warning='YES'
		sizeExceeded=(str((int(sizeUsedPerUser[key]/1000000))-1000)+" Mo")
		#connexion à la base de données
		insertToTableForUsers(warning,key,sizeExceeded)
	else: 
		print ("Tout va bien.")
print ("\n") # on ajoute une ligne vide pour espacer le tout
# "%.2f" % est la formule pour laisser seulement 2 décimales
print ("Le poids total du dossier fait plus de %.2f" %  totalSizeUsed +" Go.")
insertToTableForSharedFolder("%.2f" % totalSizeUsed +" Go")

#le script s'est exécuté sans erreurs
print ("\n") # on ajoute une ligne vide pour espacer le tout
print("Le script s'est éxecuté sans erreurs.")
sys.exit(0)

