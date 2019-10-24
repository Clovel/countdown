form datetime import datetime, date
from time import sleep
import sys, os

CURSOR_UP_ONE = "\x1b[1A"
ERASE_LINE = "\x1b[2K"

def usage():
    print "[USAGE] This program counts down to the date specified in the argument"
    print "            - arg1 : \"YYYY-MM-DD hh:mm::ss:f\""
    print "        Beware ! 00:00:00.000 is the beginning of the day, not the end. "

def processArgs():
    argc = len(sys.argv)
    print "[DEBUG] argc = " + str(argc)
    if(1 >= argc):
        print "[ERROR] <processArgs> No arguments were given to the program !"
        usage()
        exit(1)
    elif(2 < argc):
        print "[ERROR] <processArgs> Too many arguments were given to the program"
        usage()
        exit(1)
    else:
        arg = sys.argv[1]
        print "[DEBUG] <processArgs> Good argument found : " + str(arg)
        return arg
    return None

def clearLine():
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

def clearConsole():
    os.system("cls") # For Windows
    #os.system("clear") # For Linux & macOS

def dateDiff(d1, d2):
    return abs(d2 - d1)

def main():
    # Process arguments
    goalStr = processArgs()
    if(None == goalStr):
        print "[ERROR] Got no date to countdown to !"
        exit(1)

    try:
        goal = datetime.strptime(goalStr, "%Y-%m-%d %H:%M:%S:%f")
    except ValueError:
        print "[ERROR] Argument date-time " + goalStr + " is not formated correctly."
        print "        Expected format is YYYY-MM-DD hh:mm:ss.f"
        exit(1)

    # Main routine
    print "[INFO ] Counting down to : " + goal.strftime("%d/%m/%y %H:%M:%S.%f")
    while True:
        today = datetime.today()
        diff = dateDiff(today, goal)
        #clearLine() # Works for bash & unix systems
        #clearConsole() # Works for Windows systems
        print diff
        sleep(1)

if __name__ == "__main__":
    main()
