# Script-Python-auto-reorganize

Français
=======

Script en Python qui réorganise les fichiers dans un dossier et ses sous-dossiers (si ils existent) selon la date de création des fichiers : si un fichier est vieux de plus de 2 semaines, le déplace dans un sous-dossier du nom du créateur.

Mise en place : pour utiliser le script, le mettre à la racine du dossier à trier. Ensuite il faut renommer "directorytosort" par le nom de votre dossier pour la variable "mypath" dans le fichier script.py.
Ouvrez ensuite votre console et executer le script --> si des fichiers sont vieux, cela créera (si il n'existe pas déjà) le dossier "archives" puis un dossier du nom du créateur, ensuite le script va déplacer ces fichiers dans ce dossier.

Le script écrit toutes les informations dans le fichier log.txt directement. Par contre cela écrase ce qui était écrit précédemment le jour même sauf si vous rajoutez d'autres indications de temps dans l'écriture du log.

-------------------------------------------------------------------------------------------------------------------------------------------

English
=======

Script in Python that reorganizes files in a folder or in subfolders (if they exist) depending on creation time : if a file is older than 2 weeks, move it to archives/"creatorusername"


 Set up: to use the script, put it at the root of the folder to sort. Then you must rename "directorytosort" by the name of your folder for the "mypath" variable in the script.py file.
Then open your console and run the script -> if files are old, it will create (if it does not already exist) the folder "archives" then a folder of the name of the creator, then the script will move these files in this folder.


This script writes all the information of prints directly in log.txt. However if you run it 2 times a day or more : anything already written will be destroyed except if you add other time indication in the code for log creation.
