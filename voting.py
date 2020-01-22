
import candidates
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

global election

election = 0
cand0 = 0
cand1 = 0
cand2 = 0
cand3 = 0

class Ui_MainWindow(object):
    global votes
    votes = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(50, 20, 241, 151))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Logo_Web_2020.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 50, 451, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 280, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 280, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 410, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 410, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 210, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 611, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagesgui/divider-line-png-15.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda: self.setvote(0))
        self.pushButton_2.clicked.connect(lambda: self.setvote(1))
        self.pushButton_3.clicked.connect(lambda: self.setvote(2))
        self.pushButton_4.clicked.connect(lambda: self.setvote(3))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if election == "president":
            cand0 = candidates.BSOfficers[0].name
            cand1 = candidates.BSOfficers[1].name
            cand2 = candidates.BSOfficers[2].name
            cand3 = candidates.BSOfficers[3].name

    def setvote(self,x):
        votes.append(x)
        if x == 0:
            self.pushButton.setEnabled(False)
        if x == 1:
            self.pushButton_2.setEnabled(False)
        if x == 2:
            self.pushButton_3.setEnabled(False)
        if x == 3:
            self.pushButton_4.setEnabled(False)
        if len(votes) == 4:
            if election == "GSU Elections":
                writeGSUOfficers(votes[0],votes[1],votes[2],votes[3])
            if election == "FACH Elections":
                writeFACHOfficers(votes[0],votes[1],votes[2],votes[3])
            if election == "BS Elections":
                writeBSOfficers(votes[0],votes[1],votes[2],votes[3])
            if election == "FEH Elections":
                writeFEHOfficers(votes[0],votes[1],votes[2],votes[3])
            if election == "President Elections":
                writePresidents(votes[0],votes[1],votes[2],votes[3])

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Your Votes were Cast Succesfully")
            msg.setWindowTitle("Voting Complete")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "{}".format(election)))
        self.pushButton.setText(_translate("MainWindow","{}".format(cand0)))
        self.pushButton_2.setText(_translate("MainWindow","{}".format(cand1)))
        self.pushButton_3.setText(_translate("MainWindow","{}".format(cand2)))
        self.pushButton_4.setText(_translate("MainWindow","{}".format(cand3)))
        self.label_2.setText(_translate("MainWindow","Choose your {} option".format("Option")))

    def writeGSUOfficers(self,a, b, c, d):
        f = open("votesGSU.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

    def writeFEHOfficers(self,a, b, c, d):
        f = open("votesFEH.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

    def writeFACHOfficers(self,a, b, c, d):
        f = open("votesFACH.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

    def writeBSOfficers(self,a, b, c, d):
        f = open("votesBS.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

    def writePresidents(self,a, b, c, d):
        f = open("votesPres.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def voteGSU():
    global election,cand0,cand1,cand2,cand3

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    writeGSUOfficers(votes[0],votes[1],votes[2],votes[3])
    sys.exit(app.exec_())

def voteFACH():
    global election,cand0,cand1,cand2,cand3

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def voteFEH():
    global election,cand0,cand1,cand2,cand3

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def voteBS():
    global election,cand0,cand1,cand2,cand3
    election = "BS Elections"
    cand0 = candidates.BSOfficers[0].name
    cand1 = candidates.BSOfficers[1].name
    cand2 = candidates.BSOfficers[2].name
    cand3 = candidates.BSOfficers[3].name
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def writeGSUOfficers(a, b, c, d):
        f = open("votesGSU.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeFEHOfficers(a, b, c, d):
        f = open("votesFEH.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeFACHOfficers(a, b, c, d):
        f = open("votesFACH.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeBSOfficers(a, b, c, d):
        f = open("votesBS.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writePresidents(a, b, c, d):
        f = open("votesPres.txt", "a")
        f.write("%s,%s,%s,%s\n" % (a, b, c, d))