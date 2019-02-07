import subprocess
import os
import time
import sys
import datetime

import time
from threading import Timer
import threading

logFile = "log_" + str(datetime.datetime.now().day) +"-"+str(datetime.datetime.now().month) +"-"+str(datetime.datetime.now().year) +"_"+  str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + ".txt"
f = open(logFile,"w+")
f.write("INIT LOG ")
f.close() 


    
def loggin(text):
    f = open(logFile,"a") 
    print(text)
    f.write(text + "\n")
    f.close()

def runCommand(command, device):
    time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + ":" + str(datetime.datetime.now().microsecond) 
    loggin("runCommand("+time+")("+command+", "+device+")")

    print ("run command adb -s "+device +" " + command )

    p = subprocess.Popen(("adb -s "+device +" " + command).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))
    #print ("end command output ")

def runCommandAllDevices(command, devices):
    threads = list()
    for device in devices:
        #loggin("runCommandAllDevices("+command+", "+device+")")
    
        #print("- - - - - - - - command = " + command + " device " + device)
        #runCommand(command, device)
        t = threading.Thread(target=runCommand, args=(command,device,))
        threads.append(t)
        t.start()



def getDevices():
    loggin("getDevices()")
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
            loggin("devicesList +=" + deviceLine)
    return devicesList

def runCicle():
    loggin("runCicle()")
   # print("time = " + datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
   # print("time: " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second))
    loggin("time: " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second))
    runCommandAllDevices(commandStop, myDevices)
    runCommandAllDevices(commandPlay, myDevices)
    # runCommandAllDevices(commandStop, myDevices)
    # runCommandAllDevices(commandPlay, myDevices)

def stopAll():
    loggin("stopAll()")
    runCommandAllDevices(commandStop, myDevices)

def awakeAll():
    loggin("awakeAll()")
    runCommandAllDevices(commandAwake, myDevices)



def print_time():
    print("TIMERRRR")

def unistallAll():
    loggin("unistallAll()")
    runCommandAllDevices(commandUnistall, myDevices)

def installAll():
    loggin("installAll()")
    runCommandAllDevices(commandInstall, myDevices)





if (len(sys.argv) < 3):
    print ("Error: wrong number of paramters")
    print ("Usage: 'python adbCommands.py package_name eventCount(int) iterations duration_of_iterations(seconds)'")
    sys.exit(-1) 
else:
    PACKAGE_NAME = sys.argv[1]
    #EVENT_COUNT = int(sys.argv[2])
    ITERATIONS = int(sys.argv[2])
    DURATION = int(sys.argv[3])
    loggin("init (PACKAGE_NAME:"+str(PACKAGE_NAME)+" ITERATIONS:"+str(ITERATIONS)+ " DURATION:" + str(DURATION))
#commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER " + str(EVENT_COUNT)
commandInstall = "install game.apk"
commandUnistall = "uninstall " + PACKAGE_NAME
commandPlayFirst = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
commandPlay =  "shell monkey -p " + PACKAGE_NAME + " --throttle 100 --pct-touch 20 --pct-motion 20 --pct-trackball 20 --pct-nav 20 --pct-majornav 20 --pct-syskeys 0 -c android.intent.category.LAUNCHER --ignore-timeouts --kill-process-after-error " + str(DURATION*10)

commandAwake = "adb shell input keyevent KEYCODE_WAKEUP"
commandStop = "shell am force-stop " + PACKAGE_NAME
commandMonkeyStop = "shell ps | awk '/com\.android\.commands\.monkey/ { system(\"adb shell kill \" $2) }'"



myDevices = getDevices()

onlyInstall = True


if (onlyInstall):
    unistallAll()
    installAll()
else:
    t = 0
    for i in range(0,ITERATIONS):
    #     #print ("t = " + str(t)  + " runCicle ")
        loggin("t = " + str(t)  + " runCicle ")
        Timer( t, runCicle, ()).start()
        t = (i+1) * DURATION

    loggin("t = " + str(t)  + " runCicle ")
    Timer( t, stopAll, ()).start()


