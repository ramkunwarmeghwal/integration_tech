import os
import subprocess
def clearscr():
    x = subprocess.getstatusoutput("cls")
    if x[0] == 0:
        os.system("cls")
    else:
        os.system("clear")
def startmsg():
    clearscr()
    print("                     Hadoop                     ")
    print("------------------------------------------------\n")

hdfsFile = '''"<?xml version=\\\"1.0\\\"?>
<?xml-stylesheet type=\\\"text/xsl\\\" href=\\\"configuration.xsl\\\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.{}.dir</name>
<value>/{}</value>
</property>
</configuration>"'''

coreFile = '''"<?xml version=\\\"1.0\\\"?>
<?xml-stylesheet type=\\\"text/xsl\\\" href=\\\"configuration.xsl\\\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>"'''

def report():
    os.system("hadoop dfsadmin -report")
def slave():
    print("    Configuring hadoop as Data node on this system")
    print("    please provide following details")
    dirName = input("    Please enter name of folder on which data node to be mount: ")
    os.system("mkdir {}".format(dirName))
    nnIP = input("    Please enter ip_address of name node: ")
    nnport = input("    Please enter port of name node: ")
    hdfs = hdfsFile.format('data', dirName)
    os.system("echo {}| cat > /ect/hadoop/hdfs-site.xml".format(hdfs))
    core = coreFile.format(nnIP, nnport)
    os.system("echo {}| cat > /etc/hadoop/core-site.xml".format(core))
    os.system("systemctl stop firewalld")
    os.system("hadoop-daemon.sh stop datanode")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start datanode")
    if x[0] == 0:
        os.system("hadoop-daemon.sh start datanode")
        clearscr()
        print("    Data node is configure successfully")
    else:
        print("Error occurs =>")
        print(x[1])
def master():
    print("    Configuring hadoop as Name node on this system")
    print("    please provide following details")
    dirName = input("    Please enter name of folder on which name node to be mount: ")
    os.system("mkdir {}".format(dirName))
    nnIP = input("    Please enter ip_address of name node: ")
    nnport = input("    Please enter port of name node: ")
    hdfs =  hdfsFile.format('name', dirName)
    os.system("echo {}| cat > /etc/hadoop/hdfs-site.xml".format(hdfs))
    core = coreFile.format(nnIP, nnport)
    os.system("echo {}| cat > /etc/hadoop/core-site.xml".format(core))
    os.system("systemctl stop firewalld")
    os.system("hadoop namenode -format")
    os.system("hadoop-daemon.sh stop namenode")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start namenode")
    if x[0] == 0:
        os.system("hadoop-daemon.sh start namenode")
        clearscr()
        print("    Name node is configure successfully")
    else:
        print("Error occurs =>")
        print(x[1])
def client():
    print("    Configuring hadoop as client on this system")
    print("    please provide following details")
    nnIP = input("    Please enter ip_address of name node: ")
    nnport = input("    Please enter port of name node: ")
    core = coreFile.format(nnIP, nnport)
    os.system("echo {}| cat > /etc/hadoop/core-site.xml".format(core))
    print("    Client is configure successfully")
def uploadFile():
    file = input("Enter file path: ")
    x = subprocess.getstatusoutput("hadoop fs -put {} /".format(file))
    if x[0] == 0:
        os.system("hadoop fs -put {} /".format(file))
        clearscr()
        print("File uploaded successfully")
    else:
        print("Error occurs =>")
        print(x[1])
def deleteFile():
    file = input("Enter file path: ")
    x = subprocess.getstatusoutput("hadoop fs -rm {}".format(file))
    if x[0] == 0:
        os.system("hadoop fs -rm {}".format(file))
        clearscr()
        print("File deleted successfully")
    else:
        print("Error occurs =>")
        print(x[1])



def hadoopStart():
    x = subprocess.getstatusoutput("java -version")
    if x[0] != 0:
        print("    Sorry, your system don't have jdk install, please install it first")
        input("Press enter to exit...")
        clearscr()
        return
    x = subprocess.getstatusoutput("hadoop version")
    if x[0] != 0:
        print("    Sorry, your system don't have hadoop install, please install it first")
        input("Press enter to exit...")
        clearscr()
        return
    startmsg()
    while True:
        print("""    Enter -
        1. For Namenode
        2. For Datanode
        3. For client 
        4. exit
        => """, end = "")
        user = input()
        startmsg()
        if user == '1':
            print("""    Enter -
        1. To configure Namenode
        2. To see admin report
        3.exit
        => """, end = "")
            choice = input()
            startmsg()
            if choice == '1':
                master()
            elif choice == '2':
                report()
            elif choice == '3':
                break
            else:
                print("Please enter correct option...")
                continue
        elif user == '2':
            print("""    Enter -
        1. To configure Datanode
        2. To see admin report
        3. exit
        => """, end = "")
            choice = input()
            startmsg()
            if choice == '1':
                slave()
            elif choice == '2':
                report()
            elif choice == '3':
                break
            else:
                print("Please enter correct option...")
                continue
        elif user == '3':
            print("""    Enter -
        1. To configure as a client
        2. To see admin report
        3. to upload file
        4. To delete file
        5. exit
        => """, end = "")
            choice = input()
            startmsg()
            if choice == '1':
                client()
            elif choice == '2':
                report()
            elif choice == '3':
                uploadFile()
            elif choice == '4':
                deleteFile()
            elif choice == '5':
                break
            else:
                print("Please enter correct option...")
                continue
        elif user == '4':
            break
        else:
            print("Please enter cotterct option...")
            continue
        break
    input("Press enter to exit...")
    clearscr()
#hadoopStart()
