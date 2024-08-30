from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

# matpotlib figure class. where plotting will be placed on the GUI
class MplWidget(QWidget):

    # initialization method, to be run first and self keyword that it can be used from outside the class
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # figurecanvas is added to code, where the real plotting will be done
        # figurecanvas is like a paper to be drawn on
        self.canvas = FigureCanvas(Figure())

        # canvas layout
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        # no of plot is one
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


