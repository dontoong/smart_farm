#system
import os
import sys
import time
import numpy as np
# 센서데이터 모듈
from machbaseAPI import machbase
from PyQt5.QtCore import *
import re
import random

# PyQt5 모듈
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

#matplotlib 모듈
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation


def read_temp():
    db = machbase()
    if db.open('175.126.123.217','SYS','MANAGER',5656) == 0 :
        return db.result()
    if db.execute('select value from tag where name =\'temp\' order by time desc limit 1') == 0 :
        return db.result()
    result = db.result()
    if db.close() == 0 :
        return db.result()
    return float(result[10:-2])

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=800, height=600, dpi=100):
        fig = Figure(figsize=(800, 600), dpi=dpi)
        self.axes = fig.add_subplot(111, xlim=(0, 50), ylim=(20,40))
        #self.axes2 = fig.add_subplot(212, xlim=(0, 50), ylim=(0, 600))

        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
    def compute_initial_figure(self):
        pass

class AnimationWidget(QWidget):
    def __init__(self, parent=None, width=800, height=600, dpi=100):
        QMainWindow.__init__(self)
        vbox = QVBoxLayout()
        self.canvas = MyMplCanvas(self, width=800, height=600, dpi=100)
        vbox.addWidget(self.canvas)
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.x = np.arange(50)
        self.y = np.ones(50, dtype=np.float)*np.nan
        self.line, = self.canvas.axes.plot(self.x, self.y, animated=True, lw=2)

      
        self.ani = animation.FuncAnimation(self.canvas.figure, self.update_line,blit=True, interval=25)
        
    def update_line(self, i):
        y = read_temp()
        old_y = self.line.get_ydata()
        new_y = np.r_[old_y[1:], y]
        self.line.set_ydata(new_y)
        
        # self.line.set_ydata(y)
        #print(self.y)
        return [self.line]

    # def update_line2(self, i):
    #     y2 = random.randint(0,510)
    #     old_y2 = self.line2.get_ydata()
    #     new_y2 = np.r_[old_y2[1:], y2]
    #     self.line2.set_ydata(new_y2)
    #     return [self.line2]
        # self.line.set_ydata(y)
        
if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    aw = AnimationWidget()
    aw.resize(800,600)
    aw.show()
    sys.exit(qApp.exec_())