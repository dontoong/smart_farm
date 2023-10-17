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
import graph
import machbase_sql
import mqqt_control


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_main = resource_path('C:\\Users\\rlaau\\Desktop\\smart_farm\\smart_farm.ui')
form_main_ui = uic.loadUiType(form_main)[0]

form_sensor_temp = resource_path('sensor_temp.ui')
form_sensor_temp_window = uic.loadUiType(form_sensor_temp)[0]

form_sensor_humi = resource_path('sensor_humi.ui')
form_sensor_humi_window = uic.loadUiType(form_sensor_humi)[0]

form_sensor_ph = resource_path('sensor_ph.ui')
form_sensor_ph_window = uic.loadUiType(form_sensor_ph)[0]

form_sensor_co2 = resource_path('sensor_co2.ui')
form_sensor_co2_window = uic.loadUiType(form_sensor_co2)[0]

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
        
    def btn_main_to_temp(self):
        # self.hide()                     # 메인윈도우 숨김
        self.second = sensor_temp()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐
    
    def btn_main_to_humi(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_humi()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐
        
    def btn_main_to_ph(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_ph()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐
        
    def btn_main_to_co2(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = sensor_co2()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

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
        
        # General - raspberry-pi.png
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color:transparent;")
        self.tab.setObjectName("tab")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("raspberry-pi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        
        # Control - control.png
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color:transparent;")
        self.tab_2.setObjectName("tab_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        
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
        
        # Sensor 온도 푸쉬버튼
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
        
        # Sensor 습도 푸쉬버튼
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
        
        # Sensor ph 푸쉬버튼
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#55aaff;")
        self.pushButton_7.setObjectName("pushButton_7")
        
        # Sensor Co2 푸쉬버튼
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 20, 160, 100))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:rgb(220, 150, 120); border-radius:10px;\n"
"color:#aaffff;")
        self.pushButton_8.setObjectName("pushButton_8")
 
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
        
        # General 블랙박스
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 731, 440))
        self.label_9.setStyleSheet("background-color:rgba(0, 0, 0, 0.45); border-radius:20px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        
        # 온도 센서 데이터
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label.setObjectName("label")
        
        # 습도 센서 데이터
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(490, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_2.setObjectName("label_2")
        
        # ph 센서 데이터
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 325, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_3.setObjectName("label_3")
        
        # Co2 센서 데이터
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(490, 325, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_4.setObjectName("label_4")
        
        # 텍스트 - 온도
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(50, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        # 텍스트 - 습도
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(490, 25, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        # 텍스트 - ph
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(50, 250, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        # 텍스트 - Co2 농도
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(490, 250, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        # 텍스트 - 개폐기_1
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(70, 35, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        
        # 텍스트 - 개폐기_2
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(70, 125, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        
        # 텍스트 - 워터펌프
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(70, 215, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        
        # 텍스트 - 환풍기
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(70, 305, 200, 75))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        
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
        
        # 온도 이미지 - temp.png
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(110, 30, 70, 70))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("temp.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        # 습도 이미지 - humi.png
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(550, 30, 70, 70))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("humi.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        
        # 텍스트 - °C
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(190, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_14.setObjectName("label_14")
        
        # 텍스트 - %
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(630, 100, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_15.setObjectName("label_15")
        
        # 텍스트 - ppm
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(630, 325, 200, 75))
        font = QtGui.QFont()
        font.setFamily("양재참숯체B")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:rgba(255,255,255);background:transparent;")
        self.label_16.setObjectName("label_16")
        
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
        #self.pushButton.clicked.connect(Dialog.btn_main_to_temp)
        self.pushButton.clicked.connect(self.window_1_toggleState)
        self.pushButton_2.clicked.connect(self.window_2_toggleState)
        self.pushButton_3.clicked.connect(self.w_pump_toggleState)
        self.pushButton_4.clicked.connect(self.Ventil_toggleState)
        self.pushButton_5.clicked.connect(self.btn_main_to_temp)
        self.pushButton_6.clicked.connect(self.btn_main_to_humi)
        self.pushButton_7.clicked.connect(self.btn_main_to_ph)
        self.pushButton_8.clicked.connect(self.btn_main_to_co2)
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
        self.label.setText(_translate("Dialog", machbase_sql.read_temp())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label.setStyleSheet("color:#ffffff;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2.setText(_translate("Dialog", machbase_sql.read_humi())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_2.setStyleSheet("color:#ffffff;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setText(_translate("Dialog", machbase_sql.read_ph())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_3.setStyleSheet("color:#ffffff;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4.setText(_translate("Dialog", machbase_sql.read_co2())) #"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.label_4.setStyleSheet("color:#ffffff;")
        self.label_4.setAlignment(Qt.AlignCenter)

        # 텍스트(단위)
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">습도</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff007f;\">온도</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#55aaff;\">pH</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aaffff;\">Co2 농도</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">°C</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">%</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">ppm</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Control"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Sensor"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">개폐기_1</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaff00;\">개폐기_2</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#55aaff;\">펌프</span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;;\">환풍기</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "온도"))
        self.pushButton_6.setText(_translate("Dialog", "습도"))
        self.pushButton_7.setText(_translate("Dialog", "ph"))
        self.pushButton_8.setText(_translate("Dialog", "Co2 농도"))
        
    def initUi(self):
        self.setupUi(self)

# 온도 실시간 그래프 ui
class sensor_temp(QDialog,QWidget,form_sensor_temp_window):
    def __init__(self):
        super(sensor_temp,self).__init__()
        self.initUi()
        self.show()
        
        self.temp_x = list(range(5))  # 25개의 x좌표
        self.temp_y = [machbase_sql.read_temp_float() for _ in range(5)]  # 25개의 y좌표       
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_temp =  self.temp.plot(self.temp_x, self.temp_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.temp_x = self.temp_x[1:]  # Remove the first y element.
        self.temp_x.append(self.temp_x[-1]+5)  # Add a new value 1 higher than the last.

        self.temp_y = self.temp_y[1:]  # Remove the first
        self.temp_y.append(machbase_sql.read_temp_float())  # Add a new random value.
        
        self.data_line_temp.setData(self.temp_x, self.temp_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.

# 습도 실시간 그래프 ui
class sensor_humi(QDialog,QWidget,form_sensor_humi_window):
    def __init__(self):
        super(sensor_humi,self).__init__()
        self.initUi()
        self.show()
        
        self.humi_x = list(range(5))
        self.humi_y = [machbase_sql.read_humi_float() for _ in range(5)]  # 100 data points
      
        
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_humi =  self.humi.plot(self.humi_x, self.humi_y, pen=pen)

        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.humi_x = self.humi_x[1:]  # Remove the first y element.
        self.humi_x.append(self.humi_x[-1]+5)  # Add a new value 1 higher than the last.

        self.humi_y = self.humi_y[1:]  # Remove the first
        self.humi_y.append(machbase_sql.read_humi_float())  # Add a new random value.
        
        self.data_line_humi.setData(self.humi_x, self.humi_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
class sensor_ph(QDialog,QWidget,form_sensor_ph_window):
    def __init__(self):
        super(sensor_ph,self).__init__()
        self.initUi()
        self.show()
        
        self.ph_x = list(range(5))  # 100 time points
        self.ph_y = [machbase_sql.read_ph_float() for _ in range(5)]  # 100 data points       

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_ph =  self.ph.plot(self.ph_x, self.ph_y, pen=pen)
        
        # 데이터 갱신
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1)  # every 10,000 milliseconds
    
    # x좌표 갱신
    def update_plot_data(self):
        self.ph_x = self.ph_x[1:]  # Remove the first y element.
        self.ph_x.append(self.ph_x[-1]+5)  # Add a new value 1 higher than the last.

        self.ph_y = self.ph_y[1:]  # Remove the first
        self.ph_y.append(machbase_sql.read_ph_float())  # Add a new random value.
        
        self.data_line_ph.setData(self.ph_x, self.ph_y)  # Update the data.

    def initUi(self):
        self.setupUi(self)

    def btn_main(self):
        self.close()                    #클릭시 종료됨.
        
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
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())