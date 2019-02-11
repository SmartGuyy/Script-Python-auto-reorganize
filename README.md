# Script-Python-auto-reorganize

Français
Script en Python qui réorganise un dossier selon la date de création des fichiers : si un fichier est vieux de plus de 2 semaines, le déplace dans un sous-dossier du nom du créateur.

Mise en place : pour utiliser le script, le mettre à la racine du dossier à trier. Ensuite il faut renommer "directorytosort" par le nom de votre dossier pour la variable "mypath" dans le fichier script.py.
Ouvrez ensuite votre console et executer le script --> si des fichiers sont vieux, cela créera (si il n'existe pas déjà) le dossier "archives" puis un dossier du nom du créateur, ensuite le script va déplacer ces fichiers dans ce dossier.

Pour le moment le script écrit des informations dans la console directement mais le but va être de tout rediriger vers un fichier .log

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

English
Script in Python that reorganizes a folder depending on creation time : if it's older than 2 weeks, move it to archives/"creatorusername"

Set up: to use the script, put it at the root of the folder to sort. Then you must rename "directorytosort" by the name of your folder for the "mypath" variable in the script.py file.
Then open your console and run the script -> if files are old, it will create (if it does not already exist) the folder "archives" then a folder of the name of the creator, then the script will move these files in this folder.

At the moment the script only writes information to the console directly but the goal is to redirect everything to a .log file