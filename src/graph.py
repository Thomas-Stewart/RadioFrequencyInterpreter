import matplotlib, numpy, sys
import Tkinter as Tk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Graph():

    def getGraph(self, root):

        #root = Tk.Tk()

        print 'figure'
        f = Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)

        data = (20, 35, 30, 35, 27)

        ind = numpy.arange(5)  # the x locations for the groups
        width = .5

        rects1 = ax.bar(ind, data, width)

        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        #canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        #toolbar = NavigationToolbar2TkAgg(canvas, root)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.draw()
        return canvas

