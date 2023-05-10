import os
import shutil
from pydub import AudioSegment

# get the current working directory
cwd = r"C:\\Users\\gamal\Desktop\\MC_Sounds\sounds\\mob\\cow"

def convert_ogg_to_wav(path, dest):
    song = AudioSegment.from_ogg(path)
    song.export(dest, format="wav")

#loop through all the directories and files in the current working directory
for root, dirs, files in os.walk(cwd):
    # loop through all the files in the current directory
    for file in files:
        # if the file name contains "hurt" or "death"
        if "ogg" in file:
            # get the full path of the file
            filePath = os.path.join(root, file)
            # create a new directory with the same name as the directory of the file in the new directory
            newDirPath = root
            # copy the file to the new directory and rename it to the same name as the directory its in
            convert_ogg_to_wav(filePath, os.path.join(newDirPath, os.path.splitext(file)[0]+".wav"))
            # print the file path
            print(filePath)
            # remove the ogg file
            # os.remove(os.path.join(root, file))
            # save the file in the desktop
            shutil.move(os.path.join(root, file), r"C:\\Users\\gamal\\Desktop")

        if "wav" in file:
            # make the file 16-bit WAV file
            sound = AudioSegment.from_wav(os.path.join(root, file))
            sound = sound.set_frame_rate(16000)
            # sound = sound.set_channels(1)
            sound = sound.set_sample_width(2)
            sound.export(os.path.join(root, file), format="wav")
            print(os.path.join(root, file))
            


