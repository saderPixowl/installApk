import subprocess
import os
import time
import sys
import datetime

import time
from threading import Timer
import threading
from time import sleep


#pochIO.py

def getDate():
    day = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)

    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    date = day + "-" + month + "-" + year 
    time = hour + ":" + minute + ":" + second 
    return date + "_" + time 
 
    
#def loggin(text):
#    logginTo(text, logFile)
    
def createFile(filename):
    tf = open(filename,"w+")
    tf.write("create " + filename)
    tf.close() 


def loggin(text, filename):
    f = open(logFile,"a") 
    #print(text)
    text = text + "\n"
    text = text.encode('utf-8')
    f.write(text)
    f.close()




def runCommand(command, device):
    time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + ":" + str(datetime.datetime.now().microsecond) 
    entireCommand = "adb -s "+device +" " + command 
    loggin("runCommand("+time+")("+command[0:80]+", "+device+")" , logFile)

    #loggin(entireCommand)

    p = subprocess.Popen((entireCommand).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'))

def runLogcatAllDevices(devices ) :
    threads = list()
    for device in devices:
        t = threading.Thread(target=runLogcat, args=(device,))
        threads.append(t)
        t.start()

def runLogcat(device):
    time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + ":" + str(datetime.datetime.now().microsecond) 
    entireCommand = "adb -s "+ device +" logcat -v time -d"

    loggin(entireCommand, logFile)

    p = subprocess.Popen((entireCommand).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    gameName = PACKAGE_NAME.split(".")[2]




# def createFile(filename):
#     tf = open(filename,"w+")
#     tf.write("create " + filename)
#     tf.close() 


# def loggin(text, filename):
#     f = open(logFile,"a") 
#     #print(text)
#     text = text + "\n"
#     text = text.encode('utf-8')
#     f.write(text)
#     f.close()



    fileName = "log_" + gameName + "_" +getDate() + "_"  + device  + ".logcat" 
    #createFile(fileName)
    #print ("fileName " + fileName )
    tf = open(fileName,"w+")



    for line in iter(p.stdout.readline, b''):
        #print(line.decode('utf-8'))
#        tf.write(line.decode('utf-8'))
        tf.write(line)
    tf.close() 
    entireCommand = "adb -s "+ device + " logcat -c"

    p = subprocess.Popen((entireCommand).split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
  #  for line in iter(p.stdout.readline, b''):
  #      print(line.decode('utf-8'))
    


    #print ("end command output ")

def runCommandAllDevices(command, devices ) :
    threads = list()
    for device in devices:
        t = threading.Thread(target=runCommand, args=(command,device,))
        threads.append(t)
        t.start()

def runMonkeyWithLogcatAllDevices(command, devices):
    threads = list()
    for device in devices:
        t = threading.Thread(target=runMonkeyWithLogcat, args=(command,device,))
        threads.append(t)
        t.start()



def getDevices():
    loggin("getDevices()", logFile)
    commandDevices = "devices"
    devicesList = []
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
            loggin("devicesList +=" + deviceLine, logFile)
    return devicesList

def runCicle():
    loggin("runCicle()", logFile)
    loggin("time: " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second), logFile)
    runCommandAllDevices(commandPlayResetDeviceSettings, myDevices)
    sleep(2.0)
    #runCommandAllDevices(commandStopResetDeviceSettings, myDevices)
    runCommandAllDevices(commandStop, myDevices)
    runCommandAllDevices(commandStopAllApps, myDevices)
    #runCommandAllDevices(commandLogcat, myDevices, True)
    
    
   # runCommandAllDevices(commandPlay, myDevices)
    runLogcatAllDevices(myDevices)

    #runMonkeyWithLogcatAllDevices(commandPlay, myDevices)
    # runCommandAllDevices(commandStop, myDevices)
    # runCommandAllDevices(commandPlay, myDevices)

def stopAll():
    loggin("stopAll()", logFile)
    runCommandAllDevices(commandStop, myDevices)

def awakeAll():
    loggin("awakeAll()", logFile)
    runCommandAllDevices(commandAwake, myDevices)

def unistallAll():
    loggin("unistallAll()", logFile)
    runCommandAllDevices(commandUnistall, myDevices)

def installAll():
    loggin("installAll()", logFile)
    runCommandAllDevices(commandInstall, myDevices)

def reinstallAll():
    loggin("reinstallAll()", logFile)
    runCommandAllDevices(commandReinstall, myDevices)
    
def installResetApkAll():
    loggin("installResetApkAll()", logFile)
    runCommandAllDevices(commmandInstallReset, myDevices)



    

if (len(sys.argv) < 3):
    print ("Error: wrong number of paramters")
    print ("Usage: 'python adbCommands.py package_name eventCount(int) iterations duration_of_iterations(seconds)'")
    sys.exit(-1) 
else:
    PACKAGE_NAME = sys.argv[1]
    #EVENT_COUNT = int(sys.argv[2])
    ITERATIONS = int(sys.argv[2])
    DURATION = int(sys.argv[3])
    GAMEAPK = "game.apk"
    onlyInstall = not True
    reinstall = True

    logFile = "log_" + PACKAGE_NAME.split(".")[2] +"_"+ getDate() + ".txt"
    createFile(logFile)
    # f = open(logFile,"w+")
    # f.write("INIT LOG ")
    # f.close() 
    loggin("init (PACKAGE_NAME:" + str(PACKAGE_NAME)+" ITERATIONS:"+str(ITERATIONS)+ " DURATION:" + str(DURATION),logFile )
#commandPlay = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER " + str(EVENT_COUNT)


resetDeviceSettingsPackage      = "com.pixowl.resetdevicesettings"
resetDeviceSettingsApk          = "resetDeviceSettings/app/build/outputs/apk/debug/app-debug.apk"

commmandInstallReset            = "install -t " + resetDeviceSettingsApk
commandInstall                  = "install " + GAMEAPK
commandReinstall                = "install -r " + GAMEAPK
commandUnistall                 = "uninstall " + PACKAGE_NAME


#commandLogcat                   = "shell logcat -d > peron.txt"
commandStopResetDeviceSettings  = "shell am force-stop " + resetDeviceSettingsPackage
commandPlayResetDeviceSettings  = "shell monkey -p " + resetDeviceSettingsPackage + " -c android.intent.category.LAUNCHER 1"
commandStopAllApps              = 'shell ps|grep -v root|grep -v system|grep -v NAME|grep -v shell|grep -v smartcard|grep -v androidshmservice|grep -v bluetooth|grep -v radio|grep -v nfc|grep -v "com.android."|grep -v "android.process."|grep -v "com.google.android."|grep -v "com.sec.android."|grep -v "com.google.process."|grep -v "com.samsung.android."|grep -v "com.smlds" | xargs adb shell kill'
commandPlayFirst                = "shell monkey -p " + PACKAGE_NAME + " -c android.intent.category.LAUNCHER 1"
commandPlay                     = "shell monkey -p " + PACKAGE_NAME + " --throttle 100 --pct-touch 20 --pct-motion 20 --pct-trackball 20 --pct-nav 20 --pct-majornav 20 --pct-syskeys 0 -c android.intent.category.LAUNCHER --ignore-timeouts --kill-process-after-error " + str(DURATION*10)
commandAwake                    = "shell input keyevent KEYCODE_WAKEUP"
commandStop                     = "shell am force-stop " + PACKAGE_NAME
commandMonkeyStop               = "shell ps | awk '/com\.android\.commands\.monkey/ { system(\"adb shell kill \" $2) }'"

myDevices = getDevices()


#installResetApkAll()
if (onlyInstall):
    if (reinstall):
        reinstallAll()
    else:
        unistallAll()
        installAll()
else:
    t = 0
    for i in range(0,ITERATIONS):
    #     #print ("t = " + str(t)  + " runCicle ")
        loggin("t = " + str(t)  + " runCicle ", logFile)
        Timer( t, runCicle, ()).start()
        t = (i+1) * DURATION

    loggin("t = " + str(t)  + " runCicle ", logFile)
    Timer( t, stopAll, ()).start()


