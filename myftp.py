from ftplib import FTP

directory = "/"

def premenue():
    print("***********************************CHOOSE FTP *****************************************")
    print("|------------------------------1) DEBIAN----------------------------------------------|")
    print("|------------------------------2) KALI LINUX------------------------------------------|")
    print("|------------------------------3) UBUNTU----------------------------------------------|")
    print("|------------------------------4) ENTER FTP MANUALLY----------------------------------|")
    print("|                              5) ADD FTP TO LIST                                     |")
    print("************************************Make a choice:************************************")
    print("**************************************************************************************\n")


def mainmenue():
    print("|***************************************MY FTP ****************************************")
    print("|------------------------------1) CONNECT TO ANOTHER FTP-------------------------------|")
    print("|------------------------------2) LIST ------------------------------------------------|")
    print("|------------------------------3) CHANGE DIRECTORY-------------------------------------|")
    print("|------------------------------4) DOWNLOAD FILE----------------------------------------|")
    print("|                        You are in this directory: /"                                   )
    print("************************************Make a choice:**************************************")
    print("**************************************************************************************\n")



def connecttoftp():
    choice = raw_input()
    if choice == "1":
        ipaddress = "ftp.debian.org"
        username = "anonymous"
        password = "anonymous"
        ftp = FTP(ipaddress, username, password)
        print("You choose: " + ipaddress)
        print(username + " connecting to: " + ipaddress)
        print("**************************************************************************************")
        print("Press Enter to return to menu")
        returntomainmenu()
        return ftp
    elif choice == "2":
        ipaddress = "ftp.halifax.rwth-aachen.de"
        username = "anonymous"
        password = "anonymous"
        ftp = FTP(ipaddress, username, password)
        print("You choose: " + ipaddress)
        print(username + " connecting to: " + ipaddress)
        print("**************************************************************************************")
        print("Press Enter to return to menu")
        returntomainmenu()
        return ftp
    elif choice == "3":
        ipaddress = "http://ftp.uni-erlangen.de/"
        username = "anonymous"
        password = "anonymous"
        ftp = FTP(ipaddress, username, password)
        print("You choose: " + ipaddress)
        print(username + " connecting to: " + ipaddress)
        print("**************************************************************************************")
        print("Press Enter to return to menu")
        returntomainmenu()
        return ftp
    elif choice == "4":
        print"Enter Address Format: ftp.xxxxx.xx"
        ipaddress = raw_input()
        print("Enter username: (default user is anonmyous)")
        username = raw_input()
        print("Enter Password:"("default password is anonymous"))
        password = raw_input()
        ftp = FTP(ipaddress, username, password)
        print(username + " connecting to: " + ipaddress)
        print("**************************************************************************************")
        print("Press Enter to return to menu")
        returntomainmenu()
        return ftp

def connectanotherftp():
    ipaddress = setipaddress()
    username = setusername()
    password = setpassword()
    ftp = FTP(ipaddress, username, password)
    print(username + " connecting to: " + ipaddress)
    print("**************************************************************************************")
    returntomainmenu()
    return ftp

def listdirectory(ftp):
    ftp.dir()
    print("**************************************************************************************")
    print("Press Enter to return to menu")
    returntomainmenu()

def changedirectory(ftp):
    global directory
    directory = setdirectory()
    ftp.cwd(directory)
    ftp.retrlines("LIST")
    print("You are in this directory: /"+directory)
    print("**************************************************************************************")
    print("Press Enter to return to menu")
    returntomainmenu()

def downloadfile(ftp):
    print("Enter Filename to download")
    directory_local = "C:\TEMP\TEST\\"
    filename = raw_input()
    file = open(directory_local + filename)
    ftp.retrbinary('RETR'+filename, file.write())
def setipaddress():
    print"Enter Address Format: ftp.xxxxx.xx"
    try:
        ipaddress = raw_input()
    except ValueError:
        print("False Format")
    return ipaddress

def setusername():
    print("Enter username: (default user is anonmyous)")
    try:
        username = raw_input()
    except ValueError:
        print("User not valid")
    return username

def setpassword():
    print("Enter Password:"("default password is anonymous"))
    try:
        password = raw_input()
    except ValueError:
        print("Password not valid")
    return password

def setdirectory():
    print("Enter directory:")
    try:
        directory = raw_input()
    except ValueError:
        print("Directory unknown")
    return directory

def returntomainmenu():
    raw_input()
    mainmenue()


def main():

    premenue()
    ftp = connecttoftp()


    while(True):
        choice = raw_input()

        if choice == "1":
            connectanotherftp(ftp)
        elif choice == "2":
            listdirectory(ftp)
        elif choice == "3":
            changedirectory(ftp)
        elif choice == "4":
            downloadfile(ftp)

main()








