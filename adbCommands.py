import subprocess
import os
import time

def run_command(command):
    print ("run command adb " + command + "\noutput:")
    p = subprocess.Popen((ADB_PATH + command).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))

    print ("end command output ")


ADB_PATH = "adb "
PACKAGE_NAME = "com.activision.peanuts"
APK_PATH = "/Users/alejandro/Downloads/"
APK_NAME = "Peanuts-499-qa-googleplay-v7a-activision-release.apk"

commandDevices = "devices"
commandUnistall = "uninstall " + PACKAGE_NAME
commandInstall = "install " + APK_PATH + APK_NAME
commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
commandStop = "shell am force-stop " + PACKAGE_NAME

minToSleep = 1/20
iterations = 4
run_command(commandStop)
#run_command(commandUnistall)
#run_command(commandInstall)

   
for i in range(iterations):
    run_command(commandPlay)
    time.sleep(minToSleep * 60.0)
    run_command(commandStop)

print ("END adbCommand.py")




  
