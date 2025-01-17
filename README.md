﻿# Script-Python-auto-reorganize

Français
=======

## Description:

Script en Python qui réorganise les fichiers dans un dossier et ses sous-dossiers (si ils existent) selon la date de création des fichiers : si un fichier est vieux de plus de 2 semaines, le déplace dans un sous-dossier du nom du créateur.

Mise en place : pour utiliser le script, le mettre à la racine du dossier à trier. 
Ouvrez ensuite votre console et executer le script: si des fichiers sont vieux, cela créera (si il n'existe pas déjà) le dossier "archives" puis un dossier du nom du créateur, ensuite le script va déplacer ces fichiers dans ce dossier. (voir la partie usage pour la mise en place complète du script)

Le script écrit toutes les informations dans le fichier log.txt directement. Par contre cela écrase ce qui était écrit précédemment le jour même sauf si vous rajoutez d'autres indications de temps dans l'écriture du log.

Si l'utilisateur dépasse 1 Giga, une alerte Windows apparait et un email est envoyé (désactivé par défaut). Si vous utilisez ce code, pensez bien à changer les identifiants email et informations SMTP dans SMTPinformations.txt, à changer votre message dans message.txt, le destinataire et son adresse dans contacts.txt.

Si vous utilisez un serveur SMTP gratuit, pensez bien à activer l'accès IMAP.


## Usage:

Tout d'abord, téléchargez l'ensemble du dossier avec ce lien: https://github.com/SmartGuyy/Script-Python-auto-reorganize/archive/master.zip

Ensuite dézipper le à la racine du dossier que vous souhaitez contrôler avec le script.

Note: vous devez être administrateur de votre machine et télécharger/installer Python à cette adresse : https://www.python.org/downloads/.

Pour tester le script avec votre propre dossier, il faudra modifier le chemin dans le fichier pathdirectory.txt avec le chemin vers votre dossier ainsi que databaseParameters.txt pour vos informations de connexion à votre base de données.

Pour la base de données vous devez créer:
- une table "datafromusers" avec 5 valeurs: entryID qui doit être un INT auto incrementé, warning(VARCHAR 3), usersConcerned(VARCHAR 20), sizeExceeded(VARCHAR 30) and Date (TIMESTAMP CURRENT_TIMESTAMP)
- une table "sizesharedfolder" avec 3 valeurs: ID (INT auto incremented), Date (TIMESTAMP CURRENT_TIMESTAMP), Size (VARCHAR 30).

L'option d'envoi de mail est désactivé par défaut, si vous voulez l'activer il faut indiquer vos informations de connexion SMTP dans le fichier SMTPinformations.txt et enlever le # de la ligne sendMail() dans votre fichier scriptFR.py.

Ensuite il faut également modifier le fichier "mycontacts.txt" par les destinataires du mail envoyé par le script ainsi que "message.txt" pour son contenu.

Pour éxecuter le script, vous devez ouvrir un terminal: pour Windows, tapez CMD dans la barre de recherche puis naviguez avec la commande "cd" jusqu'au dossier où se trouve votre scriptFR.py. Ecrivez ensuite simplement scriptFR.py et vous devriez voir apparaitre un log dans le même dossier avec toutes les informations sur l'éxecution du script.

## License:
Script-Python-auto-reorganize est sous license MIT.
Si vous voulez lire la license complète, le fichier "LICENSE" se trouve dans ce répertoire.

-------------------------------------------------------------------------------------------------------------------------------------------

English
=======

## Description:

Script in Python that reorganizes files in a folder or in subfolders (if they exist) depending on creation time : if a file is older than 2 weeks, move it to archives/"creatorusername".

Set up: to use the script, put it at the root of the folder to sort.
Then open your console and run the script: if files are old, it will create (if it does not already exist) the folder "archives" then a folder of the name of the creator, then the script will move these files in this folder. (see the usage section for the complete implementation of the script)

This script writes all the information of prints directly in log.txt. However if you run it 2 times a day or more : anything already written will be destroyed except if you add other time indication in the code for log creation.

If the user exceeds 1 Giga, a Windows alert appears and an email is sent (disabled by default). If you use this code, remember to change the email and SMTP credentials in func_send_email.py, to change your message in message.txt, the recipient and their address in contacts.txt.

If you use a free SMTP server, remember to enable IMAP access.


## Usage:

First, download the entire folder with this link: https://github.com/SmartGuyy/Script-Python-auto-reorganize/archive/master.zip
Then unzip it to the root of the folder you want to control with the script.
Note: You must be an administrator of your machine and download / install Python at this address: https://www.python.org/downloads/.

To test the script with your own folder, you must modify the file pathdirectory.txt with the path to your folder and databaseParameters.txt for your informations to connect to your database.

For the database you must create:
- one table "datafromusers" with 5 values: entryID which has to be an INT auto incremented, warning(VARCHAR 3), usersConcerned(VARCHAR 20), sizeExceeded(VARCHAR 30) and Date (TIMESTAMP CURRENT_TIMESTAMP)
- one table "sizesharedfolder" with ID (INT auto incremented), Date (TIMESTAMP CURRENT_TIMESTAMP), Size (VARCHAR 30).

The option to send mail is disabled by default, if you want to enable it you must indicate your SMTP connection information in the file SMTPinformations.txt and remove the # from the line sendMail() in your scriptEN.py file.

Then you must also modify the file "mycontacts.txt" by the recipients of the mail sent by the script as well as "message.txt" for its contents.

To run the script, you must open a terminal: for Windows, type CMD in the search bar and then navigate with the "cd" command to the folder where your scriptEN.py is located. Then just write scriptEN.py and you should see a log in the same folder with all the information about running the script.

## Licensing:
Script-Python-auto-reorganize is under MIT license.
If you want to read the full license, the file "LICENSE" is in this directory.
