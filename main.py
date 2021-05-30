#!/usr/bin/env python


import dropbox
import time
import os
from dropbox.files import WriteMode
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    #upload function    
    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                # construct the full local path
                local_path = os.path.join(root,filename)

                #full dropbox path
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))


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
    access_token = ''
    transferData = TransferData(access_token)

    file_from = str(input("Enter the file path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")
    print("Got it transfering data to dropbox")
    print("Please Wait....")
    transferData.upload_file(file_from, file_to)
    def demo(screen):
        effects = [
            Cycle(
                screen,
                FigletText("Hooray", font='big'),
                int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("Uploaded!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
        screen.play([Scene(effects, 500)])

    Screen.wrapper(demo)
    print("Transfer successfully!!")


    # The full path to upload the file to, including the file name
    
    # API v2

main()
