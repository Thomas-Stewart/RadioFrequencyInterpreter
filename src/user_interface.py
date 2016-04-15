import Tkinter
import wave


class User_Interface(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
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


        self.graphLabel = Tkinter.StringVar()
        label3 = Tkinter.Label(self,textvariable=self.graphLabel,
                              anchor="w",fg="black",bg="green")
        label3.grid(column=1,row=0,sticky='NSEW')
        self.graphLabel.set("Graph Here")

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="red")
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

    def StartButtonClick(self):
        self.labelVariable2.set("Starting...")

    def OnPressEnter(self,event):
        wr = wave.open('Sound_Files/test.wav','r')
        nchannels, sampwidth, framerate, nframes, comptype, compname =  wr.getparams()
        self.labelVariable.set(str(framerate) + "")