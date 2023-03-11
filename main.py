from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer 
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import psutil


class Ui_Form(object):
    def getBattry(self):
        self.battery = psutil.sensors_battery()
        bPercent = self.battery.percent
        #bPercent = self.x
        #print(bPercent, self.battery.percent)
        if bPercent >= 36:
            self.progressBar.setValue(bPercent)
            self.progressBar_2.setValue(36)
        elif bPercent < 36:
            self.progressBar.setValue(36)
            self.progressBar_2.setValue(bPercent)
        #self.x -=1
    def setupUi(self, Form):
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))
        Form.setObjectName("Form")
        Form.resize(sizeObject.width(), sizeObject.height())
        Form.setStyleSheet("""QProgressBar:horizontal
{
    background-color: rgba(0, 0, 0, 0);
    border: 0.1ex solid #31363b;
    border-radius: 0.3ex;
    height: 0.5ex;
    text-align: right;
    
}

QProgressBar::chunk:horizontal
{
    background-color: #3daee9;
    border: 0.1ex transparent;
    border-radius: 0.3ex;
}
QProgressBar:vertical
{
    background-color: rgba(0, 0, 0, 0);
    border: 0.1ex solid #31363b;
    border-radius: 0.3ex;
    height: 0.5ex;
    text-align: right;
}

QProgressBar::chunk:vertical
{
    background-color: #3daee9;
    border: 0.1ex transparent;
    border-radius: 0.3ex;
}
""")
        Form.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        #class
        self.battery = psutil.sensors_battery()
        self.plugged = self.battery.power_plugged
        #
        #va
        #self.x=100
        #
        self.timer_1 = QTimer()
        self.timer_1.timeout.connect(self.getBattry)
        
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, sizeObject.width(), 3))
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(36)

        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(sizeObject.width()-3, 3, 3, sizeObject.height()))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_2.setProperty("value", 100)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar")
        self.progressBar_2.setMaximum(36)
        self.progressBar_2.setMinimum(0)

        bPercent = self.battery.percent
        print(bPercent)
        if bPercent >= 36:
            self.progressBar.setValue(bPercent)
            self.progressBar_2.setValue(36)
        elif bPercent < 36:
            self.progressBar.setValue(36)
            self.progressBar_2.setValue(bPercent)
            
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.timer_1.start(1000)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
