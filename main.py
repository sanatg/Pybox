#!/usr/bin/env python


import dropbox
import time
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    #some theatrics
    print("initiating Pybox.....")
    print("connecting with servers...")
    print("server status [OK]")
    print("establishing a secure connection...")
    print("application status [OK]")
    print("starting.....")
    time.sleep(3)
    print("initialized..")
    print("successfully running....")
    if os.name == 'posix':
        #linux/macosx
        _ = os.system('clear')
    else:
      # for windows platfrom
      _ = os.system('cls')
    #printing Pybox logo
    print("""

    
██████╗░██╗░░░██╗██████╗░░█████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗╚██╗██╔╝
██████╔╝░╚████╔╝░██████╦╝██║░░██║░╚███╔╝░
██╔═══╝░░░╚██╔╝░░██╔══██╗██║░░██║░██╔██╗░
██║░░░░░░░░██║░░░██████╦╝╚█████╔╝██╔╝╚██╗
╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝ dropbox backup

    """)
    #dropbox access token
    access_token = 'qligWObuSOwAAAAAAAAAAXkx70AC3-CdZT3mxdOHJqjmUSBfxs23jZZamrBNBiBE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    transferData.upload_file(file_from, file_to)
    print("Transfer successfully!!")

    # The full path to upload the file to, including the file name
    
    # API v2

if __name__ == '__main__':
    main()
