# Script-Python-auto-reorganize

Fran�ais
Script en Python qui r�organise un dossier selon la date de cr�ation des fichiers : si un fichier est vieux de plus de 2 semaines, le d�place dans un sous-dossier du nom du cr�ateur.

Mise en place : pour utiliser le script, le mettre � la racine du dossier � trier. Ensuite il faut renommer "directorytosort" par le nom de votre dossier pour la variable "mypath" dans le fichier script.py.
Ouvrez ensuite votre console et executer le script --> si des fichiers sont vieux, cela cr�era (si il n'existe pas d�j�) le dossier "archives" puis un dossier du nom du cr�ateur, ensuite le script va d�placer ces fichiers dans ce dossier.

Pour le moment le script �crit des informations dans la console directement mais le but va �tre de tout rediriger vers un fichier .log

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

English
Script in Python that reorganizes a folder depending on creation time : if it's older than 2 weeks, move it to archives/"creatorusername"

Set up: to use the script, put it at the root of the folder to sort. Then you must rename "directorytosort" by the name of your folder for the "mypath" variable in the script.py file.
Then open your console and run the script -> if files are old, it will create (if it does not already exist) the folder "archives" then a folder of the name of the creator, then the script will move these files in this folder.

At the moment the script only writes information to the console directly but the goal is to redirect everything to a .log file