#!/usr/bin/python

import argparse as ap
import getpass
import paramiko

def SSHConnect(ipaddress):
    username = input("Enter the username for the account you wish to log into: ")
    password = getpass.getpass("Enter the password for the account you wish to log into: ")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ipaddress, username=username, password=password)

    return ssh_client


def findFiles(ssh_client:paramiko.SSHClient):
    pass
    #needs to return a list of files and the username of the person we looked at
    #should also print the names of the files and date modified (we should have the logic for this since we did it in a previous lab)

    #need to prompt for both the password for the sender email and the password (and username I guess, its not specified
    # in the assignment details) for the compromised machine we are connecting to.
def sendEmail(senderEmail, recipientEmail, ctoFlag=False):
    pass

    #needs to send an email to recipient (and the cto if the option is present at execution) with
    #file names and user who was impacted

def downloadFiles(whereToDownload=""):
    pass
    #check if whereToDownload is still blank, if it is: download in home dir, if not: download in specified dir
    #probably needs to use sftpp get? not sure tbh but I think so

def get_parser():
    parser = ap.ArgumentParser(
                                prog="CompFileIdentifier",
                                usage="./FinalProjectScripting.py [-d directoryName] [-c]",
                                add_help=True)

    parser.add_argument("-d", "--download", action="store", dest="dir_Name",
                        help="specifies the directory into which the smallest file will be download if this option is "
                             "present. If not present, download the affected file to the current user's home directory")

    parser.add_argument("-c", "--cto", action="store_true", default=False, dest="cto_Flag",
                        help="If this option is present, include the CTO as and additional recipient of the email.")
    parser.add_argument("SENDER_EMAIL", action="store", type=str, help="blah")
    parser.add_argument("RECIPIENT_EMAIL", action="store", type=str, help="blah")
    parser.add_argument("IP", action="store", type=str, help="blah")

    return parser


def main():
    myParser = get_parser()
    parserResult = myParser.parse_args()
    try:
        if parserResult.dir_Name is not None:
            pass

        if parserResult.cto_Flag:
            #set cto flag to true
            pass

    except Exception as ex:
        print(f"Invalid option: {ex}")


if __name__ == "__main__":
    main()
