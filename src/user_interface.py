import Tkinter
from graph import *
from Tkinter import *

from file_loader import File_Loader
#from psk31.psk31decoder2 import psk31_decode


class User_Interface(Tkinter.Tk):

    currentAudioFilePath = ""

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.root = self
        self.root.configure(bg="#3366cc")
        self.grid()

        # BUTTONS
        loadButton = Tkinter.Button(self,text="Load",
                                command=self.LoadButtonClick,highlightbackground="#3366cc")
        loadButton.grid(column=0,row=0)
        startButton = Tkinter.Button(self,text="Start",
                                command=self.StartButtonClick,highlightbackground="#3366cc")
        startButton.grid(column=0,row=1)

        # GRAPH
        self.graphCanvas = Graph().getGraph(self)
        self.graphCanvas.get_tk_widget().grid(column=1,row=0,sticky='NSEW')

        # LABELS
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="#737373")
        label.grid(column=1,row=1,sticky='NSEW')

        self.labelVariable2 = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.labelVariable2,
                               anchor="w",fg="black",bg="#3366cc")
        label2.grid(column=1,row=2,sticky="NSEW")

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=7)
        self.grid_rowconfigure(0,weight=10)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=2)

        self.resizable(True,False)

        # Fullscreen
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))


    def LoadButtonClick(self):
        self.labelVariable.set("Loading...")
        self.root.update()
        self.currentAudioFilePath = File_Loader().loadMP3()
        self.labelVariable.set("Loaded")



    def StartButtonClick(self):
        self.labelVariable.set("Decoding...")
        message = psk31_decode(self.currentAudioFilePath)
        self.labelVariable2.set(message)
        self.labelVariable.set("Finished")

    def OnPressEnter(self,event):
        print "enter"
