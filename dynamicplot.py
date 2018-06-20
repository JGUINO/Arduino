import matplotlib
matplotlib.use('TKAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as pltlib
import tkinter
from tkinter import *
import scipy as sc
#import matplotlib.pyplot as pltlib
# lmfit is imported becuase parameters are allowed to depend on each other along with bounds, etc.
#from lmfit import minimize, Parameters, Minimizer



#Make object for application
class App_Window(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        button = tkinter.Button(self,text="Open File",command=self.OnButtonClick).pack(side=tkinter.TOP)
        self.canvasFig=pltlib.figure(1)
        Fig = matplotlib.figure.Figure(figsize=(5,4),dpi=100)
        FigSubPlot = Fig.add_subplot(111)
        x=['1','2','3','4']
        y=[300,870,604,330]
        self.line1, = FigSubPlot.hist(x)
        FigSubPlot.axis([0,5,0,1000])
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(Fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.resizable(True,False)
        
    def refreshFigure(self,x,y):
        self.line1.set_data(x,y)
        ax = self.canvas.figure.axes[0]
        ax.set_xlim(min(x),max(x))
        ax.set_ylim(0, 1000)        
        self.canvas.draw()
    def OnButtonClick(self):
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        x=[1,2,3,4]
        y=[300,870,604,330]
        #for num in range(0,1000):x.append(num*.001+1)
        # just some random function is given here, the real data is a UV-Vis spectrum
        #for num2 in range(0,1000):y.append(sc.math.sin(num2*.06)+sc.math.e**(num2*.001))
        X = x
        Y = y
        self.refreshFigure(X,Y)

if __name__ == "__main__":
    MainWindow = App_Window(None)
    MainWindow.mainloop()