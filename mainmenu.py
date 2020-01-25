# Main menu of the voting system after the login
# The user can choose the position for which they are going to vote
import candidates, login,election, sys,voting
from PyQt5 import QtCore, QtGui, QtWidgets

f = open("username.txt","r")
username = f.read()  # get the user who logged in

# Read the users who have already voted for GSU officers
GSUVoted = open("GSUVoted.txt", "r")
GSUvoters = GSUVoted.read().splitlines()

# Read the users who have already voted for FACH officers
FACHVoted = open("FACHVoted.txt", "r")
FACHvoters = FACHVoted.read().splitlines()

# Read the users who have already voted for FEH officers
FEHVoted = open("FEHVoted.txt", "r")
FEHvoters = FEHVoted.read().splitlines()

# Read the users who have already voted for BS officers
BSVoted = open("BSVoted.txt", "r")
BSvoters = BSVoted.read().splitlines()

# Read the users who have already voted for Presidents
PresVoted = open("PresVoted.txt", "r")
Presvoters = PresVoted.read().splitlines()


# The GUI code is generated automatically by Qt designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Setting of the layout is done by Pyqt Designer
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

        # Creating the buttons:
        # Button 1
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # Button 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # Button 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 460, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # Button 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        # Button 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 350, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(17)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        # Disable the button for an election if it has already been voted by a user
        if username in GSUvoters:
            self.pushButton_2.setEnabled(False)
        if username in FACHvoters:
            self.pushButton_3.setEnabled(False)
        if username in BSvoters:
            self.pushButton_4.setEnabled(False)
        if username in FEHvoters:
            self.pushButton_5.setEnabled(False)
        if username in Presvoters:
            self.pushButton.setEnabled(False)

        #label 1
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

        #label 2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 380, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Button 1, once pressed, the program will open the voting window for the candidate
        self.pushButton.clicked.connect(self.OpenPres)
        self.pushButton_2.clicked.connect(self.OpenGSU)
        self.pushButton_3.clicked.connect(self.OpenFACH)
        self.pushButton_4.clicked.connect(self.OpenBS)
        self.pushButton_5.clicked.connect(self.OpenFEH)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def OpenPres(self):
        # Getting the candidates who are running for President
        voting.election = "President Elections"
        voting.cand0 = candidates.Presidents[0].name
        voting.cand1 = candidates.Presidents[1].name
        voting.cand2 = candidates.Presidents[2].name
        voting.cand3 = candidates.Presidents[3].name
        self.OpenVote()  # calls the function openVote() to open the voting window

    def OpenGSU(self):
        # Getting the candidates who are running for GSU officer
        voting.election = "GSU Elections"
        voting.cand0 = candidates.GSUOfficers[0].name
        voting.cand1 = candidates.GSUOfficers[1].name
        voting.cand2 = candidates.GSUOfficers[2].name
        voting.cand3 = candidates.GSUOfficers[3].name
        self.OpenVote()  # calls the function openVote() to open the voting window

    def OpenFACH(self):
        # Getting the candidates who are running for FACH officer
        voting.election = "FACH Elections"
        voting.cand0 = candidates.FACHOfficers[0].name
        voting.cand1 = candidates.FACHOfficers[1].name
        voting.cand2 = candidates.FACHOfficers[2].name
        voting.cand3 = candidates.FACHOfficers[3].name
        self.OpenVote()  # calls the function openVote() to open the voting window

    def OpenFEH(self):
        # Getting the candidates who are running for FEH officer
        voting.election = "FEH Elections"
        voting.cand0 = candidates.FEHOfficers[0].name
        voting.cand1 = candidates.FEHOfficers[1].name
        voting.cand2 = candidates.FEHOfficers[2].name
        voting.cand3 = candidates.FEHOfficers[3].name
        self.OpenVote()  # calls the function openVote() to open the voting window

    def OpenBS(self):
        # Getting the candidates who are running for BS officer
        voting.election = "BS Elections"
        voting.cand0 = candidates.BSOfficers[0].name
        voting.cand1 = candidates.BSOfficers[1].name
        voting.cand2 = candidates.BSOfficers[2].name
        voting.cand3 = candidates.BSOfficers[3].name
        self.OpenVote()  # calls the function openVote() to open the voting window

    def OpenVote(self):
        self.voting = QtWidgets.QMainWindow()
        self.ui = voting.Ui_MainWindow()
        self.ui.setupUi(self.voting)
        self.voting.show()

    # Translation of the GUI made with QTDesigner into code
    # Generated automatically
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.pushButton.setText(_translate("MainWindow", "Vote for President"))
        self.pushButton_2.setText(_translate("MainWindow", "Vote for GSU Officer"))
        self.pushButton_3.setText(_translate("MainWindow", "Vote for FACH Officer"))
        self.pushButton_4.setText(_translate("MainWindow", "Vote for BS Officer"))
        self.pushButton_5.setText(_translate("MainWindow", "Vote for FEH Officer"))
        self.label.setText(_translate("MainWindow", "Welcome to the voting system {}".format(username)))  # Display the username
        self.label_2.setText(_translate("MainWindow", "The Current Election closes at {}".format(election.GSUElections.enddate)))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow2)
    MainWindow2.show()  # show the window
    sys.exit(app.exec_())  # exit once pressed the closing window buttons
