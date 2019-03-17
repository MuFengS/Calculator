# -*- coding: utf-8 -*-

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4 import QtGui,QtCore
import sys

from cal import Ui_Dialog

class Dig_calculator(QDialog,Ui_Dialog):
    # lcd 显示的数字
    lcdstring=''
    # 操作符
    operation=''
    # 被加数
    currentNum=0
    # 加数
    previousNum=0
    # 结果
    result=0

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.action()
    # 与信号槽相关的函数
    def action(self):
        # 按下数字执行的方法
        self.connect(self.b0, QtCore.SIGNAL('clicked()'),self.buttonClicked)
        self.connect(self.b1, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b2, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b3, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b4, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b5, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b6, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b7, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b8, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b9, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b_pont, QtCore.SIGNAL('clicked()'), self.buttonClicked)

        # 按下操作符执行的方法
        self.connect(self.b_plus,QtCore.SIGNAL('clicked()'),self.opClicked)
        self.connect(self.b_sub,QtCore.SIGNAL('clicked()'),self.opClicked)
        self.connect(self.b_mul,QtCore.SIGNAL('clicked()'),self.opClicked)
        self.connect(self.b_div,QtCore.SIGNAL('clicked()'),self.opClicked)

        # 按下清除键执行的方法
        self.connect(self.b_clear, QtCore.SIGNAL('clicked()'), self.clrClicked)

        # 按下等于号执行的方法
        self.connect(self.b_eq, QtCore.SIGNAL('clicked()'), self.eqClicked)

    def buttonClicked(self):
        if len(Dig_calculator.lcdstring) <= 7 :
            Dig_calculator.lcdstring = Dig_calculator.lcdstring + self.sender().text()
            if Dig_calculator.lcdstring == '.':
                Dig_calculator.lcdstring = '0.'
            else:

                if str(Dig_calculator.lcdstring).count('.') > 1:
                    Dig_calculator.lcdstring = str(Dig_calculator.lcdstring)[:-1]
                if str(Dig_calculator.lcdstring).count('.') == 0 and str(Dig_calculator.lcdstring)[0] == '0':
                    Dig_calculator.lcdstring = str(Dig_calculator.lcdstring)[:-1]
                else:
                    self.lcd.display(Dig_calculator.lcdstring)
                    Dig_calculator.currentNum = float(Dig_calculator.lcdstring)
        else:
            pass

    def opClicked(self):
        Dig_calculator.previousNum = Dig_calculator.currentNum
        Dig_calculator.currentNum = 0
        Dig_calculator.lcdstring = ''
        Dig_calculator.operation = self.sender().objectName()

    def clrClicked(self):
        Dig_calculator.lcdstring = ''
        Dig_calculator.operation = ''
        Dig_calculator.currentNum = 0
        Dig_calculator.previousNum = 0
        Dig_calculator.result = 0
        self.lcd.display(0)

    def eqClicked(self):
        if Dig_calculator.operation == 'b_plus':
            Dig_calculator.result = Dig_calculator.previousNum + Dig_calculator.currentNum
            self.lcd.display(Dig_calculator.result)
        if Dig_calculator.operation == 'b_sub':
            Dig_calculator.result = Dig_calculator.previousNum - Dig_calculator.currentNum
            self.lcd.display(Dig_calculator.result)
        if Dig_calculator.operation == 'b_mul':
            Dig_calculator.result = Dig_calculator.previousNum * Dig_calculator.currentNum
            self.lcd.display(Dig_calculator.result)
        if Dig_calculator.operation == 'b_div':
            if Dig_calculator.currentNum == 0:
                self.lcd.display('error')
                Dig_calculator.result = 0
                Dig_calculator.previousNum = 0

            else:
                Dig_calculator.result = Dig_calculator.previousNum / Dig_calculator.currentNum
                self.lcd.display(Dig_calculator.result)

        Dig_calculator.currentNum = Dig_calculator.result
        Dig_calculator.lcdstring = ''

    def closeEvent(self, QCloseEvent):
        reply = QtGui.QMessageBox.question(self,u'警告',u'确认退出',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mycal = Dig_calculator()
    mycal.show()
    sys.exit(app.exec_())


