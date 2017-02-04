## PyQt5 version of plot_test.py ##
import sys, os, random
from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
matplotlib.use('QT5Agg')   ###
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas   ###
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  ###
from matplotlib.figure import Figure
import numpy as np


class AppForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
	self.setWindowTitle("Let's Plot the Sine Function!")
        self.create_main_frame()
        self.first_draw()

	#initial sine function
    def first_draw(self):
        t = np.arange(0, 2, 0.01)
	self.axes.plot(t, np.sin(2*np.pi*t), 'r')
	self.axes.axis([0, 2, -1.5, 1.5])
        # Update canvas by redrawing with current state of figure
        self.canvas.draw()
	self.num_plots = 1

    def Button_Clear(self):
	self.axes.clear()
	self.canvas.draw()
	self.num_plots = 0

    def Button_Plot(self):
	t = np.arange(0, 2, 0.01)
	freq = self.Frequency.text()
	amp = self.Amplitude.text()
	phase = self.Phase.text()
	freq = float(freq)
	amp = float(amp)
	phase = float(phase)
	if self.num_plots == 0:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'r')
	elif self.num_plots == 1:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'b')
	elif self.num_plots == 2:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'g')
	elif self.num_plots == 3:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'k')
	elif self.num_plots == 4:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'y')
	elif self.num_plots == 5:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'm')
	else:
		self.axes.plot(t, amp * np.sin(2*np.pi*freq*t+phase), 'c')
	self.axes.axis([0, 2, -1.5, 1.5])
	self.canvas.draw()
	self.num_plots += 1

    def create_main_frame(self):
        self.main_frame = QtWidgets.QWidget()
        # Create new figure to put plots on
        self.fig = Figure()
        # Create canvas to draw figure on
        self.canvas = FigureCanvas(self.fig)
        # Canvas is a child on main_frame
        self.canvas.setParent(self.main_frame)
        
        # self.axes now references the first subplot
        self.axes = self.fig.add_subplot(111)
	self.axes.axis([0, 2, -1.5, 1.5])
        # Create a matplotlib toolbar for the canvas. Set parent to main_frame
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
	# Create text boxes for entering graph variables
	self.Amplitude = QtWidgets.QLineEdit('1')
	self.Amplitude.setParent(self.main_frame)
	self.Frequency = QtWidgets.QLineEdit('1')
	self.Frequency.setParent(self.main_frame)
	self.Phase = QtWidgets.QLineEdit('0')
	self.Phase.setParent(self.main_frame)
	# Set labels for text boxes
	self.Amp_Label = QtWidgets.QLabel("Amplitude:")
	self.Amp_Label.setParent(self.main_frame)
	self.Frq_Label = QtWidgets.QLabel("Frequency:")
	self.Frq_Label.setParent(self.main_frame)
	self.Phs_Label = QtWidgets.QLabel("Phase:")
	self.Phs_Label.setParent(self.main_frame)
	# Create buttons for plotting and clearing
	self.Sine_Plot = QtWidgets.QPushButton("Plot Sine Wave", self.main_frame)
	self.Clear_All = QtWidgets.QPushButton("Clear", self.main_frame)


	hbox1 = QtWidgets.QHBoxLayout()
	hbox2 = QtWidgets.QHBoxLayout()
	hbox3 = QtWidgets.QHBoxLayout()
	hbox4 = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
	vbox.addLayout(hbox1)
	hbox1.addWidget(self.Amp_Label)	
	hbox1.addWidget(self.Amplitude)
	vbox.addLayout(hbox2)
	hbox2.addWidget(self.Frq_Label)
	hbox2.addWidget(self.Frequency)
	vbox.addLayout(hbox3)
	hbox3.addWidget(self.Phs_Label)
	hbox3.addWidget(self.Phase)
	vbox.addLayout(hbox4)
	hbox4.addWidget(self.Sine_Plot)
	hbox4.addWidget(self.Clear_All)

	self.Clear_All.clicked.connect(self.Button_Clear)
	self.Sine_Plot.clicked.connect(self.Button_Plot)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)



app = QtWidgets.QApplication(sys.argv)
form = AppForm()
form.show()
app.exec_()
