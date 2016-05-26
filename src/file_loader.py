import Tkinter
from tkFileDialog import askopenfilename


class File_Loader():

    def loadMP3(self):
        currentAudioFilePath = askopenfilename(filetypes=[("Sound files","*.mp3, *.wav")]) # show an "Open" dialog box and return the path to the selected file
        print(currentAudioFilePath)
        return currentAudioFilePath