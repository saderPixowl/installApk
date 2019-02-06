import subprocess
import os
import time
import sys
import datetime

import time
from threading import Timer

if (len(sys.argv) < 3):
    print ("Error: wrong number of paramters")
    print ("Usage: 'python adbCommands.py package_name eventCount(int) iterations duration_of_iterations(seconds)'")
    sys.exit(-1) 
else:
    PACKAGE_NAME = sys.argv[1]
    #EVENT_COUNT = int(sys.argv[2])
    ITERATIONS = int(sys.argv[2])
    DURATION = int(sys.argv[3])


    
    
def runCommand(command, device):
    print ("run command adb -s "+device +" " + command )

    p = subprocess.Popen(("adb -s "+device +" " + command).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))
    #print ("end command output ")

def runCommandAllDevices(command, devices):
    for device in devices:
        #print("- - - - - - - - command = " + command + " device " + device)
        runCommand(command, device)

def getDevices():
    commandDevices = "devices"
    devicesList=[]
    # print ("run command adb " + commandDevices + "\noutput:")
    p = subprocess.Popen(("adb " + commandDevices).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        if (line == "List of devices attached"):
            next
        deviceLine = line.decode('utf-8')
        if ("device\n" in deviceLine):
            deviceLine = deviceLine.replace("device", "")
            deviceLine = deviceLine.strip()
            devicesList.append(deviceLine)
    return devicesList

def runCicle():
   # print("time = " + datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
    print("time: " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second))
    runCommandAllDevices(commandStop, myDevices)
    runCommandAllDevices(commandPlay, myDevices)
    # runCommandAllDevices(commandStop, myDevices)
    # runCommandAllDevices(commandPlay, myDevices)




def print_time():
    print("TIMERRRR")

commandUnistall = "uninstall " + PACKAGE_NAME
#commandInstall = "install " + APK_NAME
commandPlayFirst = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
#commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER " + str(EVENT_COUNT)
commandPlay =  "shell monkey -p " + PACKAGE_NAME + " --throttle 1000 --pct-touch 20 --pct-motion 20 --pct-trackball 20 --pct-nav 20 --pct-majornav 20 -c android.intent.category.LAUNCHER " + str(DURATION) +" --ignore-timeouts --kill-process-after-error"

#ADB           shell monkey --throttle 1000 --pct-touch 20 --pct-motion 20 --pct-trackball 20 --pct-nav 20 --pct-majornav 20 -p com.pixowl.tsb2 -v "DURATION --ignore-timeouts --kill-process-after-error

#ADB           shell monkey 

commandStop = "shell am force-stop " + PACKAGE_NAME
commandMonkeyStop = "shell ps | awk '/com\.android\.commands\.monkey/ { system(\"adb shell kill \" $2) }'"


myDevices = getDevices()
for i in range(0,ITERATIONS):
    t = i * DURATION
    print ("t = " + str(t)  + " runCicle ")
    Timer( t, runCicle, ()).start()
#Timer(10, print_time, ()).start()
#Timer(15, print_time, ()).start()

#runCommandAllDevices(commandPlay, myDevices)




#print ("sleep for " + str(MIN_FIRST_LAUNCH * 60.0))
#runCommand(commandStop)   


# print ("myDevices = " + ", ".join(myDevices))

# for device in myDevices :
#     print ("device: " + device)





#runCommand(commandStop)
#runCommand(commandUnistall)

#don't work on jenkins
#runCommand(commandInstall)

#runCommand(commandPlay)
#print ("sleep for " + str(MIN_FIRST_LAUNCH * 60.0))
#runCommand(commandStop)   
#for i in range(ITERATIONS-1):
#    runCommand(commandPlay)
#print ("END adbCommand.py")
