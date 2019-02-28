import os
from os import listdir
from os.path import isfile, join
'''
    Pour le chemin donné, obtient la liste de tous les fichiers de l’arborescence
'''
def getListOfFiles(dirName):
    # créer une liste de fichiers et de sous-répertoires 'noms' dans le répertoire donné
    listOfFile = os.listdir(dirName)
    allFiles = list()

    # on recommence pour chaque entrée
    for entry in listOfFile:
        # on stocke le chemin complet
        fullPath = os.path.join(dirName, entry)
        
        # si l'entrée est un répertoire alors recherche tout les fichiers également dans ce répertoire.
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
