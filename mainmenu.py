import candidates, login,election, sys

from PyQt5 import QtCore, QtGui, QtWidgets

sys.setrecursionlimit(1500)

username = "UsernamePlaceholder"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(280, 40, 421, 251))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Logo_Web_2020.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 460, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 350, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 320, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 380, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.pushButton.clicked.connect(VoteUI())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Vote for President"))
        self.pushButton_2.setText(_translate("MainWindow", "Vote for GSU Officer"))
        self.pushButton_3.setText(_translate("MainWindow", "Vote for FACH Officer"))
        self.pushButton_4.setText(_translate("MainWindow", "Vote for BS Officer"))
        self.pushButton_5.setText(_translate("MainWindow", "Vote for FEH Officer"))
        self.label.setText(_translate("MainWindow", "Welcome {}".format(username)))
        self.label_2.setText(_translate("MainWindow", "The Current Election closes at {}".format(election.GSUElections.enddate)))


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

    def VoteGSU(self):
        candidates.showGSUOfficers()
        a, b, c, d = selectOptions()
        self.writeGSUOfficers(a, b, c, d)

    def VoteFEH(self):
        candidates.showFEHOfficers()
        a, b, c, d = selectOptions()
        self.writeFEHOfficers(a, b, c, d)

    def VoteFACH(self):
        candidates.showFACHOfficers()
        a, b, c, d = selectOptions()
        self.writeFACHOfficers(a, b, c, d)

    def VoteBS(self):
        candidates.showBSOfficers()
        a, b, c, d = selectOptions()
        self.writeBSOfficers(a, b, c, d)

    def VotePres(self):
        candidates.showPresidents()
        a, b, c, d = selectOptions()
        self.writePresidents(a, b, c, d)

    def selectOptions(self):
        a = int(input("select your first option")) - 1
        b = int(input("select your second option")) - 1
        while b == a:
            b = int(input("you cant select the same option twice, please insert someone else")) - 1
        c = int(input("select your third option")) - 1
        while c == a or c == b:
            c = int(input("you cant select the same option twice, please insert someone else")) - 1
        d = int(input("select your fourth option")) - 1
        while d == a or d == b or d == c:
            d = int(input("you cant select the same option twice, please insert someone else")) - 1
        return a, b, c, d


def Voting():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())

def selectOptions():
    a = int(input("select your first option")) - 1
    b = int(input("select your second option")) - 1
    while b == a:
        b = int(input("you cant select the same option twice, please insert someone else")) - 1
    c = int(input("select your third option")) - 1
    while c == a or c == b:
        c = int(input("you cant select the same option twice, please insert someone else")) - 1
    d = int(input("select your fourth option")) - 1
    while d == a or d == b or d == c:
        d = int(input("you cant select the same option twice, please insert someone else")) - 1
    return a, b, c, d


print("your votes were cast")
