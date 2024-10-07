#!/bin/usr/python3

#Log Parse auth.log: Extract command usage
print('Here is the list of commands used, including the timestamp and the executing user')
file=open('auth.log','r') 									#opens the file named "auth.log" and sets up reading mode
for eachline in file:										#creates a for loop for reading each line in the auth.log
	if 'COMMAND' in eachline:								#project objective (1): Extracting command usage. If a 'command' is used, it will be in focus
		splatline=eachline.split()							#splits up the string of eachline into substrings
		timestamp=' '.join(splatline[:3])					#project objective 1.1 stores the first three strings in the splatline with a space separating them, as a variable named timestamp
		user=splatline[5]									#project objective 1.2 stores the 12th substring following the zero index rule as a variable named user
		commandequal=splatline[13]								#project objective 1.3 stores the 14th substring following the zero index rule as a variable named command
		slcommandequal=commandequal.split('/')				#splits the variable command equal using '/' as a delimiter
		command=slcommandequal[-1]							#obtains the last object of the slcommandequal list and stores it as the variable
		print('On',timestamp,',',user,'executed the command','"',command,'"')
file.close() 												#closes the file
#Log Prase auth.log: Monitor user authentication changes

#Print details of newly added users, including time stamp
print(' ')
print('Here are the details of newly added users')
file=open('auth.log','r') 																#opens the file named "auth.log" and sets up reading mode
for elnewuser in file:																	#creates a for loop for reading each line in the auth.log (el= each line)
	if 'new user' in elnewuser: 														#if condition for locating "new user" string in each line
		slnewuser=elnewuser.split()  													#splits the string of ealnewuser in to substrings
		newusertimestamp=' '.join(slnewuser[:3])										#Stores the first three strings in the slnewuser into a new variable
		newuserequal=slnewuser[7] 														#obtains the 8th substring and stores it as the variable "newuserequal"
		splatnewuserequal=newuserequal.split('=')										#splits the string(former substring) into substring again using "=" as a divider
		newuser=splatnewuserequal[1]													#obtains the 2nd substring to be stored as variable "newuser"
		print('A new user with the username',newuser,'was added','on',newusertimestamp) #prints string sentence informing user of new users being added
file.close() 																			#closes the file

#Print details of deleted users, including the Timestamp
print(' ')
print('Here are the details of deleted users')	
file=open('auth.log','r') 																	#opens the file named "auth.log" and sets up reading mode
for eldeluser in file:																		#creates a for loop for reading each line in the auth.log (el= each line)
	if 'userdel' in eldeluser: 																#if condition for locating "userdel" string in each line
		sldeluser=eldeluser.split() 														#splits the string of eldeluser in to substrings
		delusertimestamp=' '.join(sldeluser[:3])											#Obtains the first 3 substring which includes the date and time
		deluser=sldeluser[5] 																#obtains the 8th substring and stores it as the variable "deluser"
		print('A user with the username',deluser,'was deleted','on',delusertimestamp)		#prints string sentence informing user of deleted user
file.close() 																				#closes the file

#Print details of changing passwords, including the Timestamp
print(' ')
print('Here are the details of changed passwords')	
file=open('auth.log','r') 																	#opens the file named "auth.log" and sets up reading mode
for elchpass in file: 																		#creates a for loop for reading each line in the auth.log (el= each line)
	if 'password changed' in elchpass: 														#if condition for locating "password changed" string in each line
		slchpass=elchpass.split()															#splits the string of eldeluser in to substrings
		chpasstimestamp=' '.join(slchpass[:3])											 	#Obtains the first 3 substring which includes the date and time
		chpassuser=slchpass[-1]																#Obtains the last substring as the vairable "chpassuser"
		print(chpassuser, 'changed password on', chpasstimestamp)							#prints string informing user of users that changed passwords
file.close() 																				#closes the file

print(' ')
print('Here are the details of the su command being used')	
file=open('auth.log','r') 																	#opens the file named "auth.log" and sets up reading mode
for elsu in file:																			#creates a for loop for reading each line in the auth.log (el= each line)
	if '(su:session): session opened' in elsu:												#looks for lines that contains said string. This focuses on "session opened" lines
		slsu=elsu.split()																	#splits the string of eldeluser in to substrings
		sutimestamp=' '.join(slsu[:3])														#Obtains the first 3 substring which includes the date and time
		sudetails=' '.join(slsu[6:])														#obtains the details of the su command being used from the 7th substring till the end
		print('On',sutimestamp,'A', sudetails) 												#prints string informing reader of users that executed the su command
file.close() 																				#closes the file

print(' ')
print('Here are the details if the sudo command being used')	
file=open('auth.log','r') 																	#opens the file named "auth.log" and sets up reading mode
for elsudopass in file:																		#creates a for loop for reading each line in the auth.log (el= each line)
	if 'sudo' and 'COMMAND' in elsudopass: 													#looks for lines that contain the string "sudo" and "COMMAND"
		slsudopass=elsudopass.split()														#splits the string of eldeluser in to substrings
		sudouserpass=slsudopass[5]															#obtains the 6th substring which which contains the user that executed the sudo command and stores it as a vairable sudouserpass
		sudocommandequal=slsudopass[13] 													#obtains the 14th substring and stores it as the command that the user executed with the sudo command and stores it as a variable "sudocommand"
		slsudocommandequal=sudocommandequal.split('/')										#splits the string sudocommandequal using '/' as a delimiter
		sudocommand=slsudocommandequal[-1]													#takes the last object of the slsudocommandequal and stores it as a variable
		print(sudouserpass, 'used the command','"', sudocommand,'"', 'with sudo') 			#prints information informing reader of the users that executed the sudo command
file.close() 																				#closes the file	
	
print(' ')
print('Here are the details if there was an attempt to use a sudo command')	
file=open('auth.log','r') 																								#opens the file named "auth.log" and sets up reading mode		
for elsudofail in file:																									#creates a for loop for reading each line in the auth.log (el= each line)
	if 'sudo' and 'command not allowed' in elsudofail:																	#looks for lines that contain the string "sudo" and "command not allowed"
		slsudofail=elsudofail.split()																					#splits the string of eldeluser in to substrings
		sudouserfail=slsudofail[5] 																						#obtains the 6th substring and stores it as a variable named "sudouserfail"
		sudofailcommandequal=slsudofail[17]																				#obtains the 18th substring and stores it as a variable named "sudofailcommand"
		slsudofailcommandequal=sudofailcommandequal.split('/')															#splits the string of sudofailcommandequal using "/" as a delimiter 
		sudofailcommand=slsudofailcommandequal[-1]																		#Takes the last object of the list from sldusocommandfailequal
		print('ALERT!', sudouserfail, 'attempted to use the command','"', sudofailcommand,'"', 'with sudo privileges') 	#prints Alert informing reader of users that attempted to use the sudo command
file.close() 																											#closes the file

