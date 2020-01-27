from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,mainmenu,voting


# The GUI is done automatically by Qt designer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 530)

        # Setting of the layout is done by QTdesigner
        # Textfield username
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(31, 268, 461, 55))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(70)
        font.setKerning(True)
        self.login.setFont(font)
        self.login.setText("")
        self.login.setReadOnly(False)
        self.login.setObjectName("login")

        # Textfield password
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(31, 346, 461, 55))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setWeight(70)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        # Login Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 440, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")

        # Logo GSU
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(40, 0, 421, 251))
        self.logo.setAutoFillBackground(False)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Logo_Web_2020.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.dologin)

    # Function for opening the voting menu
    def OpenMenu(self):
        self.mainmenu = QtWidgets.QMainWindow()
        self.ui = mainmenu.Ui_MainWindow()
        self.ui.setupUi(self.mainmenu)
        login.hide()  # hide the login window
        self.mainmenu.show()  # show the main menu window

    # Translation of the GUI made with QTDesigner into code
    # Generated automatically
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login", "Login"))
        self.login.setPlaceholderText(_translate("MainWindow", "University ID"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))

    # Function of login
    def dologin(self):
        global username  # global username which will be used to display the username in the main menu
        username,password = self.getcredentials()  # Get the credentials (username and password)
        print(username)
        file = open("StudentVoters.txt", "r")  # open the file where are stored the login details of students
        check = False  # boolean variable to check to return true or false whether conditions are satisfied
        logins = []
        for row in file:
            field = row.rstrip('\n').split(",")
            logins.append([field[0],field[1]])  # field[0] = username, field[1] = password
        print(logins)
        for i in range(len(logins)):
            if username == logins[i][0] and password == logins[i][1]:  # if the username and password are correct
                f = open("username.txt", "w")
                f.write(username)
                check = True  # The boolean variable 'check' will set its status into True
                break

        if check:
            self.OpenMenu()  # If Check is True, the program will open the MainMenu window

        else:
            msg = QMessageBox()  # If check is False, the program will show a message box
            msg.setIcon(QMessageBox.Information)
            msg.setText("Username or Password Incorrect")
            msg.setWindowTitle("Failed Login")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        file.close()  # close the file

    def getcredentials(self):
        username = self.login.text()  # from username textfield
        password = self.password.text()  # from password textfield
        return username, password  # returns the values

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(login)
    login.show()  # Show the window
    sys.exit(app.exec_())  # Close the window when we press the close button
