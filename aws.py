import os
import subprocess

def clearscr():
    x = subprocess.getstatusoutput("cls")
    if x[0] != 0:
        x = subprocess.getstatusoutput("clear")
        print(x[1])
    else:
        os.system("cls")
def startingmsg():
    clearscr()
    print("                  AMAZON WEB SERVICES                  ")
    print("-------------------------------------------------------\n")
def cmd_run(cmd):
    x = subprocess.getstatusoutput(cmd)   
    if x[0] == 0 :
        print("command executed successfully")
    else :
        print("Some error occured => {}".format(x[1]))
        print("Please try again by doing changes")   
def createBucket():
    bucketName = input("    Enter bucket name: ")
    bucketRegion = input("    Enter region where this bucket to be created: ")
    cmd = "aws s3api create-bucket --bucket {} --region {}".format(bucketName, bucketRegion)
    cmd_run(cmd)
def deleteBucket():
    bucketName = input("    Enter bucket name to be delete: ")
    bucketRegion = input("    Enter region where this bucket is present: ")
    cmd = "aws s3api delete-bucket --bucket {} --region {}".format(bucketName, bucketRegion)
    cmd_run(cmd)   
def uploadFileToBucket():
    filePathLocal = input("    Enter file path from which file to be copy: ")
    bucketName = input("    Enter bucket name: ")
    name = input("    Enter name of file: ")
    access = input("    Enter permissions: ")
    cmd = "aws s3 cp {}  s3://{}/{} --acl {}".format(filePathLocal, bucketName, name, access)
    cmd_run(cmd)
def deleteFileFromBucket():  
    bucketName = input("    Enter bucket name: ")
    name = input("    Enter name of file: ")
    cmd = "aws s3 rm s3://{}/{}".format(bucketName, name)
    cmd_run(cmd)
def createCloudFront():
    origin = input("    Enter origin Domain: ")
    cmd= "aws cloudfront create-distribution --origin-domain-name {}".format(origin)
    cmd_run(cmd)
def deleteCloudFront():
    cloudfrontID = input("    Enter the ID of cloudfront: ")
    eTag = input("    Enter ETag header value: ")
    cmd = "aws cloudfront delete-distribution --id {} --if-match {}".format(cloudfrontID, eTag)
    cmd_run(cmd)
def describeInstances():
    os.system("aws ec2 describe-instances")
def launchInstance():
    imgID = input("    Enter image ID: ")
    imgType = input("    Enter instance type: ")
    keyPair = input("    Enter key pair name: ")
    cmd =  "aws ec2 run-instances --image-id {} --instance-type {} --key-name {}".format(imgID, imgType, keyPair)
    cmd_run(cmd)
def startInstance():
    insID = input("    Enter instance ID which is to be start: ")
    cmd = "aws ec2 start-instances --instance-ids {}".format(insID)
    cmd_run(cmd)
def stopInstance():
    insID = input("    Enter instance ID which is to be stop: ")
    cmd = "aws ec2 stop-instances --instance-ids {}".format(insID)
    cmd_run(cmd)
def rebootInstance():
    insID = input("    Enter instance ID which is to be reboot: ")
    cmd = "aws ec2 reboot-instances --instance-ids {}".format(insID)
    cmd_run(cmd) 
def terminateInstance():
    insID = input("    Enter instance ID which is to be terminated: ")
    cmd = "aws ec2 terminate-instances --instance-ids {}".format(insID)
    cmd_run(cmd) 
def createVolume():
    print("    To create volume =>...")
    volumeType = input("    Enter volume type: ")
    volumeSize = input("    Enter volume size: ")
    volumeZone = input("    Enter availability-zone: ")
    cmd = "aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(volumeType, volumeSize, volumeZone)
    cmd_run(cmd)
def deleteVolume():
    volumeID = input("    Enter volume id which is to be deleted: ")
    cmd = "aws ec2 delete-volume --volume-id {} ".format(volumeID)
    cmd_run(cmd)
def attachVolume():
    volumeID = input("    Enter volume id which is to be attach: ")
    insID = input("    Enter instance ID to which this volume to be attach: ")
    device = input("    Enter device name: ")
    cmd = "aws ec2 attach-volume --volume-id {} --instance-id {} --device {} ".format(volumeID, insID, device)
    cmd_run(cmd)
def detachVolume():
    volumeID = input("    Enter volume id which is to be detached: ")
    cmd = "aws ec2 detach-volume --volume-id {} ".format(volumeID)
    cmd_run(cmd)
def deleteSnapshot():
    ssID = input("    Enter snapshot id which is to be deleted: ")
    cmd = "aws ec2 delete-snapshot --snapshot-id {} ".format(ssID)
    cmd_run(cmd)
def createSnapshot():
    vol = input("    Enter volume id whose snapshot is to be created: ")
    desc = input("    Enter its description: ")
    cmd = "aws ec2 create-snapshot --volume-id {} --description  {} ".format(vol, desc)
    cmd_run(cmd)
def createSG():
    name = input("    Enter Security-Group name which is to create: ")
    desc = input("    Enter {} description: ".format(name))
    cmd = "aws ec2 create-security-group --group-name {} --description {}".format(name, desc)
    cmd_run(cmd)
def deleteSG():
    choice3 = int(input("    Want to delete Security group by- 1.name 2.id: "))
    if choice3 == 1:
        name = input("    Enter Security-Group name which is to delete: ")
        cmd = "aws ec2 delete-security-group --group-name {}".format(name)
    else:
        sgId = input("    Enter Security-Group ID which is to delete: ")
        cmd = "aws ec2 delete-security-group --group-id {}".format(sgId)
    cmd_run(cmd)
def createKeyPair():
    name = input("    Enter Key pair name which is to create: ")
    cmd = "aws ec2 create-key-pair --key-name {}".format(name)
    cmd_run(cmd)
def deleteKeyPair():
    name = input("    Enter Key pair name which is to delete: ")
    cmd = "aws ec2 delete-key-pair --key-name {}".format(name)
    cmd_run(cmd)
def instances():
    print("""    Please enter
    1. Launch a new instance
    2. Start a instance
    3. Stop a instance
    4. Reboot a instance
    5. Terminate a instance
    6. To describe instances
    7. exit
    => """, end = "") 
    choice2 = int(input())
    startingmsg()
    if choice2 == 1:
        launchInstance()
    elif choice2 == 2:
        startInstance()
    elif choice2 == 3:
        stopInstance()
    elif choice2 == 4:
        rebootInstance()
    elif choice2 == 5: 
        terminateInstance()
    elif choice2 == 6:
        describeInstances()
    elif choice2 == 7:
        return
    else:
        print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
        instances()
    return
def elasticBlockStorage():
    print("""    Please enter
    1. To create a volume
    2. To delete a volume
    3. To attach a volume
    4. To detach a volume
    5. To create a snapshot
    6. To delete a snapshot
    7. exit
    => """, end = "") 
    choice2 = int(input())
    startingmsg()
    if choice2 == 1:
        createVolume()
    elif choice2 == 2:
        deleteVolume()
    elif choice2 == 3:
        attachVolume()
    elif choice2 == 4:
        detachVolume()
    elif choice2 == 5: 
        createSnapshot()
    elif choice2 == 6: 
        deleteSnapshot()
    elif choice2 == 7:
        return
    else:
        print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
        elasticBlockStorage()
    return
def networkSecurity():
    print("""    Please enter
    1. To create a Security group
    2. To delete a Security froup
    3. To create Key-pair
    4. To delete a Key-pair
    5. exit
    => """, end = "") 
    choice2 = int(input())
    startingmsg()
    if choice2 == 1:
        createSG()
    elif choice2 == 2:
        deleteSG()
    elif choice2 == 3:
        createKeyPair()
    elif choice2 == 4:
        deleteKeyPair()
    elif choice2 == 5: 
        return
    else:
        print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
        networkSecurity()
    return
def awsStart():

    x = subprocess.getstatusoutput("aws help")
    if x[0] != 0:
        print("Sorry, looks like yous system don't have aws cli install")
        return
    x = subprocess.getstatusoutput("aws configure get aws_access_key_id")
    if x[0] != 0:
        print("Please configure AWS CLI\n")
        os.system("aws configure")


    startingmsg()
    while True:
        print("""    1. EC2 service
    2. S3 service
    3. Cloud front service
    4.exit
    Please select one of the option""", end = ": ")
        choice = int(input())
        startingmsg()
        if choice == 1:
            while True:
                print("""    Please enter
    1. To perform operations on Instances
    2. To perform operations on Elastic Block Storage
    3. To perform operation on Network & Security
    4. exit
    => """, end = "")
                choice1 = int(input())
                startingmsg()
                if choice1 == 1:
                    instances()
                elif choice1 == 2:
                    elasticBlockStorage()
                elif choice1 == 3:
                    networkSecurity()
                elif choice1 == 4:
                    break
                else:
                    print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
                    continue
                break
        elif choice == 2:
            while True:
                print("""    Please enter
    1. To create a bucket
    2. To delete a bucket
    3. To upload file to a bucket
    4. To delete file from a bucket
    5. exit
    => """, end = "")
                choice1 = int(input())
                startingmsg()
                if choice1 == 1:
                    createBucket()
                elif choice1 == 2:
                    deleteBucket()
                elif choice1 == 3:
                    uploadFileToBucket()
                elif choice1 == 4:
                    deleteFileFromBucket()
                elif choice1 == 5: 
                    break
                else:
                    print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
                    continue
                break
        elif choice == 3:
            while True:
                print("""    Please enter
    1. To create cloud front
    2. To delete cloud front
    3. exit
    => """, end = "")
                choice1 = int(input())
                startingmsg()
                if choice1 == 1:
                    createCloudFront()
                elif choice1 == 2:
                    deleteCloudFront()
                elif choice1 == 3: 
                    break
                else:
                    print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
                    continue
                break
        elif choice == 4:
            break
        else:
            print("Sorry, you have enter wrong choice. Please enter a correct choice\n")
            continue
        break
    input("Press Enter to exit...")
    clearscr()
awsStart()