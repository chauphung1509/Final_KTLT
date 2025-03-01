# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\Final_KTLT\USER_INTERFACE\MainWindowLogin.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(951, 711)
        Login.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 12, 445, 637))
        self.label.setStyleSheet("border radius: 500px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Nicolee\\Coding\\Final_KTLT\\USER_INTERFACE\\../RESOURCE/IMAGE/login_bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 949, 661))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 72, 445, 385))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_3.setStyleSheet("font: 75 22pt \"CocogooseProTrial Bold\";\n"
"color: rgb(5, 129, 253);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_4.setStyleSheet("color: rgb(58, 58, 58);\n"
"font: 57 12pt \"Montserrat Medium\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditUsername.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setToolTipDuration(-1)
        self.lineEditUsername.setStyleSheet("padding-left: 10px; padding-right: 10px;\n"
"background-color: rgb(229, 229, 229);\n"
"color: rgb(152, 152, 152);\n"
"font: 25 14pt \"Montserrat Light\";")
        self.lineEditUsername.setText("")
        self.lineEditUsername.setFrame(False)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setStyleSheet("color: rgb(58, 58, 58);\n"
"font: 57 12pt \"Montserrat Medium\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditPassword.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setToolTipDuration(-1)
        self.lineEditPassword.setStyleSheet("padding-left: 10px; padding-right: 10px;\n"
"background-color: rgb(229, 229, 229);\n"
"color: rgb(152, 152, 152);\n"
"font: 25 14pt \"Montserrat Light\";")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setFrame(False)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox.setStyleSheet("color: rgb(58, 58, 58);\n"
"font: 57 12pt \"Montserrat Medium\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonLogin.setMaximumSize(QtCore.QSize(240, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButtonLogin.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonLogin.setStyleSheet("font: 57 12pt \"Montserrat Medium\";\n"
"background-color: rgb(53, 182, 232);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(36, 60, 385, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTimer = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.labelTimer.setMaximumSize(QtCore.QSize(16777215, 70))
        self.labelTimer.setStyleSheet("font: 87 48pt \"Montserrat Black\";\n"
"color: rgb(255, 255, 255);")
        self.labelTimer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTimer.setObjectName("labelTimer")
        self.verticalLayout_2.addWidget(self.labelTimer)
        self.labelDay = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.labelDay.setMaximumSize(QtCore.QSize(16777215, 50))
        self.labelDay.setStyleSheet("font: 63 14pt \"Montserrat Medium\";\n"
"color: rgb(255, 255, 255);")
        self.labelDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDay.setObjectName("labelDay")
        self.verticalLayout_2.addWidget(self.labelDay)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 528, 445, 24))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setStyleSheet("color: rgb(58, 58, 58);\n"
"font: 57 10pt \"Montserrat Medium\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButtonLogin_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin_2.setGeometry(QtCore.QRect(504, 564, 400, 40))
        self.pushButtonLogin_2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButtonLogin_2.setFont(font)
        self.pushButtonLogin_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButtonLogin_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonLogin_2.setStyleSheet("font: 57 12pt \"Montserrat Medium\";\n"
"background-color: rgb(23, 189, 192);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonLogin_2.setObjectName("pushButtonLogin_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 516, 325, 1))
        self.label_6.setMaximumSize(QtCore.QSize(350, 1))
        self.label_6.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_7.raise_()
        self.pushButtonLogin_2.raise_()
        self.label_6.raise_()
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label_3.setText(_translate("Login", "Welcome!"))
        self.label_4.setText(_translate("Login", "Username"))
        self.label_5.setText(_translate("Login", "Password"))
        self.checkBox.setText(_translate("Login", "Remember me"))
        self.pushButtonLogin.setText(_translate("Login", "Login"))
        self.labelTimer.setText(_translate("Login", "00:00"))
        self.labelDay.setText(_translate("Login", "Tuesday, 18 June, 2025"))
        self.label_7.setText(_translate("Login", "You don\'t have account?"))
        self.pushButtonLogin_2.setText(_translate("Login", "Create one"))
