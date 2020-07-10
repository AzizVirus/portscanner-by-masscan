import os
import sys
import time

#banner
#
#_____________________________________________________________________________
#  ____            _   ____                                    ____          |
# |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ___ _ __  | __ ) _   _   |
# | |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__| |  _ \| | | |  |
# |  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | |  __/ |    | |_) | |_| |  |
# |_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_|\___|_|    |____/ \__, |  |
#                                                                    |___/   |
#  __  __                                                                    |
# |  \/  | __ _ ___ ___  ___ __ _ _ __                                       | 
# | |\/| |/ _` / __/ __|/ __/ _` | '_ \                                      |
# | |  | | (_| \__ \__ \ (_| (_| | | | |                                     |
# |_|  |_|\__,_|___/___/\___\__,_|_| |_|                                     |
#                                                                            |
#-----------------------------------------------------------------------------

#Defining colors
class bcolors:
	HEADER = '\033[95m' #move
	OKBLUE = '\033[94m' #blue
	OKGREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

prompt = bcolors.FAIL + 'PortScanner By Masscan:@ ' + bcolors.ENDC + ' '
start_time = time.time()
os.system("clear")
time.sleep(0.5)
os.system("figlet PortScanner By Masscan")
time.sleep(0.75)
target = raw_input(prompt + 'Enter Target: ')
print prompt + "Target Selected ! ===> " + target
scanrange = raw_input(prompt + 'Select Port Scanning Range (0-65535 max) : ')
print prompt + "Port Scanning Range Selected ! ===>  " + scanrange
print prompt + "There Is Your Settings below: "
print " "
print "                          IP Target      ===> " + target
print "                          Scanning Range ===> " + scanrange
print " "
time.sleep(0.75)
if raw_input (prompt + "Start Scan ? (y/n): ") == "n":
 print " "
 sys.exit("exit")
else:
 os.system("clear")
 os.system("figlet Scan Started ")
 os.system("masscan "+target+" -p "+scanrange)
 print prompt + "Scan Finished !"
 print prompt + "Time elapsed: " + str(time.time() - start_time)
 print prompt + "Exit Now !"
 sys.exit
 

  


