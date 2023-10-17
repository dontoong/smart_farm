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
from random import randint

# PyQt5 모듈
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

#matplotlib 모듈
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation

#나머지 모듈
from PyQt5 import QtWidgets, QtCore

from PyQt5 import uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import paho.mqtt.client as mqtt
from datetime import datetime
#import graph
import machbase_sql
import mqqt_control


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_main = resource_path('C:\\Users\\rlaau\\Desktop\\smart_farm\\smart_farm.ui')
form_main_ui = uic.loadUiType(form_main)[0]

form_sensor_ground_temp = resource_path('sensor_ground_temp.ui')
form_sensor_ground_temp_window = uic.loadUiType(form_sensor_ground_temp)[0]

form_sensor_ground_humi = resource_path('sensor_ground_humi.ui')
form_sensor_ground_humi_window = uic.loadUiType(form_sensor_ground_humi)[0]

form_sensor_ground_ph = resource_path('sensor_ground_ph.ui')
form_sensor_ground_ph_window = uic.loadUiType(form_sensor_ground_ph)[0]

form_sensor_co2 = resource_path('sensor_co2.ui')
form_sensor_co2_window = uic.loadUiType(form_sensor_co2)[0]

form_sensor_inner_temp = resource_path('sensor_inner_temp.ui')
form_sensor_inner_temp_window = uic.loadUiType(form_sensor_inner_temp)[0]

form_sensor_inner_humi = resource_path('sensor_inner_humi.ui')
form_sensor_inner_humi_window = uic.loadUiType(form_sensor_inner_humi)[0]

form_sensor_outer_temp = resource_path('sensor_outer_temp.ui')
form_sensor_outer_temp_window = uic.loadUiType(form_sensor_outer_temp)[0]

form_sensor_outer_humi = resource_path('sensor_outer_humi.ui')
form_sensor_outer_humi_window = uic.loadUiType(form_sensor_outer_humi)[0]

form_sensor_sun = resource_path('sensor_sun.ui')
form_sensor_sun_window = uic.loadUiType(form_sensor_sun)[0]

form_sensor_rain = resource_path('sensor_rain.ui')
form_sensor_rain_window = uic.loadUiType(form_sensor_rain)[0]

form_sensor_water_ph = resource_path('sensor_water_ph.ui')
form_sensor_water_ph_window = uic.loadUiType(form_sensor_water_ph)[0]

form_sensor_wind = resource_path('sensor_wind.ui')
form_sensor_wind_window = uic.loadUiType(form_sensor_wind)[0]

class Ui_Dialog(QDialog,QWidget,form_main_ui):
    
    def __init__(self):
        super().__init__()
        self.initUi()
        self.show()
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.start(1)  # every 10,000 milliseconds
        #self.show()        
        
    def btn_main_to_ground_temp(self):
        # self.hide()                     # 메인윈도우 숨김
        self.second = sensor_ground_temp()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
    
    def btn_main_to_ground_humi(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_ground_humi()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_ground_ph(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_ground_ph()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_co2(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_co2()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_inner_temp(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_inner_temp()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def btn_main_to_inner_humi(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_inner_humi()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_outer_temp(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_outer_temp()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def btn_main_to_outer_humi(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_outer_humi()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_sun(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_sun()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def btn_main_to_rain(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_rain()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def btn_main_to_water_ph(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_water_ph()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def btn_main_to_wind(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_wind()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(800, 600)
        
        self.realtime = QtCore.QTimer()
        self.realtime.setInterval(50)
        
        # tabWidget 초기화
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 750, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(750, 700))
        self.tabWidget.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane{border-radius:20px;margin:9px;}\n"
"QTabBar::tab{color:white;\n"
"background-color:rgba(255,255,255,0.3);\n"
"border-radius:20px;\n"
"width:230px;\n"
"height:90px;\n"
" margin:9px;}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 70))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

# General        
        # General - raspberry-pi.png
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color:transparent;")
        self.tab.setObjectName("tab")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("raspberry-pi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        
        # General tabWidget2 초기화
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 731, 440))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setStyleSheet("QTabWidget::tab-bar{alignment: center;}\n"
"QTabBar::tab:selected {color:white;\n"
"background-color:rgb(0,0,0);}\n"
"QTabWidget::pane{border-radius:20px;margin:9px;}\n"
"QTabBar::tab{color:black;\n"
"background-color:rgba(255,255,255,0.3);\n"
"border-radius:20px;\n"
"width:50px;\n"
"height:50px;\n"
" margin:9px;}")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")

# General
# General - 1
        # General 1번째 탭
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        
        # General 1번째 탭 블랙박스
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(2, 0, 711, 351))
        self.label_9.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:20px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
                
        # General 1번째 탭 온도 센서 데이터
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(50, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label.setObjectName("label")
        
        # General 1번째 탭 습도 센서 데이터
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(410, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_2.setObjectName("label_2")
        
        # General 1번째 탭 ph 센서 데이터
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_3.setObjectName("label_3")
        
        # General 1번째 탭 Co2 센서 데이터
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(410, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_4.setObjectName("label_4")
        
        # General 1번째 탭 온도 텍스트
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(50, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        # General 1번째 탭 습도 텍스트
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(410, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        # General 1번째 탭 ph 텍스트
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(50, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        # General 1번째 탭 Co2 농도 텍스트
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(410, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        # General 1번째 탭 온도 이미지 - temp.png
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 70, 70))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("temp.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        # General 1번째 탭 습도 이미지 - humi.png
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(530, 30, 70, 70))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("humi.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        
        # General 1번째 탭 °C 텍스트
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(190, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_14.setObjectName("label_14")
        
        # General 1번째 탭 % 텍스트
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(560, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_15.setObjectName("label_15")
        
        # General 1번째 탭 pH 텍스트
        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(200, 265, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_37.setObjectName("label_37")
        
        # General 1번째 탭 ppm 텍스트
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(560, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_16.setObjectName("label_16")

# General - 2        
        # General 2번째 탭
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        
        # General 2번째 탭 블랙박스
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(2, 0, 711, 351))
        self.label_18.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:30px;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        
        # General 2번째 탭 내부 온도 센서 데이터
        self.label_35 = QtWidgets.QLabel(self.tab_5)
        self.label_35.setGeometry(QtCore.QRect(50, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_35.setObjectName("label_35")

        # General 2번째 탭 내부 습도 센서 데이터
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setGeometry(QtCore.QRect(410, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_20.setObjectName("label_20")
        
        # General 2번째 탭 외부 온도 센서 데이터
        self.label_34 = QtWidgets.QLabel(self.tab_5)
        self.label_34.setGeometry(QtCore.QRect(50, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_34.setObjectName("label_34")
        
        # General 2번째 탭 외부 습도 센서 데이터
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(410, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_36.setObjectName("label_36")
        
        # General 2번째 탭 내부 온도 텍스트
        self.label_30 = QtWidgets.QLabel(self.tab_5)
        self.label_30.setGeometry(QtCore.QRect(50, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        
        # General 2번째 탭 내부 습도 텍스트
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(410, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        
        # General 2번째 탭 외부 온도 텍스트
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(50, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        
        # General 2번째 탭 외부 습도 텍스트
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(410, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        
        # General 2번째 탭 °C 텍스트
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(200, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_21.setObjectName("label_21")
        
        # General 2번째 탭 % 텍스트
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(560, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_28.setObjectName("label_28")
        
        # General 2번째 탭 °C 텍스트 
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(200, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_32.setObjectName("label_32")
        
        # General 2번째 탭 % 텍스트
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(560, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_29.setObjectName("label_29")
        
# General - 3        
        # General 세번째 탭
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        
        # General 3번째 탭 블랙박스
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(2, 0, 711, 351))
        self.label_19.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:30px;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        
        # General 3번째 탭 태양 센서 데이터
        self.label_39 = QtWidgets.QLabel(self.tab_6)
        self.label_39.setGeometry(QtCore.QRect(50, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_39.setObjectName("label_39")
        
        # General 3번째 탭 강수량 센서 데이터
        self.label_43 = QtWidgets.QLabel(self.tab_6)
        self.label_43.setGeometry(QtCore.QRect(410, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_43.setObjectName("label_43")
        
        # General 3번째 탭 물 ph 센서 데이터
        self.label_48 = QtWidgets.QLabel(self.tab_6)
        self.label_48.setGeometry(QtCore.QRect(50, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_48.setObjectName("label_48")
        
        # General 3번째 탭 풍 센서 데이터
        self.label_44 = QtWidgets.QLabel(self.tab_6)
        self.label_44.setGeometry(QtCore.QRect(410, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_44.setObjectName("label_44")
        
        # General 3번째 탭 일조량 텍스트
        self.label_41 = QtWidgets.QLabel(self.tab_6)
        self.label_41.setGeometry(QtCore.QRect(50, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        
        # General 3번째 탭 강수량 텍스트
        self.label_42 = QtWidgets.QLabel(self.tab_6)
        self.label_42.setGeometry(QtCore.QRect(410, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        
        # General 3번째 탭 물 pH 텍스트
        self.label_38 = QtWidgets.QLabel(self.tab_6)
        self.label_38.setGeometry(QtCore.QRect(50, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        
        # General 3번째 탭 풍속 텍스트
        self.label_49 = QtWidgets.QLabel(self.tab_6)
        self.label_49.setGeometry(QtCore.QRect(410, 185, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        
        # General 3번째 탭 °C 텍스트
        self.label_45 = QtWidgets.QLabel(self.tab_6)
        self.label_45.setGeometry(QtCore.QRect(200, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_45.setObjectName("label_45")
        
        # General 3번째 탭 mm 텍스트
        self.label_47 = QtWidgets.QLabel(self.tab_6)
        self.label_47.setGeometry(QtCore.QRect(560, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_47.setObjectName("label_47")        
        
        # General 3번째 탭 pH 텍스트
        self.label_46 = QtWidgets.QLabel(self.tab_6)
        self.label_46.setGeometry(QtCore.QRect(200, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_46.setObjectName("label_46")
        
        # General 3번째 탭 m/s 텍스트
        self.label_40 = QtWidgets.QLabel(self.tab_6)
        self.label_40.setGeometry(QtCore.QRect(560, 260, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_40.setObjectName("label_40")        
        
# Control
        # Control - control.png
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color:transparent;")
        self.tab_2.setObjectName("tab_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        
        # Control 블랙박스
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 731, 440))
        self.label_22.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:20px;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_22.raise_()
        
        # Control 푸쉬버튼 이미지
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("toggle_switch_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("toggle_switch_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        # Control 개폐기_1 푸쉬버튼
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(500, 40, 150, 61))
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.realtime.timeout.connect(machbase_sql.find_window_1)
        self.realtime.timeout.connect(self.realtime_window_1)

        # Control 개폐기_2 푸쉬버튼
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 130, 150, 61))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.realtime.timeout.connect(machbase_sql.find_window_2)
        self.realtime.timeout.connect(self.realtime_window_2)
        
        # Control 워터펌프 푸쉬버튼
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 220, 150, 61))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.realtime.timeout.connect(machbase_sql.find_w_pump)
        self.realtime.timeout.connect(self.realtime_w_pump)
        
        # Control 환풍기 푸쉬버튼
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 310, 150, 61))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.realtime.timeout.connect(machbase_sql.find_Ventil)
        self.realtime.timeout.connect(self.realtime_Ventil)

        # Control 텍스트 - 개폐기_1
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(70, 35, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        
        # Control 텍스트 - 개폐기_2
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(70, 125, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        
        # Control 텍스트 - 워터펌프
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(70, 215, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        
        # Control 텍스트 - 환풍기
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(70, 305, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")

# Sensor
        # Sensor - sensor.png
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("background-color:transparent;")
        self.tab_3.setObjectName("tab_3")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sensor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, "")
        
        # Sensor 블랙박스
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 731, 440))
        self.label_17.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:20px;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        
        # Sensor 지면 온도 푸쉬버튼
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#ff007f;")
        self.pushButton_5.setObjectName("pushButton_5")
        
        # Sensor 지면 습도 푸쉬버튼
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;color:#aaff00;")
        self.pushButton_6.setObjectName("pushButton_6")
        
        # Sensor 일조량 푸쉬버튼
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(370, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#ff007f;")
        self.pushButton_11.setObjectName("pushButton_11")
        
        # Sensor 강수량 푸쉬버튼
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;color:#aaff00;")
        self.pushButton_12.setObjectName("pushButton_12")
        
        # Sensor 내부 온도 푸쉬버튼
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 150, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#ff007f;")
        self.pushButton_7.setObjectName("pushButton_7")
        
        # Sensor 내부 습도 푸쉬버튼
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 150, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;color:#aaff00;")
        self.pushButton_8.setObjectName("pushButton_8")
        
                
        # Sensor pH 푸쉬버튼
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 150, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#55aaff;")
        self.pushButton_13.setObjectName("pushButton_13")
        
        # Sensor Co2 푸쉬버튼
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(540, 150, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#aaffff;")
        self.pushButton_14.setObjectName("pushButton_14")
        
        # Sensor 외부 온도 푸쉬버튼
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 280, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#ff007f;")
        self.pushButton_9.setObjectName("pushButton_9")
        
        # Sensor 외부 습도 푸쉬버튼
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 280, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;color:#aaff00;")
        self.pushButton_10.setObjectName("pushButton_10")
        
        # Sensor 물 ph 푸쉬버튼
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(370, 280, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#55aaff;")
        self.pushButton_15.setObjectName("pushButton_15")
        
        # Sensor 풍속 푸쉬버튼
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(540, 280, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#aaffff;")
        self.pushButton_16.setObjectName("pushButton_16")
        
        # smart_farm.jpg 블랙박스
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 811, 611))
        self.label_7.setStyleSheet("background-color:rgba(0, 0, 0, 0.45);")
        #self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        
        # 배경 이미지 - smart_farm.jpg
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 800, 600))
        #self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("smart_farm.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        
        # 위젯의 위치
        self.label_22.raise_()
        self.pushButton.raise_()
        self.label_24.raise_()
        self.pushButton_2.raise_()
        self.label_25.raise_()
        self.pushButton_3.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.pushButton_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.tabWidget.raise_()
        
        # 로드
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        #self.pushButton.clicked.connect(Dialog.btn_main_to_temp)
        self.pushButton.clicked.connect(self.window_1_toggleState)
        self.pushButton_2.clicked.connect(self.window_2_toggleState)
        self.pushButton_3.clicked.connect(self.w_pump_toggleState)
        self.pushButton_4.clicked.connect(self.Ventil_toggleState)
        self.pushButton_5.clicked.connect(self.btn_main_to_ground_temp)
        self.pushButton_6.clicked.connect(self.btn_main_to_ground_humi)
        self.pushButton_7.clicked.connect(self.btn_main_to_inner_temp)
        self.pushButton_8.clicked.connect(self.btn_main_to_inner_humi)
        self.pushButton_9.clicked.connect(self.btn_main_to_outer_temp)
        self.pushButton_10.clicked.connect(self.btn_main_to_outer_humi)
        self.pushButton_11.clicked.connect(self.btn_main_to_sun)
        self.pushButton_12.clicked.connect(self.btn_main_to_rain)
        self.pushButton_13.clicked.connect(self.btn_main_to_ground_ph)
        self.pushButton_14.clicked.connect(self.btn_main_to_co2)
        self.pushButton_15.clicked.connect(self.btn_main_to_water_ph)
        self.pushButton_16.clicked.connect(self.btn_main_to_wind)
        self.realtime.start(1)
#        self.pushButton.clicked.connect(send_0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    # 토글 버튼 동기화
    def realtime_window_1(self):
        if machbase_sql.find_window_1() == '1':
            self.pushButton.setChecked(True)
        elif machbase_sql.find_window_1() == '0':
            self.pushButton.setChecked(False)
            
    def realtime_window_2(self):        
        if machbase_sql.find_window_2() == '1':
            self.pushButton_2.setChecked(True)
        elif machbase_sql.find_window_2() == '0':
            self.pushButton_2.setChecked(False)
            
    def realtime_w_pump(self):        
        if machbase_sql.find_w_pump() == '1':
            self.pushButton_3.setChecked(True)
        elif machbase_sql.find_w_pump() == '0':
            self.pushButton_3.setChecked(False)
            
    def realtime_Ventil(self):        
        if machbase_sql.find_Ventil() == '1':
            self.pushButton_4.setChecked(True)
        elif machbase_sql.find_Ventil() == '0':
            self.pushButton_4.setChecked(False)
    
    # 토글 버튼 제어
    def window_1_toggleState(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(machbase_sql.ip, mqqt_control.mqqt_port)
        if self.pushButton.isChecked() == True:
            machbase_sql.window_1_open()
            mqqt_control.window_1_send_1()
        elif self.pushButton.isChecked() == False:
            machbase_sql.window_1_close()
            mqqt_control.window_1_send_0()

    def window_2_toggleState(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(machbase_sql.ip, mqqt_control.mqqt_port)
        if self.pushButton_2.isChecked() == True:
            machbase_sql.window_2_open()
            mqqt_control.window_2_send_1()
        elif self.pushButton_2.isChecked() == False:
            machbase_sql.window_2_close()
            mqqt_control.window_2_send_0()

    def w_pump_toggleState(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(machbase_sql.ip, mqqt_control.mqqt_port)
        if self.pushButton_3.isChecked() == True:
            machbase_sql.w_pump_open()
            mqqt_control.w_pump_send_1()
        elif self.pushButton_3.isChecked() == False:
            machbase_sql.w_pump_close()
            mqqt_control.w_pump_send_0()

    def Ventil_toggleState(self):
       self.mqttc = mqtt.Client()
       self.mqttc.connect(machbase_sql.ip, mqqt_control.mqqt_port)
       if self.pushButton_4.isChecked() == True:
            machbase_sql.Ventil_open()
            mqqt_control.ventil_send_1()
       elif self.pushButton_4.isChecked() == False:
            machbase_sql.Ventil_close()
            mqqt_control.ventil_send_0()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
        #센서데이터 로드
        self.label.setText(_translate("Dialog", machbase_sql.read_ground_temp())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label.setStyleSheet("color:#ffffff;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2.setText(_translate("Dialog", machbase_sql.read_ground_humi())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_2.setStyleSheet("color:#ffffff;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setText(_translate("Dialog", machbase_sql.read_ground_ph())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_3.setStyleSheet("color:#ffffff;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4.setText(_translate("Dialog", machbase_sql.read_co2())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_4.setStyleSheet("color:#ffffff;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_35.setText(_translate("Dialog", machbase_sql.read_inner_temp())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_35.setStyleSheet("color:#ffffff;")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_20.setText(_translate("Dialog", machbase_sql.read_inner_humi())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_20.setStyleSheet("color:#ffffff;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_34.setText(_translate("Dialog", machbase_sql.read_outer_temp())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_34.setStyleSheet("color:#ffffff;")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_36.setText(_translate("Dialog", machbase_sql.read_outer_humi())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_36.setStyleSheet("color:#ffffff;")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_39.setText(_translate("Dialog", machbase_sql.read_sun())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_39.setStyleSheet("color:#ffffff;")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_43.setText(_translate("Dialog", machbase_sql.read_rain())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_43.setStyleSheet("color:#ffffff;")
        self.label_43.setAlignment(Qt.AlignCenter)
        self.label_48.setText(_translate("Dialog", machbase_sql.read_water_ph())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_48.setStyleSheet("color:#ffffff;")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_44.setText(_translate("Dialog", machbase_sql.read_wind())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_44.setStyleSheet("color:#ffffff;")
        self.label_44.setAlignment(Qt.AlignCenter)

        # 텍스트(단위)
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">지면 습도</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff007f;\">지면 온도</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#55aaff;\">지면 pH</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aaffff;\">Co2 농도</span></p></body></html>"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff007f;\">내부 온도</span></p></body></html>"))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">내부 습도</span></p></body></html>"))
        self.label_33.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff007f;\">외부 온도</span></p></body></html>"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">외부 습도</span></p></body></html>"))
        self.label_41.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff007f;\">일조량</span></p></body></html>"))
        self.label_42.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">강수량</span></p></body></html>"))
        self.label_38.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#55aaff;\">물 pH</span></p></body></html>"))
        self.label_49.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aaffff;\">풍속</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">%</span></p></body></html>"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">%</span></p></body></html>"))
        self.label_32.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">%</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">ppm</span></p></body></html>"))
        self.label_45.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.label_46.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">pH</span></p></body></html>"))
        self.label_47.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">mm</span></p></body></html>"))
        self.label_40.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">m/s</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Control"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Sensor"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">개폐기_1</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">개폐기_2</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#55aaff;\">펌프</span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;;\">환풍기</span></p></body></html>"))
        self.label_37.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">pH</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "지표 온도"))
        self.pushButton_6.setText(_translate("Dialog", "지표 습도"))
        self.pushButton_7.setText(_translate("Dialog", "내부 온도"))
        self.pushButton_8.setText(_translate("Dialog", "내부 습도"))
        self.pushButton_9.setText(_translate("Dialog", "외부 온도"))
        self.pushButton_10.setText(_translate("Dialog", "외부 습도"))
        self.pushButton_11.setText(_translate("Dialog", "일조량"))
        self.pushButton_12.setText(_translate("Dialog", "강수량"))
        self.pushButton_13.setText(_translate("Dialog", "지표 ph"))
        self.pushButton_14.setText(_translate("Dialog", "Co2 농도"))
        self.pushButton_15.setText(_translate("Dialog", "물 ph"))
        self.pushButton_16.setText(_translate("Dialog", "풍속"))
        
    def initUi(self):
        self.setupUi(self)

# 지표 온도 실시간 그래프 ui
class sensor_ground_temp(QDialog,QWidget,form_sensor_ground_temp_window):
    def __init__(self):
        super(sensor_ground_temp,self).__init__()
        self.initUi()
        self.show()
        
        self.ground_temp_x = list(range(5))  # 25개의 x좌표
        self.ground_temp_y = [machbase_sql.read_ground_temp_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_ground_temp =  self.ground_temp.plot(self.ground_temp_x, self.ground_temp_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.ground_temp_x = self.ground_temp_x[1:]  # Remove the first y element.
        self.ground_temp_x.append(self.ground_temp_x[-1]+5)  # Add a new value 1 higher than the last.

        self.ground_temp_y = self.ground_temp_y[1:]  # Remove the first
        self.ground_temp_y.append(machbase_sql.read_ground_temp_float())  # Add a new random value.
        
        self.data_line_ground_temp.setData(self.ground_temp_x, self.ground_temp_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

# 지표 습도 실시간 그래프 ui
class sensor_ground_humi(QDialog,QWidget,form_sensor_ground_humi_window):
    def __init__(self):
        super(sensor_ground_humi,self).__init__()
        self.initUi()
        self.show()
        
        self.ground_humi_x = list(range(5))
        self.ground_humi_y = [machbase_sql.read_ground_humi_float() for _ in range(5)]  # 100 data points
      
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_ground_humi =  self.ground_humi.plot(self.ground_humi_x, self.ground_humi_y, pen=pen)

        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.ground_humi_x = self.ground_humi_x[1:]  # Remove the first y element.
        self.ground_humi_x.append(self.ground_humi_x[-1]+5)  # Add a new value 1 higher than the last.

        self.ground_humi_y = self.ground_humi_y[1:]  # Remove the first
        self.ground_humi_y.append(machbase_sql.read_ground_humi_float())  # Add a new random value.
        
        self.data_line_ground_humi.setData(self.ground_humi_x, self.ground_humi_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

# 지표 pH 실시간 그래프 ui        
class sensor_ground_ph(QDialog,QWidget,form_sensor_ground_ph_window):
    def __init__(self):
        super(sensor_ground_ph,self).__init__()
        self.initUi()
        self.show()
        
        self.ground_ph_x = list(range(5))  # 100 time points
        self.ground_ph_y = [machbase_sql.read_ground_ph_float() for _ in range(5)]  # 100 data points       

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_ground_ph =  self.ground_ph.plot(self.ground_ph_x, self.ground_ph_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.ground_ph_x = self.ground_ph_x[1:]  # Remove the first y element.
        self.ground_ph_x.append(self.ground_ph_x[-1]+5)  # Add a new value 1 higher than the last.

        self.ground_ph_y = self.ground_ph_y[1:]  # Remove the first
        self.ground_ph_y.append(machbase_sql.read_ground_ph_float())  # Add a new random value.
        
        self.data_line_ground_ph.setData(self.ground_ph_x, self.ground_ph_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

# Co2 실시간 그래프 ui        
class sensor_co2(QDialog,QWidget,form_sensor_co2_window):
    def __init__(self):
        super(sensor_co2,self).__init__()
        self.initUi()
        self.show()
        
        self.co2_x = list(range(5))
        self.co2_y = [machbase_sql.read_co2_float() for _ in range(5)]  # 100 data points        
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_co2 =  self.co2.plot(self.co2_x, self.co2_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
        #self.show()
    
    # x좌표 갱신
    def update_plot_data(self):
        self.co2_x = self.co2_x[1:]  # Remove the first y element.
        self.co2_x.append(self.co2_x[-1]+1)  # Add a new value 1 higher than the last.

        self.co2_y = self.co2_y[1:]  # Remove the first
        self.co2_y.append(machbase_sql.read_co2_float())  # Add a new random value.
        
        self.data_line_co2.setData(self.co2_x, self.co2_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

# 내부 온도 실시간 그래프 ui        
class sensor_inner_temp(QDialog,QWidget,form_sensor_inner_temp_window):
    def __init__(self):
        super(sensor_inner_temp,self).__init__()
        self.initUi()
        self.show()
        
        self.inner_temp_x = list(range(5))  # 25개의 x좌표
        self.inner_temp_y = [machbase_sql.read_inner_temp_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_inner_temp =  self.inner_temp.plot(self.inner_temp_x, self.inner_temp_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.inner_temp_x = self.inner_temp_x[1:]  # Remove the first y element.
        self.inner_temp_x.append(self.inner_temp_x[-1]+5)  # Add a new value 1 higher than the last.

        self.inner_temp_y = self.inner_temp_y[1:]  # Remove the first
        self.inner_temp_y.append(machbase_sql.read_inner_temp_float())  # Add a new random value.
        
        self.data_line_inner_temp.setData(self.inner_temp_x, self.inner_temp_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
class sensor_inner_humi(QDialog,QWidget,form_sensor_inner_humi_window):
    def __init__(self):
        super(sensor_inner_humi,self).__init__()
        self.initUi()
        self.show()
        
        self.inner_humi_x = list(range(5))  # 25개의 x좌표
        self.inner_humi_y = [machbase_sql.read_inner_humi_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_inner_humi =  self.inner_humi.plot(self.inner_humi_x, self.inner_humi_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.inner_humi_x = self.inner_humi_x[1:]  # Remove the first y element.
        self.inner_humi_x.append(self.inner_humi_x[-1]+5)  # Add a new value 1 higher than the last.

        self.inner_humi_y = self.inner_humi_y[1:]  # Remove the first
        self.inner_humi_y.append(machbase_sql.read_inner_humi_float())  # Add a new random value.
        
        self.data_line_inner_humi.setData(self.inner_humi_x, self.inner_humi_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

class sensor_outer_temp(QDialog,QWidget,form_sensor_outer_temp_window):
    def __init__(self):
        super(sensor_outer_temp,self).__init__()
        self.initUi()
        self.show()
        
        self.outer_temp_x = list(range(5))  # 25개의 x좌표
        self.outer_temp_y = [machbase_sql.read_outer_temp_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_outer_temp =  self.outer_temp.plot(self.outer_temp_x, self.outer_temp_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.outer_temp_x = self.outer_temp_x[1:]  # Remove the first y element.
        self.outer_temp_x.append(self.outer_temp_x[-1]+5)  # Add a new value 1 higher than the last.

        self.outer_temp_y = self.outer_temp_y[1:]  # Remove the first
        self.outer_temp_y.append(machbase_sql.read_outer_temp_float())  # Add a new random value.
        
        self.data_line_outer_temp.setData(self.outer_temp_x, self.outer_temp_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
class sensor_outer_humi(QDialog,QWidget,form_sensor_outer_humi_window):
    def __init__(self):
        super(sensor_outer_humi,self).__init__()
        self.initUi()
        self.show()
        
        self.outer_humi_x = list(range(5))  # 25개의 x좌표
        self.outer_humi_y = [machbase_sql.read_outer_humi_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_outer_humi =  self.outer_humi.plot(self.outer_humi_x, self.outer_humi_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.outer_humi_x = self.outer_humi_x[1:]  # Remove the first y element.
        self.outer_humi_x.append(self.outer_humi_x[-1]+5)  # Add a new value 1 higher than the last.

        self.outer_humi_y = self.outer_humi_y[1:]  # Remove the first
        self.outer_humi_y.append(machbase_sql.read_outer_humi_float())  # Add a new random value.
        
        self.data_line_outer_humi.setData(self.outer_humi_x, self.outer_humi_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

class sensor_wind(QDialog,QWidget,form_sensor_wind_window):
    def __init__(self):
        super(sensor_wind,self).__init__()
        self.initUi()
        self.show()
        
        self.wind_x = list(range(5))  # 25개의 x좌표
        self.wind_y = [machbase_sql.read_wind_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_wind =  self.wind.plot(self.wind_x, self.wind_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.wind_x = self.wind_x[1:]  # Remove the first y element.
        self.wind_x.append(self.wind_x[-1]+5)  # Add a new value 1 higher than the last.

        self.wind_y = self.wind_y[1:]  # Remove the first
        self.wind_y.append(machbase_sql.read_wind_float())  # Add a new random value.
        
        self.data_line_wind.setData(self.wind_x, self.wind_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
class sensor_water_ph(QDialog,QWidget,form_sensor_water_ph_window):
    def __init__(self):
        super(sensor_water_ph,self).__init__()
        self.initUi()
        self.show()
        
        self.water_ph_x = list(range(5))  # 25개의 x좌표
        self.water_ph_y = [machbase_sql.read_water_ph_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_water_ph =  self.water_ph.plot(self.water_ph_x, self.water_ph_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.water_ph_x = self.water_ph_x[1:]  # Remove the first y element.
        self.water_ph_x.append(self.water_ph_x[-1]+5)  # Add a new value 1 higher than the last.

        self.water_ph_y = self.water_ph_y[1:]  # Remove the first
        self.water_ph_y.append(machbase_sql.read_water_ph_float())  # Add a new random value.
        
        self.data_line_water_ph.setData(self.water_ph_x, self.water_ph_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

class sensor_sun(QDialog,QWidget,form_sensor_sun_window):
    def __init__(self):
        super(sensor_sun,self).__init__()
        self.initUi()
        self.show()
        
        self.sun_x = list(range(5))  # 25개의 x좌표
        self.sun_y = [machbase_sql.read_sun_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_sun =  self.sun.plot(self.sun_x, self.sun_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.sun_x = self.sun_x[1:]  # Remove the first y element.
        self.sun_x.append(self.sun_x[-1]+5)  # Add a new value 1 higher than the last.

        self.sun_y = self.sun_y[1:]  # Remove the first
        self.sun_y.append(machbase_sql.read_sun_float())  # Add a new random value.
        
        self.data_line_sun.setData(self.sun_x, self.sun_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
class sensor_rain(QDialog,QWidget,form_sensor_rain_window):
    def __init__(self):
        super(sensor_rain,self).__init__()
        self.initUi()
        self.show()
        
        self.rain_x = list(range(5))  # 25개의 x좌표
        self.rain_y = [machbase_sql.read_rain_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_rain =  self.rain.plot(self.rain_x, self.rain_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.rain_x = self.rain_x[1:]  # Remove the first y element.
        self.rain_x.append(self.rain_x[-1]+5)  # Add a new value 1 higher than the last.

        self.rain_y = self.rain_y[1:]  # Remove the first
        self.rain_y.append(machbase_sql.read_rain_float())  # Add a new random value.
        
        self.data_line_rain.setData(self.rain_x, self.rain_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
