# Form implementation generated from reading ui file 'E:\Final_KTLT\USER_INTERFACE\Login\MainWindowSignup.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(950, 711)
        Signup.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=Signup)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 949, 661))
        self.label_2.setStyleSheet("background-color: rgb(242, 248, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(24, 24, 901, 73))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_3.setStyleSheet("font: 75 22pt \"CocogooseProTrial Bold\";\n"
"color: rgb(5, 129, 253);\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius: 20px; ")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(24, 108, 901, 469))
        self.groupBox.setStyleSheet("padding: 5px;\n"
"border-radius: 10px;\n"
"color: rgb(155, 159, 162);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Montserrat Light\";")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(24, 36, 397, 397))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditStaffID = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEditStaffID.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditStaffID.setFont(font)
        self.lineEditStaffID.setToolTipDuration(-1)
        self.lineEditStaffID.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditStaffID.setText("")
        self.lineEditStaffID.setFrame(False)
        self.lineEditStaffID.setObjectName("lineEditStaffID")
        self.verticalLayout_2.addWidget(self.lineEditStaffID)
        self.lineEditName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEditName.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditName.setFont(font)
        self.lineEditName.setToolTipDuration(-1)
        self.lineEditName.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditName.setText("")
        self.lineEditName.setFrame(False)
        self.lineEditName.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditPosition = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEditPosition.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditPosition.setFont(font)
        self.lineEditPosition.setToolTipDuration(-1)
        self.lineEditPosition.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditPosition.setText("")
        self.lineEditPosition.setFrame(False)
        self.lineEditPosition.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEditPosition.setObjectName("lineEditPosition")
        self.verticalLayout_2.addWidget(self.lineEditPosition)
        self.lineEditPhone = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEditPhone.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditPhone.setFont(font)
        self.lineEditPhone.setToolTipDuration(-1)
        self.lineEditPhone.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditPhone.setText("")
        self.lineEditPhone.setFrame(False)
        self.lineEditPhone.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.verticalLayout_2.addWidget(self.lineEditPhone)
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEditEmail.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setToolTipDuration(-1)
        self.lineEditEmail.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditEmail.setText("")
        self.lineEditEmail.setFrame(False)
        self.lineEditEmail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.verticalLayout_2.addWidget(self.lineEditEmail)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(480, 36, 397, 241))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.lineEditUsername.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setToolTipDuration(-1)
        self.lineEditUsername.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditUsername.setText("")
        self.lineEditUsername.setFrame(False)
        self.lineEditUsername.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout_3.addWidget(self.lineEditUsername)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.lineEditPassword.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setToolTipDuration(-1)
        self.lineEditPassword.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setFrame(False)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout_3.addWidget(self.lineEditPassword)
        self.lineEditPasswordagain = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.lineEditPasswordagain.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEditPasswordagain.setFont(font)
        self.lineEditPasswordagain.setToolTipDuration(-1)
        self.lineEditPasswordagain.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEditPasswordagain.setText("")
        self.lineEditPasswordagain.setFrame(False)
        self.lineEditPasswordagain.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPasswordagain.setObjectName("lineEditPasswordagain")
        self.verticalLayout_3.addWidget(self.lineEditPasswordagain)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 288, 397, 145))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonCreate = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonCreate.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButtonCreate.setFont(font)
        self.pushButtonCreate.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButtonCreate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonCreate.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: #35B6E8; /* Màu nền mặc định */\n"
"    font: 57 12pt \"Montserrat Medium\";color: rgb(255, 255, 255);\n"
"    border-radius: 10px; \n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A3E3FC; /* Màu khi di chuột */  \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #35B6E8; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 5px solid #A3E3FC; /* Viền khi nút được focus */ \n"
"}\n"
"\n"
"")
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.verticalLayout.addWidget(self.pushButtonCreate)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButtonClear.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonClear.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: #0581F9; /* Màu nền mặc định */\n"
"    font: 57 12pt \"Montserrat Medium\";color: rgb(255, 255, 255);\n"
"    border-radius: 10px; \n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #87C4FF; /* Màu khi di chuột */  \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0581F9; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 5px solid #87C4FF; /* Viền khi nút được focus */ \n"
"}\n"
"")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.pushButtonCancel = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButtonCancel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonCancel.setStyleSheet("QPushButton {\n"
"    background-color: #FF2090; /* Màu nền mặc định */\n"
"    font: 57 12pt \"Montserrat Medium\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px; \n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFA2D1; /* Màu khi di chuột */  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF2090; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 5px solid #FFA2D1; /* Viền khi nút được focus */ \n"
"}\n"
"")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(444, 96, 2, 250))
        self.label.setMaximumSize(QtCore.QSize(2, 250))
        self.label.setStyleSheet("background-color: rgb(155, 159, 162);")
        self.label.setObjectName("label")
        Signup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Signup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        Signup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Signup)
        self.statusbar.setObjectName("statusbar")
        Signup.setStatusBar(self.statusbar)

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Sign up"))
        self.label_3.setText(_translate("Signup", "Create Account "))
        self.groupBox.setTitle(_translate("Signup", "Staff Information "))
        self.lineEditStaffID.setPlaceholderText(_translate("Signup", "Staff ID"))
        self.lineEditName.setPlaceholderText(_translate("Signup", "Name"))
        self.lineEditPosition.setPlaceholderText(_translate("Signup", "Position"))
        self.lineEditPhone.setPlaceholderText(_translate("Signup", "Phone"))
        self.lineEditEmail.setPlaceholderText(_translate("Signup", "Email"))
        self.lineEditUsername.setPlaceholderText(_translate("Signup", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("Signup", "Password"))
        self.lineEditPasswordagain.setPlaceholderText(_translate("Signup", "Password again(*)"))
        self.pushButtonCreate.setText(_translate("Signup", "Create"))
        self.pushButtonClear.setText(_translate("Signup", "Clear"))
        self.pushButtonCancel.setText(_translate("Signup", "Cancel"))
        self.label.setText(_translate("Signup", "TextLabel"))
