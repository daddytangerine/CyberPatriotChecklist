##############################################################################################################
#             Cyber Patriot Checklist - Windows v4.0                                                         #
#             Created By Bennett Yardley                                                                     #
#             Licensed Under GNU                                                                             # 
#             To view more information type "i", To continue type "c", To go to next section type "n"        #
##############################################################################################################

import os

def FRST():
	os.system('cls')
	print "FRST"
	print " "
	print 'You may need to change "only elevation applications that are signed/validated - enabled" in secpol.msc (security options)'
	print "Check all options - Press Scan"
	print "Carefully look through the output files - if you see anything copy it into a new text file (underneath the same directory) called fixlist.txt"
	print "Press the fix button when fixlist.txt is finished"
	print " "


def windows8():
	os.system('cls')
	print "Settings App For Windows 8 +"
	print " "
	print "Privacy:"
	print "Turn off all allow share location"
	print "Turn off Camera"
	print "Turn off Mircrophone"
	print "Don't Allow apps to use Account Info"
	print "Don't Allow apps to use Contact Info"
	print "...Don't Allow apps to use anything"
	print " " 
	print "System:"
	print "Uninstall all apps"
	print " "
	print "Accounts:"
	print "Don't allow users to sign in with microsoft account"
	print " "
	choice23 = raw_input("Continue or View More Info: ")
	if choice23 == 'c': 
		FRST()
	if choice23 == 'i':
		print "No information is currently available for this topic"
		choice24 = raw_input("Continue?: ")
		if choice24 == 'c':
			FRST()
	

def management():
	os.system('cls')
	print "Computer Management"
	print " "
	print "Task Scheduler:"
	print "Delete all tasks"
	print " "
	print "Shared Folders:"
	print "Delete any folder shares that are not (C$ ADMIN$ IPC$)"
	print " " 
	choice21 = raw_input("Continue or View More Info: ")
	if choice21 == 'c': 
		windows8()
	if choice21 == 'i':
		print "No information is currently available for this topic"
		choice22 = raw_input("Continue?: ")
		if choice22 == 'c':
			windows8()


def taskManager():
	os.system('cls')
	print "Task Manager"
	print " "
	print "Processes:"
	print "Look through processes - Open File Location see if it is a bad location"
	print "Search Online"
	print " "
	print "Startup:"
	print "Look through applications - Open File Location see if it is a bad location"
	print "Search Online"
	print " "
	print "Services:"
	print "Open services"
	print "Disable any service that is not listed as critical or is not absolutley needed"
	print " "
	choice19 = raw_input("Continue or View More Info: ")
	if choice19 == 'c': 
		management()
	if choice19 == 'i':
		print "No information is currently available for this topic"
		choice20 = raw_input("Continue?: ")
		if choice20 == 'c':
			management()


def fileExplorer():
	os.system('cls')
	print "File Explorer"
	print " "
	print "Show hidden files/folders"
	print "Check through each folder for .exe or .rar ETC..."
	print " "
	choice17 = raw_input("Continue or View More Info: ")
	if choice17 == 'c': 
		taskManager()
	if choice17 == 'i':
		print "No information is currently available for this topic"
		choice18 = raw_input("Continue?: ")
		if choice18 == 'c':
			taskManager()


def inter():
	print "At this point you should save / take a picture of your points"
	print "You may want to do this a few times throughout"
	print "If you didn't install service packs you may want to now"
	print " "
	inter1 = raw_input("Continue or View More Info: ")
	if inter1 == 'c': 
		fileExplorer()
	if inter1 == 'i':
		print "No information is currently available for this topic"
		inter2 = raw_input("Continue?: ")
		if inter2 == 'c':
			fileExplorer()


def secpolLP():
	os.system('cls')
	print "Local Security Policy"
	print "Sections: Account Policies / Local Policies"
	print " "
	print "Local Policies"
	print " "
	print "Audit Policy:"
	print "Change every option to Success, Faliure"
	print " "
	print "Security Options:"
	print "Admin Account - Disabled"
	print "Block Microsoft Accounts - Can't add or logon"
	print "Guest Account - Disabled"
	print "Limit local account use of blank passwords - Enabled"
	print "Rename Administrator Account - Admin"
	print "Rename Guest Account - Not Admin"
	print "Allow undock without having to logon - Disabled"
	print "Allowed to format and eject media - Admins"
	print "Pevent users from installing printer drivers - Enabled"
	print "Restrict CDROM access to locally logged-on user - Enabled"
	print "Restrict Floppy access to logged-on user - Enabled"
	print "Allow server operators to schedule tasks - Disabled"
	print "LDAP requirments - Require"
	print "Refuse machine account password changes - Enabled"
	print "Digitally encrypt or sign data - Enabled"
	print "Digitally encrypt secure channel data - Enabled"
	print "Digitally sign secure channel data - Enabled"
	print "Require strong session key - Enabled"
	print "Display user information - Do Not Display"
	print "Do not display last user name - Enabled"
	print "Do not require CTRL+ALT+DELETE - Disabled"
	print "Machine inactivity limit - 60 seconds"
	print "Message Text: You are only allowed if you are allowed"
	print "Message Title: Only for authorized users"
	print "number of logons to cache - 0"
	print "Require domain controller authentication - disabled"
	print "require smart card - disabled"
	print "digitally sign communications(always/if agrees) - enabled"
	print "send unencrypted password to SMB server - disabled"
	print "amount of idle time - 10 minutes"
	print "attempt S4U2Self - enabled"
	print "digitally sign communications(always/if agress) - enabled"
	print "disconect clients when logon hours expire - enabled"
	print "SPN target name - required"
	print "allow anonymous SID translation - disabled"
	print "do not allow anonymous enumerations of SAM - enabled"
	print "do not allow storage of passwards/credentials - enabled"
	print "let everyone persmissions apply to anonymous users - enabled"
	print "remotely accessibly registry - clear all"
	print "remotely accessibly registry paths and sub-paths - clear all"
	print "restrict anonymous access to named pipes/shares - enabled"
	print "sharing model for local - classic"
	print "allow local system to use computer identity for NTLM - disabled"
	print "allow local system NUMM session fallback - disabled"
	print "allow PJU2U authentication to use online identities - disabled"
	print "do not store lan hash value on next change - enabled"
	print "force logoff when hours expire - enabled"
	print "LDAP requirments - require signing"
	print  "minimum session security for clients/servers - require both"
	print "Restrict NTLM: Incoming NTLM Traffic - deny all"
	print "NTLM authentication - deny all"
	print "outgoing NTLM traffic - deny all"
	print "allow automatic admin logon - disabled"
	print "allow floppy copy and access to all drives/folders - disabled"
	print "allow system to be shutdown without logging in - enabled"
	print "clear virtual memory page file - enabled"
	print "force strong key protection - enabled"
	print "use FIPS algorithm - enabled"
	print "require case insensitivity - disabled"
	print "strengthen default permissions of internal objects - enabled"
	print "use certificate rules on windows executables - enabled"
	print "admin approval mode - enabled"
	print "UIAccess applications to prompt for elevation - disabled"
	print "Behavior of elevation prompt - prompt for credentials on secure desktop"
	print "Behavior of elevation prompt for standard users - prompt for credentials on secure desktop"
	print "detect application installations and prompt for elevation - enabled"
	print "only elevation applications that are signed/validated - enabled"
	print "only elevate UIAccess applications that are installed in secure locations - enabled"
	print "run all admins in admin aproval mode - enabled"
	print "switch to secure desktop when prompting for elevation - enabled"
	print "virtualize file and registry write failures - enabled"
	print " "
	choice15 = raw_input("Continue or View More Info: ")
	if choice15 == 'c': 
		inter()
	if choice15 == 'i':
		print "No information is currently available for this topic"
		choice16 = raw_input("Continue?: ")
		if choice16 == 'c':
			inter()


def secpolAP():
	os.system('cls')
	print "Local Security Policy"
	print "Sections: Account Policies / Local Policies"
	print " "
	print "Account Policies"
	print " "
	print "Password Policy:"
	print "History - 5"
	print "Maximum Age- 30"
	print "Minimum Age- 15"
	print "Minimum Length - 8"
	print "Complexity - Enable"
	print "Reversible Encryption - Disable"
	print " " 
	print "Account Lockout Policy:"
	print "Threshold - 3"
	print "Should automatically change others to 30 minutes"
	print " "
	choice13 = raw_input("Next Section or View More Info: ")
	if choice13 == 'n': 
		secpolLP()
	if choice13 == 'i':
		print "No information is currently available for this topic"
		choice14 = raw_input("Continue?: ")
		if choice14 == 'c':
			secpolLP()
	

def controlPanelNaI():
	os.system('cls')
	print "Control Panel"
	print "Sections: Users / PaF / SaS"
	print " "
	print "Network and Internet"
	print " "
	print "Network and Sharing Center:"
	print "Advanced Sharing Settings - Turn off network discovery"
	print "Advanced Sharing Settings - Turn off file/printer sharing"
	print "Advanced Sharing Settings - Use passwords for homegroup"
	print " "
	print "Internet Options:"
	print "Change Homepage to http://www.google.com"
	print "Delete browsing history on exit"
	print "Turn up slider under security"
	print "Turn up any other sliders"
	print "Privacy - PopUp Blocker enabled"
	print "Privacy - Don't Accept Cookies"
	print "Remove all add-ons"
	print " "
	choice11 = raw_input("Continue or View More Info: ")
	if choice11 == 'c': 
		secpolAP()
	if choice11 == 'i':
		print "No information is currently available for this topic"
		choice12 = raw_input("Continue?: ")
		if choice12 == 'c':
			secpolAP()


def controlPanelSAS():
	os.system('cls')
	print "Control Panel"
	print "Sections: Users / PaF / SaS / NaI"
	print " "
	print "System and Security"
	print " "
	print "Action Center:"
	print "Ensure Firewall/Defender is active"
	print "Ensure User Action Control is at highest"
	print "Ensure Windows SmartScreen is on and active at highest settings"
	print "Change maintenance settings to everyday and start maintenance"
	print " " 
	print "System: "
	print "Advanced System Settings - Uncheck Allow remote assistance"
	print "Don't allow remote connections to this computer"
	print " "
	print "Power Options: "
	print "Require a password on wakeup - Enabled"
	print " "
	print "Windows Update: "
	print "Check for updates daily / Install automatically"
	print "Check for updates and update"
	print "Install Service Packs (If you do not right now take a note to do it later)"
	print " "
	choice9 = raw_input("Next Section or View More Info: ")
	if choice9 == 'n': 
		controlPanelNaI()
	if choice9 == 'i':
		print "No information is currently available for this topic"
		choice10 = raw_input("Continue?: ")
		if choice10 == 'c':
			controlPanelNaI()
	

def controlPanelPAF():
	os.system('cls')
	print "Control Panel"
	print "Sections: Users / PaF / SaS / NaI"
	print " "
	print "Programs and Features"
	print " "
	print "Remove Programs Acording To ReadMe"
	print " "
	choice7 = raw_input("Next Section or View More Info: ")
	if choice7 == 'n': 
		controlPanelSAS()
	if choice7 == 'i':
		print "No information is currently available for this topic"
		choice8 = raw_input("Continue?: ")
		if choice8 == 'c':
			controlPanelSAS()


def controlPanelUsers():
	os.system('cls')
	print "Control Panel"
	print "Sections: Users / PaF / SaS / NaI"
	print " "
	print "Users"
	print " "
	print "Add/Delete Users"
	print "Add/Delete Admins"
	print "Change Everyones Password"
	print "Disable Guest Account"
	print "Turn up User Account Control Settings"
	print " "
	choice5 = raw_input("Next Section or View More Info: ")
	if choice5 == 'n': 
		controlPanelPAF()
	if choice5 == 'i':
		print "No information is currently available for this topic"
		choice6 = raw_input("Continue?: ")
		if choice6 == 'c':
			controlPanelPAF()


def openingNotes():
	os.system('cls')
	print "Opening Notes"
	print " "
	print "Read the ReadMe and take notes"
	print "Do the forensics questions NOW"
	print " "
	choice3 = raw_input("Continue or View More Info: ")
	if choice3 == 'c':
		controlPanelUsers()
	if choice3 == 'i':
		print "Take notes on which users to keep"
		print "Take notes on which users are admins"
		print "Take notes on which programs to update or keep"
		print "Use a teammate or google to do forensics"
		choice4 = raw_input("Continue?: ")
		if choice4 == 'c':
			controlPanelUsers()
		
	
def main():
	os.system('cls')
	os.system('color 2')
	print "Cyber Patriot Checklist - Windows v4.0" 
	print "Created By Bennett Yardley"
	print "Licensed Under GNU"
	print 'To view more information type "i", To continue type "c", To go to next section type "n"'
	print " "
	choice1 = raw_input("Continue or View More Info: ")
	if choice1 == 'c':
		openingNotes()
	if choice1 == 'i':
		print "No extra information is currently available for this topic"
		choice2 = raw_input("Continue?: ")
		if choice2 == 'c':
			openingNotes()
		
		
main()
	 
