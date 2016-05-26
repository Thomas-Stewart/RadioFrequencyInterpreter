import matplotlib, numpy, sys
import Tkinter as Tk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from random import randint

class Graph():

    def getGraph(self, root):

        #root = Tk.Tk()

        print 'figure'
        f = Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)


        data = (randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50),
                randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50))

        ind = numpy.arange(5)  # the x locations for the groups
        width = .5

        #ax.bar(ind, data, width)
        ax.plot(data)


        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.draw()
        return canvas

