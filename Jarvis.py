import time
import sys
# from JarvisUi import Ui_MainWindow
# from PyQt5 import QtCore
# from PyQt5.QtGui import QMovie
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt,QTimer,QTime,QDate
# from PyQt5.uic import loadUiType
# from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
# from os import startfile
from main import jarvisSpeak, recordAudio
from main import jarvis
from main import wishMe
from main import respond

class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self): 
        self.task_Gui()

    def task_Gui(self):
        voice_data = recordAudio()
        respond(voice_data)
              
start = MainThread()

class  Gui_Start(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        from JavisUI import Ui_VoiceAssistant

        self.gui = Ui_VoiceAssistant()
        self.gui.setupUi(self)

        startapp = self.startApp
        exitapp = self.exitApp

        self.gui.pushButtonStart.clicked.connect(startapp)
        self.gui.pushButtonExit.clicked.connect(exitapp)
    
    def startApp(self):
       
        wake_up = recordAudio()

        if 'wake up' in wake_up:  

            showGif = self.showGif

            showGif()

            timer = QtCore.QTimer(self)

            timer.timeout.connect(self.showTimeLive)

            timer.start(999)

            time.sleep(20)

            jarvis()

            time.sleep(1)

            jarvisSpeak('Hello Lovelyo, thanks for waking me up')
            
            time.sleep(1)

            wishMe()   

            start.start()

            

        else:
            print('Nothing..')

    def showGif(self):

        self.gui.label1 = QtGui.QMovie('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\Gui\\..//..//..//files//photos//ironman2.gif')
        self.gui.jarvisGif1.setMovie(self.gui.label1)
        
        self.gui.label2 = QtGui.QMovie('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\Gui\\..//..//..//files//photos//ironman4.gif')
        self.gui.jarvisGif2.setMovie(self.gui.label2)
        
        self.gui.label3 = QtGui.QMovie('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\Gui\\..//..//..//files/photos//ironman5.gif')
        self.gui.jarvisGif3.setMovie(self.gui.label3)
        
        self.gui.label1.start()
        self.gui.label2.start()
        self.gui.label3.start()

    def showTimeLive(self):
        t_time = QtCore.QTime.currentTime()
        time = t_time.toString()
        d_date = QtCore.QDate.currentDate()
        date = d_date.toString()
        labelTime = 'Time : ' + time
        labelDate =  date

        self.gui.time.setText(labelTime)
        self.gui.date.setText(labelDate)

    def exitApp(self):
        print('exit')
        exit()

GuiApp = QtWidgets.QApplication(sys.argv)
jarvisUi = Gui_Start()
jarvisUi.show()
exit(GuiApp.exec_())

