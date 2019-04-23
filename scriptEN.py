# to get time and file informations
import os.path, time, sys, datetime
from os import listdir
from os.path import isfile, join

# to create an alert box
import ctypes   

# import our own functions
from packageEN.func_move_file_EN import movefile
from packageEN.func_list_files_EN import getListOfFiles
from packageEN.func_send_email_EN import sendMail
from packageEN.func_connect_to_MySQL_DB_EN import insertToTableForUsers, insertToTableForSharedFolder
from packageEN.func_modifiy_path_directorytosort_EN import getPathDirectoryToSort
# here we use Windows Security API
# MUST install pypiwin32 package before running script
import win32api, win32con, win32security

# date of today
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

# get all prints and redirects it to a new log file (this is for 1 per day, any other log on same day is erased)
try:
	sys.stdout = open("log-"+date+".txt", "w")

except IOError:
	print ("Error: can't create log file.")

# directory (and subdirectories) to sort
myPath = getPathDirectoryToSort('pathdirectory.txt')
# get all files and store it in a table
filesInFolder = getListOfFiles(myPath)
# get number of files in mypath
numberOfFiles = len (filesInFolder)


# get timenow (hour)
timeNow = time.time()
# number of seconds in 2 weeks (this will be the cap of longevity for a file since its creation)
# modify twoWeeksAgo to change how much time files can stay in folder since their creation
twoWeeksAgo = timeNow - 60*60*24*14
# write the date to begin our log file
print (date)

# ceate empty list to get names in it 
nameList = []
# initialize the variable that will count the space used by the user in the folder and subfolders
# then create a dictonnary to store in the order the total used space per user
sizeUsed = 0
sizeUsedPerUser = {}

# check that list is not empty
if not numberOfFiles:
	print ("There is no file to sort.")

# initializing variable to indent in while
i = -1
# initializing totalSizeUsed
totalSizeUsed = 0


# while incrementation is less than numberOfFiles then get file and sort them one by one
while i < numberOfFiles:


	# get information on that file
	statInfo = os.stat(filesInFolder[i])
	sd = win32security.GetFileSecurity (filesInFolder[i], win32security.OWNER_SECURITY_INFORMATION)
	owner_sid = sd.GetSecurityDescriptorOwner ()
	
	# get name and domain name of file creator
	name, domain, type = win32security.LookupAccountSid (None, owner_sid)
	# seconds spent since file creation
	fileCreationTime = os.path.getctime(filesInFolder[i])

	# number of hour before file is sorted
	daysBeforeExpiration = int((fileCreationTime - twoWeeksAgo)/3600) 

	print ("\n") # empty line
	print ("File analyzed :")
	print (filesInFolder[i])
	print ("Last modification: %s" % time.ctime(os.path.getmtime(filesInFolder[i])))
	print ("Created: %s" % time.ctime(os.path.getctime(filesInFolder[i])) )
	print ("Owner of the file is %s\\%s" % (domain, name))
	

	if fileCreationTime < twoWeeksAgo :
		print ("The file is older than 2 weeks, so it has been moved to the archive folder of its creator.")
		
		#delete name of file after last slash
		getPathOnly = "/".join(fichiersDansDossier[i].split("/")[:-1])
		# we call our function movefile of our file func_move_file
		try :
			movefile(fichiersDansDossier[i], "archives\\"+name+"\\"+getPathOnly)

		except :
			sys.exit("Error: file could not be moved.")

		print ("The file is older than 2 weeks, so it has been moved to the archive folder of its creator.")

	else :
		
		print ("The file is recent and will be archived in " + str(daysBeforeExpiration) + " hour.")

	# we add the username in our list if it does not already exist
	# we get the size of the file, if the name already exists then sizeUsed is incremented by the size of the new file
	if name not in nameList:
		nameList.append(name)
		sizeUsed = statInfo.st_size
		sizeUsedPerUser.update({name:sizeUsed})

	else:
		sizeUsed = statInfo.st_size
	
		for names, size in sizeUsedPerUser.items():
			if names == name:
				sizeUsedPerUser[name] += sizeUsed
			
	# increment the loop to move to the next file
	i += 1
	print ("File size is "+str(sizeUsed/1000)+" Kb or "+str(sizeUsed/1000000)+"Mb")

# end of loop -> end result per user

# for each key in the sizeUsedPerUser dictionary, write the name and its value.
for key in sizeUsedPerUser:
	print ("\n") # empty line
	print ("User " + key + " is using " + str(int(sizeUsedPerUser[key]/1000)) + " Kb or " + str(int(sizeUsedPerUser[key]/1000000)) + " Mb.")
	
	# we recover the total weight of the file and convert it into Gigas
	totalSizeUsed += float((sizeUsedPerUser[key]/1000000000))

	if (sizeUsedPerUser[key]/1000000000) > 1: #supérieur à 1 Go 
		print ("Alert : user " + key + " uses more than 1 Giga of storage on the entire folder.")

		#call func to send mail - MUST CHANGE func_send_email before use
		#sendMail()
		warning='YES'
		sizeExceeded=(str((int(sizeUsedPerUser[key]/1000000))-1000)+" Mo")

		# connexion to Database
		insertToTableForUsers(warning,key,sizeExceeded)
	else: 
		print ("Everything is ok.")
print ("\n") # empty line
# "%.2f" % is the formula to leave only 2 decimals
print ("Total size of folder is more than %.2f" %  totalSizeUsed +" Gb.")
insertToTableForSharedFolder("%.2f" % totalSizeUsed +" Gb")

#Script execution was successful
print ("\n") # empty line
print("Script execution was successful.")
sys.exit(0)
