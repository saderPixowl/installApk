import subprocess
import os
import time
import sys

if (len(sys.argv) < 5):
    print ("Error: wrong number of paramters")
    print ("Usage: 'python adbCommands.py package_name path_to_file minutes_first_launch minutes_for_launch(flaot) iterations(int)'")
    sys.exit(-1) 
else:
    PACKAGE_NAME = sys.argv[1]
    APK_NAME = sys.argv[2]
    MIN_FIRST_LAUNCH = float(sys.argv[3])
    MIN_FOR_LAUNCH = float(sys.argv[4])
    ITERATIONS = int(sys.argv[5])

    
    
def run_command(command):
    print ("run command adb " + command + "\noutput:")
    p = subprocess.Popen(("adb " + command).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))

    print ("end command output ")


commandDevices = "devices"
commandUnistall = "uninstall " + PACKAGE_NAME
commandInstall = "install " + APK_NAME
commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
commandStop = "shell am force-stop " + PACKAGE_NAME


#run_command(commandStop)
#run_command(commandUnistall)

#don't work on jenkins
#run_command(commandInstall)

run_command(commandPlay)
print ("sleep for " + str(MIN_FIRST_LAUNCH * 60.0))
time.sleep(MIN_FIRST_LAUNCH * 60.0)
run_command(commandStop)

   
for i in range(ITERATIONS-1):
    run_command(commandPlay)
    print ("sleep for " + str(MIN_FOR_LAUNCH * 60.0))
    time.sleep(MIN_FOR_LAUNCH * 60.0)
    run_command(commandStop)

print ("END adbCommand.py")




  
