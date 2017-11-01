# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jingziqi.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 40, 343, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.b22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b22.sizePolicy().hasHeightForWidth())
        self.b22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b22.setFont(font)
        self.b22.setText("")
        self.b22.setObjectName("b22")
        self.gridLayout.addWidget(self.b22, 1, 1, 1, 1)
        self.b32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b32.sizePolicy().hasHeightForWidth())
        self.b32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b32.setFont(font)
        self.b32.setText("")
        self.b32.setObjectName("b32")
        self.gridLayout.addWidget(self.b32, 2, 1, 1, 1)
        self.b33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b33.sizePolicy().hasHeightForWidth())
        self.b33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b33.setFont(font)
        self.b33.setText("")
        self.b33.setObjectName("b33")
        self.gridLayout.addWidget(self.b33, 2, 2, 1, 1)
        self.b12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b12.sizePolicy().hasHeightForWidth())
        self.b12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b12.setFont(font)
        self.b12.setText("")
        self.b12.setObjectName("b12")
        self.gridLayout.addWidget(self.b12, 0, 1, 1, 1)
        self.b23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b23.sizePolicy().hasHeightForWidth())
        self.b23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b23.setFont(font)
        self.b23.setText("")
        self.b23.setObjectName("b23")
        self.gridLayout.addWidget(self.b23, 1, 2, 1, 1)
        self.b21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b21.sizePolicy().hasHeightForWidth())
        self.b21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b21.setFont(font)
        self.b21.setText("")
        self.b21.setObjectName("b21")
        self.gridLayout.addWidget(self.b21, 1, 0, 1, 1)
        self.b13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b13.sizePolicy().hasHeightForWidth())
        self.b13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b13.setFont(font)
        self.b13.setText("")
        self.b13.setObjectName("b13")
        self.gridLayout.addWidget(self.b13, 0, 2, 1, 1)
        self.b11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b11.sizePolicy().hasHeightForWidth())
        self.b11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b11.setFont(font)
        self.b11.setText("")
        self.b11.setObjectName("b11")
        self.gridLayout.addWidget(self.b11, 0, 0, 1, 1)
        self.b31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b31.sizePolicy().hasHeightForWidth())
        self.b31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.b31.setFont(font)
        self.b31.setText("")
        self.b31.setObjectName("b31")
        self.gridLayout.addWidget(self.b31, 2, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(521, 271, 93, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(490, 70, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.infoLabel.setFont(font)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.attackRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.attackRadioBtn.setGeometry(QtCore.QRect(521, 181, 57, 19))
        self.attackRadioBtn.setObjectName("attackRadioBtn")
        self.defendRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.defendRadioBtn.setGeometry(QtCore.QRect(521, 207, 57, 19))
        self.defendRadioBtn.setObjectName("defendRadioBtn")
        self.regrettButton = QtWidgets.QPushButton(self.centralwidget)
        self.regrettButton.setGeometry(QtCore.QRect(521, 312, 93, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.regrettButton.setFont(font)
        self.regrettButton.setObjectName("regretButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resetButton.setText(_translate("MainWindow", "开始"))
        self.attackRadioBtn.setText(_translate("MainWindow", "先手"))
        self.defendRadioBtn.setText(_translate("MainWindow", "后手"))
        self.regrettButton.setText(_translate("MainWindow", "悔棋"))

class Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #mainWindow = QtWidgets.QMainWindow()
        super().setupUi(self)
        #游戏区域
        self.map = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.stepLeft = 9 #剩余步数
        self.bestMove = {'x':1, 'y':1} #最优位置
        self.btnList = []
        self.humanStep = [] 
        self.aiStep = []
        self.btnList.append(self.b11)
        self.btnList.append(self.b12)
        self.btnList.append(self.b13)
        self.btnList.append(self.b21)
        self.btnList.append(self.b22)
        self.btnList.append(self.b23)
        self.btnList.append(self.b31)
        self.btnList.append(self.b32)
        self.btnList.append(self.b33)
        for btn in self.btnList:
            btn.setStyleSheet('background:rgba(0,0,0,50)') #设置透明度
            btn.setEnabled(False)
        self.resetButton.setStyleSheet('background:rgba(255,255,255,150)')
        self.regrettButton.setEnabled(False)
        self.user = 1 #现在轮到谁 1为用户 -1为电脑
        self.attackRadioBtn.setChecked(True)
        self.goFirst = 1 #先手还是后手
        self.gameStart = False #比赛是否已经开始
        self.buildUpConnect()
        
        palette1 = QtGui.QPalette()
        #palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        d = os.path.dirname(__file__)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(os.path.join(d + r'\timg.jpg'))))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True) # 不设置也可以
        
        self.show()

    def buildUpConnect(self):
        for i in self.btnList:
            i.clicked.connect(self.btnClicked)
        self.resetButton.clicked.connect(self.resetBtnClicked)
        self.attackRadioBtn.toggled.connect(self.radioBtnClicked)
        self.defendRadioBtn.toggled.connect(self.radioBtnClicked)
        self.regrettButton.clicked.connect(self.regretBtnClicked)

    def regretBtnClicked(self):
        if self.stepLeft == 0:
            return
        aiMove = self.aiStep.pop()
        humanMove = self.humanStep.pop()
        self.map[aiMove[0]][aiMove[1]] = 0
        self.map[humanMove[0]][humanMove[1]] = 0
        aiIndex = aiMove[0] * 3 + aiMove[1]
        humanIndex = humanMove[0] * 3 + humanMove[1]
        self.btnList[aiIndex].setText('')
        self.btnList[aiIndex].setEnabled(True)
        self.btnList[humanIndex].setText('')
        self.btnList[humanIndex].setEnabled(True)
        self.stepLeft += 2

    def radioBtnClicked(self):
        sender = self.sender()
        if sender == self.attackRadioBtn:
            self.goFirst = 1
            self.user = 1
        else:
            self.goFirst = -1
            self.user = -1

    def resetBtnClicked(self):

        if self.gameStart == 0:
            self.resetButton.setText('重置')
            self.gameStart = 1
            self.attackRadioBtn.setEnabled(False)
            self.defendRadioBtn.setEnabled(False)
            self.regrettButton.setEnabled(True)
            for btn in self.btnList:
                btn.setEnabled(True)
            if self.goFirst == -1:
                self.aiGo()

        else:
            self.gameStart = 0
            self.attackRadioBtn.setEnabled(True)
            self.defendRadioBtn.setEnabled(True)
            self.regrettButton.setEnabled(False)
            self.goFirst = 1
            self.attackRadioBtn.setChecked(True)
            self.resetButton.setText('开始')
            for i in self.btnList:
                i.setEnabled(True)
                i.setText('')

            for i in range(0, 3):
                for j in range(0, 3):
                    self.map[i][j] = 0
            for btn in self.btnList:
                btn.setEnabled(False)
            self.stepLeft = 9
            self.user = 1
            self.infoLabel.setText('')
            self.humanStep.clear()
            self.aiStep.clear()

    def btnClicked(self):
        sender = self.sender()
        index = self.btnList.index(sender)
        rowIndex = int(index / 3)
        colIndex = index % 3
        sender.setEnabled(False)
        if self.user == -1:
            sender.setText('X')
            self.map[rowIndex][colIndex] = -1
        else:
            sender.setText('O')
            self.map[rowIndex][colIndex] = 1
            self.humanStep.append([rowIndex, colIndex])
        self.user = -self.user
        self.stepLeft -= 1
        result = self.checkWinner()
        if result == 0:
            self.aiGo()
            return
        self.handleWinner(result)
        # elif result == -1:
        #     self.infoLabel.setText('AI Win!')
        # elif result == 1:
        #     self.infoLabel.setText('You Win!')
        # else:
        #     self.infoLabel.setText('Draw!')
        # for i in self.btnList:
        #     i.setEnabled(False)
        
    def aiGo(self):
        if self.stepLeft == 9:
            self.bestMove['x'] = 1
            self.bestMove['y'] = 1
        elif self.stepLeft == 8:
            if self.map[1][1] == 0:
                self.bestMove['x'] = 1
                self.bestMove['y'] = 1
            else:
                self.bestMove['x'] = 0
                self.bestMove['y'] = 0
        else:
            self.miniMaxSearch(self.stepLeft, -1000, 1000)
        #print(self.bestMove)
        self.map[self.bestMove['x']][self.bestMove['y']] = -1
        self.aiStep.append([self.bestMove['x'], self.bestMove['y']])
        index = self.bestMove['x'] * 3 + self.bestMove['y']
        self.btnList[index].setText('X')
        self.btnList[index].setEnabled(False)
        self.user = -self.user
        self.stepLeft -= 1
        result = self.checkWinner()
        self.handleWinner(result)
        # if result == 0:
        #     return
        # elif result == -1:
        #     self.infoLabel.setText('AI Win!')
        # elif result == 1:
        #     self.infoLabel.setText('You Win!')
        # else:
        #     self.infoLabel.setText('Draw!')
        # for i in self.btnList:
        #     i.setEnabled(False)

    def miniMaxSearch(self, depth, alpha, beta):
        #print('depth: ', depth)
        #time.sleep(1)
        bestValue = 0
        winner = self.checkWinner()
        # if winner == -1 or winner == 1:
        #     return self.evaluteMap()
        if winner == -1:
            return 1000
        elif winner == 1:
            return -1000
        if depth == 0:
            #return self.evaluteMap()
            return 0

        if self.user == 1:
            bestValue = 1000
        else:
            bestValue = -1000
        
        moveList = []
        moveCount = self.getEmptyMove(moveList)

        for i in range(moveCount):
            move = moveList[i]
            self.makeMove(move)
            value = self.miniMaxSearch(depth - 1, alpha, beta)
            self.unMakeMove(move)
            #print(value)
            if self.user == -1:
                if value > bestValue:
                    bestValue = value    
                    if depth == self.stepLeft:
                        self.bestMove['x'] = int(move / 3)
                        self.bestMove['y'] = move % 3  
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break     
            else:
                if value < bestValue:
                    bestValue = value
                    if depth == self.stepLeft:
                        self.bestMove['x'] = int(move / 3)
                        self.bestMove['y'] = move % 3
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
            #print('bestV:', bestValue)
            #time.sleep(1)
        
        return bestValue

    def getEmptyMove(self, moveList):
        moveList.clear()
        moveCount = 0
        for i in range(3):
            for j in range(3):
                if self.map[i][j] == 0:
                    moveList.append(i * 3 + j)
                    moveCount += 1
        return moveCount

    def makeMove(self, move):
        r = int(move / 3)
        c = move % 3
        self.map[r][c] = self.user
        self.user = -self.user
    
    def unMakeMove(self, move):
        r = int(move / 3)
        c = move % 3
        self.map[r][c] = 0
        self.user = -self.user

    def evaluteMap(self):
        winner = self.checkWinner()
        if winner == -1:
            return 1000
        elif winner == 1:
            return -1000
        count = 0

        tempBoard = self.map[:]

        for i in range(3):
            for j in range(3):
                if self.map[i][j] == 0:
                    tempBoard[i][j] = 1
        
        for i in range(3):
            count += int((tempBoard[i][0] + tempBoard[i][1] + tempBoard[i][2]) / 3)
        for i in range(3):
            count += int((tempBoard[0][i] + tempBoard[1][i] + tempBoard[2][i]) / 3)
        count += int((tempBoard[0][0] + tempBoard[1][1] + tempBoard[2][2]) / 3)
        count += int((tempBoard[2][0] + tempBoard[1][1] + tempBoard[0][2]) / 3)

        for i in range(3):
            for j in range(3):
                if self.map[i][j] == 0:
                    tempBoard[i][j] = -1
        
        for i in range(3):
            count += int((tempBoard[i][0] + tempBoard[i][1] + tempBoard[i][2]) / 3)
        for i in range(3):
            count += int((tempBoard[0][i] + tempBoard[1][i] + tempBoard[2][i]) / 3)
        count += int((tempBoard[0][0] + tempBoard[1][1] + tempBoard[2][2]) / 3)
        count += int((tempBoard[2][0] + tempBoard[1][1] + tempBoard[0][2]) / 3)

        return -count

    def handleWinner(self, result):
        if result == 0:
            return
        elif result == -1:
            self.infoLabel.setText('U Lost!')
        elif result == 1:
            self.infoLabel.setText('U Win!')
        else:
            self.infoLabel.setText('Draw!')
        for i in self.btnList:
            i.setEnabled(False)
        self.regrettButton.setEnabled(False)

    def checkWinner(self):
        #检查行
        for i in range(0, 3):
            if abs(sum(self.map[i])) == 3:
                return self.map[i][0]
        
        #检查列
        for j in range(0, 3):
            if abs(self.map[0][j] + self.map[1][j] + self.map[2][j]) == 3:
                return self.map[0][j]
        
        if (abs(self.map[0][0] + self.map[1][1] + self.map[2][2]) == 3 or
        abs(self.map[0][2] + self.map[1][1] + self.map[2][0] == 3)) :
            return self.map[1][1]

        if self.stepLeft:
            return 0
        return 2
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())