# loop through all the files in the directory and get the sound files with name contains "break"
# and copy them to the new directory

import os
import shutil

# get the current working directory
cwd = r"C:\Users\gamal\Desktop\MC_Sounds\sounds"
# get the new directory
newDir = r"C:\Users\gamal\Desktop\MC_Sounds\Other"

# loop through all the directories and files in the current working directory
for root, dirs, files in os.walk(cwd):
    # loop through all the files in the current directory if the path of the file does not contain "dig" or "block" or "entity" or "mob"
    if "dig" not in root and "block" not in root and "entity" not in root and "mob" not in root:
        for file in files:
            # if the file name not contains "hurt" or "death" or "break"
                # get the full path of the file
            filePath = os.path.join(root, file)
            # create a new directory with the same name as the directory of the file in the new directory
            newDirPath = newDir
            # copy the file to the new directory and rename it to the same name as the directory its inshutil.copy(filePath, os.path.join(newDirPath, str(len(os.listdir(newDirPath))) + ".ogg"))
            shutil.copy(filePath, os.path.join(newDirPath, os.path.basename(root)+" "+str(len(os.listdir(newDirPath))) + ".ogg"))
            # print the file path
            print(filePath)
            




print("Done")