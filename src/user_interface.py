import Tkinter
import wave
from graph import *

from src.file_loader import File_Loader


class User_Interface(Tkinter.Tk):

    currentAudioFilePath = ""

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        #self.parent = parent
        #self.initialize()
        self.root = self

    #def initialize(self):
        self.grid()

        #self.entry = Tkinter.Entry(self)
        #self.entry.grid(column=1,row=0,sticky='NSEW')
        #self.entry.bind("<Return>", self.OnPressEnter)

        loadButton = Tkinter.Button(self,text="Load",
                                command=self.LoadButtonClick)
        loadButton.grid(column=0,row=0)

        startButton = Tkinter.Button(self,text="Start",
                                command=self.StartButtonClick)
        startButton.grid(column=0,row=1)


        # self.graphLabel = Tkinter.StringVar()
        # label3 = Tkinter.Label(self,textvariable=self.graphLabel,
        #                       anchor="w",fg="black",bg="green")

        # label3.grid(column=1,row=0,sticky='NSEW')
        # self.graphLabel.set("Graph Here")


        ######BROKEN######
        self.graphCanvas = Graph().getGraph(self)
        print self
        #self.graphCanvas.show()
        self.graphCanvas.get_tk_widget().grid(column=1,row=0,sticky='NSEW')
        #self.graphCanvas.grid(column=1,row=0,sticky='NSEW')
        ##################





        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="red")
        label.pack()
        label.grid(column=1,row=1,sticky='NSEW')


        self.labelVariable2 = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.labelVariable2,
                               anchor="w",fg="black",bg="blue")
        label2.grid(column=1,row=2,sticky="NSEW")

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=7)
        self.grid_rowconfigure(0,weight=10)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=2)


        self.resizable(True,False)


        #Fullscreen
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))







    def LoadButtonClick(self):
        self.labelVariable.set("Loading...")
        self.root.update()
        self.currentAudioFilePath = File_Loader().loadMP3()
        self.labelVariable.set("Loaded")



    def StartButtonClick(self):
        self.labelVariable.set("Starting...")
        wr = wave.open(self.currentAudioFilePath, 'r')
        nchannels, sampwidth, framerate, nframes, comptype, compname =  wr.getparams()
        self.labelVariable2.set(str(framerate) + "")
        self.labelVariable.set("Finished")


    def OnPressEnter(self,event):
        print "enter"
