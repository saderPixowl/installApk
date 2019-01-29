import subprocess
import os
import time
import sys

if (len(sys.argv) < 2):
    print ("Error: wrong number of paramters")
    print ("Usage: 'python adbCommands.py package_name path_to_file'")
    sys.exit(-1)
        
else:
    PACKAGE_NAME = sys.argv[1]
    APK_NAME = sys.argv[2]
    
    
def run_command(command):
    print ("run command adb " + command + "\noutput:")
    p = subprocess.Popen(("adb " + command).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))

    print ("end command output ")



#PACKAGE_NAME = "com.activision.peanuts"
#APK_NAME = "temp.apk"

commandDevices = "devices"
commandUnistall = "uninstall " + PACKAGE_NAME
commandInstall = "install " + APK_NAME
commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
commandStop = "shell am force-stop " + PACKAGE_NAME

minToSleep = 1/20
iterations = 4
print ("step 01")
run_command(commandStop)
print ("step 02")
run_command(commandUnistall)
print ("step 03")
run_command(commandInstall)

   
for i in range(iterations):
    run_command(commandPlay)
    time.sleep(minToSleep * 60.0)
    run_command(commandStop)

print ("END adbCommand.py")




  
