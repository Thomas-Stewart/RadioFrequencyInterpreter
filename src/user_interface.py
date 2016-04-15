import Tkinter
import wave


class User_Interface(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)



    def OnButtonClick(self):
        self.labelVariable.set("You clicked the button !")

    def OnPressEnter(self,event):
        wr = wave.open('Sound_Files/test.wav','r')
        nchannels, sampwidth, framerate, nframes, comptype, compname =  wr.getparams()
        self.labelVariable.set(str(framerate) + "")