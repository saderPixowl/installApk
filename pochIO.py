#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hua:p:i:d:",["apk=","package=", "iterations=", "duration="])
   except getopt.GetoptError:
      printHelp()
      sys.exit(2)
   package_name = ""
   iterations = ""
   duration = ""
   gameapk = ""
   unistall = False

   for opt, arg in opts:
      if opt in ("-h", "--help"):
         printHelp()
         sys.exit()
      elif opt in ("-a", "--apk"):
         gameapk = arg
      elif opt in ("-p", "--package"):
         package_name = arg
      elif opt in ("-i", "--iterations"):
         iterations = arg
      elif opt in ("-d", "--duration"):
         duration = arg
      elif opt in ("-u", "--unistall"):
         unistall = True

   if(not(package_name and iterations and duration)) :
      print ("ERROR!!!!")
      printHelp()
      sys.exit()

   print("package_name ", package_name)
   print("iterations ", iterations)
   print("duration ", duration)
   print("gameapk ", gameapk)
   print("unistall ", unistall)

def printHelp():
   print ('usage :')
   print ('\tpochI.py -h -u -a <apk> -p <package> -i <iterations> -d <duration>')
   print ('optional :')
   print ('\t-h --help \t\t\t: this help')
   print ('\t-a --apk \t\t\t: apk to re install, combine with -u to fresh install')
   print ('\t-u --unistall \t\t\t: fresh install , use only with -a')
   print ('mandatory :')
   print ('\t-p --package \t\t\t: package to run (com.pixowl.tsb2 | com.activision.peanuts | com.pixowl.goosebumps etc...)')
   print ('\t-i --iterations \t\t: # of iterations')
   print ('\t-d --duration \t\t\t: time(approx) in seconds of a iteration')




      


if __name__ == "__main__":
   main(sys.argv[1:])