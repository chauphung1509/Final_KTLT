# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\Final_KTLT\USER_INTERFACE\DEFAULT\MainWindowProduct.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindowProduct(object):
    def setupUi(self, MainWindowProduct):
        MainWindowProduct.setObjectName("MainWindowProduct")
        MainWindowProduct.resize(1389, 855)
        MainWindowProduct.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindowProduct.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        MainWindowProduct.setAutoFillBackground(False)
        MainWindowProduct.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        MainWindowProduct.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindowProduct)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 24, 229, 793))
        self.label.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(36, 180, 205, 517))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonProduct = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonProduct.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonProduct.setToolTipDuration(-1)
        self.pushButtonProduct.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonProduct.setAutoFillBackground(False)
        self.pushButtonProduct.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"color: rgb(14, 23, 67);\n"
"background-color: rgb(242, 248, 255)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/album.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonProduct.setIcon(icon)
        self.pushButtonProduct.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonProduct.setObjectName("pushButtonProduct")
        self.verticalLayout.addWidget(self.pushButtonProduct)
        self.pushButtonAdmin = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonAdmin.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonAdmin.setToolTipDuration(-1)
        self.pushButtonAdmin.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonAdmin.setAutoFillBackground(False)
        self.pushButtonAdmin.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/adm2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAdmin.setIcon(icon1)
        self.pushButtonAdmin.setIconSize(QtCore.QSize(35, 35))
        self.pushButtonAdmin.setObjectName("pushButtonAdmin")
        self.verticalLayout.addWidget(self.pushButtonAdmin)
        self.pushButtonVendor = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonVendor.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonVendor.setToolTipDuration(-1)
        self.pushButtonVendor.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonVendor.setAutoFillBackground(False)
        self.pushButtonVendor.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/vendor1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonVendor.setIcon(icon2)
        self.pushButtonVendor.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonVendor.setObjectName("pushButtonVendor")
        self.verticalLayout.addWidget(self.pushButtonVendor)
        self.pushButtonImport = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonImport.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonImport.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonImport.setToolTipDuration(0)
        self.pushButtonImport.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonImport.setAutoFillBackground(False)
        self.pushButtonImport.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/import.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonImport.setIcon(icon3)
        self.pushButtonImport.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonImport.setObjectName("pushButtonImport")
        self.verticalLayout.addWidget(self.pushButtonImport)
        self.pushButtonReceipt = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonReceipt.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonReceipt.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonReceipt.setToolTipDuration(0)
        self.pushButtonReceipt.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonReceipt.setAutoFillBackground(False)
        self.pushButtonReceipt.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/doc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReceipt.setIcon(icon4)
        self.pushButtonReceipt.setIconSize(QtCore.QSize(35, 35))
        self.pushButtonReceipt.setObjectName("pushButtonReceipt")
        self.verticalLayout.addWidget(self.pushButtonReceipt)
        self.pushButtonExport = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonExport.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonExport.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonExport.setToolTipDuration(0)
        self.pushButtonExport.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonExport.setAutoFillBackground(False)
        self.pushButtonExport.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/export.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExport.setIcon(icon5)
        self.pushButtonExport.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.verticalLayout.addWidget(self.pushButtonExport)
        self.pushButtonInvoice = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonInvoice.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonInvoice.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonInvoice.setToolTipDuration(0)
        self.pushButtonInvoice.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonInvoice.setAutoFillBackground(False)
        self.pushButtonInvoice.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        self.pushButtonInvoice.setIcon(icon4)
        self.pushButtonInvoice.setIconSize(QtCore.QSize(35, 35))
        self.pushButtonInvoice.setObjectName("pushButtonInvoice")
        self.verticalLayout.addWidget(self.pushButtonInvoice)
        self.pushButtonInventory = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonInventory.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonInventory.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonInventory.setToolTipDuration(0)
        self.pushButtonInventory.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonInventory.setAutoFillBackground(False)
        self.pushButtonInventory.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/inventory.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonInventory.setIcon(icon6)
        self.pushButtonInventory.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonInventory.setObjectName("pushButtonInventory")
        self.verticalLayout.addWidget(self.pushButtonInventory)
        self.pushButtonStatistic = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonStatistic.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButtonStatistic.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButtonStatistic.setToolTipDuration(0)
        self.pushButtonStatistic.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonStatistic.setAutoFillBackground(False)
        self.pushButtonStatistic.setStyleSheet("font: 63 12pt \"Montserrat SemiBold\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #9b9fa2;\n"
"color: rgb(155, 159, 162);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/statis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonStatistic.setIcon(icon7)
        self.pushButtonStatistic.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonStatistic.setObjectName("pushButtonStatistic")
        self.verticalLayout.addWidget(self.pushButtonStatistic)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(264, 24, 493, 109))
        self.groupBox.setStyleSheet("padding: 5px;\n"
"border-radius: 10px;\n"
"color: rgb(155, 159, 162);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Montserrat Light\";")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(12, 36, 217, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNew = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButtonNew.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButtonNew.setToolTipDuration(-1)
        self.pushButtonNew.setStyleSheet("QPushButton {\n"
"    background-color: #FF2090; /* Màu nền mặc định */\n"
"\n"
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
        self.pushButtonNew.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNew.setIcon(icon8)
        self.pushButtonNew.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.horizontalLayout.addWidget(self.pushButtonNew)
        self.pushButtonEdit = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButtonEdit.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButtonEdit.setStyleSheet("QPushButton {\n"
"    background-color: #35B6E8; /* Màu nền mặc định */\n"
"\n"
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
"")
        self.pushButtonEdit.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonEdit.setIcon(icon9)
        self.pushButtonEdit.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButtonDelete.setStyleSheet("QPushButton {\n"
"    background-color: #0581F9; /* Màu nền mặc định */\n"
"\n"
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
        self.pushButtonDelete.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon10)
        self.pushButtonDelete.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(2, 16777215))
        self.label_3.setStyleSheet("background-color: rgb(155, 159, 162);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButtonExcel = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonExcel.setGeometry(QtCore.QRect(240, 36, 241, 61))
        self.pushButtonExcel.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Màu nền mặc định */\n"
"    border-radius: 10px; \n"
"    border: 2px solid #79DADC;\n"
"    padding: 5px;\n"
"    color: #79DADC;\n"
"    font: 63 12pt \"Montserrat SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #79DADC; /* Màu khi di chuột */  \n"
"    color: #FFFFFF;\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFFFFF; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #79DADC; /* Màu khi di chuột */  \n"
"    border:5px solid #B4EDEE;\n"
"    color: #FFFFFF;\n"
"\n"
"}\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/exc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExcel.setIcon(icon11)
        self.pushButtonExcel.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonExcel.setObjectName("pushButtonExcel")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -12, 1393, 817))
        self.label_2.setStyleSheet("background-color: rgb(242, 248, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(768, 24, 601, 109))
        self.groupBox_2.setStyleSheet("padding: 5px;\n"
"border-radius: 10px;\n"
"color: rgb(155, 159, 162);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Montserrat Light\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(156, 36, 361, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(528, 36, 61, 61))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #35B6E8; /* Màu nền mặc định */\n"
"    border-radius: 10px; \n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8EDAF8; /* Màu khi di chuột */  \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #35B6E8; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 5px solid #8EDAF8; /* Viền khi nút được focus */ \n"
"}\n"
"")
        self.pushButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(12, 36, 133, 61))
        self.comboBox.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"padding: 10px;")
        self.comboBox.setEditable(False)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(264, 143, 1105, 673))
        self.tableWidget.setToolTip("")
        self.tableWidget.setStyleSheet("padding: 5px;\n"
"border-radius: 10px;\n"
"color: rgb(14, 23, 67);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 57 10pt \"Montserrat Medium\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(36, 36, 205, 61))
        self.label_4.setStyleSheet("color: rgb(53, 182, 232);\n"
"font: 87 30pt \"Montserrat Black\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(36, 96, 205, 37))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 15pt \"Montserrat SemiBold\";\n"
"background-color: rgb(5, 129, 249);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 720, 157, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* Màu nền mặc định */\n"
"    color: #D23435;\n"
"    font: 8120 17pt \"Montserrat Bold\";\n"
"    border-radius: 10px; \n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #D23435;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D23435; /* Màu khi nhấn */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #D23435;\n"
"}\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("/RESOURCE/ICON/turnoff.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.tableWidget.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        MainWindowProduct.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindowProduct)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1389, 26))
        self.menubar.setObjectName("menubar")
        MainWindowProduct.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindowProduct)
        self.statusbar.setObjectName("statusbar")
        MainWindowProduct.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowProduct)
        QtCore.QMetaObject.connectSlotsByName(MainWindowProduct)

    def retranslateUi(self, MainWindowProduct):
        _translate = QtCore.QCoreApplication.translate
        MainWindowProduct.setWindowTitle(_translate("MainWindowProduct", "Product"))
        self.pushButtonProduct.setText(_translate("MainWindowProduct", "  Product"))
        self.pushButtonAdmin.setText(_translate("MainWindowProduct", "  Admin"))
        self.pushButtonVendor.setText(_translate("MainWindowProduct", "  Vendor"))
        self.pushButtonImport.setText(_translate("MainWindowProduct", "  Import"))
        self.pushButtonReceipt.setText(_translate("MainWindowProduct", " Good rec."))
        self.pushButtonExport.setText(_translate("MainWindowProduct", "  Export"))
        self.pushButtonInvoice.setText(_translate("MainWindowProduct", "  Invoice"))
        self.pushButtonInventory.setText(_translate("MainWindowProduct", " Inventory"))
        self.pushButtonStatistic.setText(_translate("MainWindowProduct", "  Statistic"))
        self.groupBox.setTitle(_translate("MainWindowProduct", "Functions"))
        self.pushButtonNew.setToolTip(_translate("MainWindowProduct", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff2090;\">New</span></p></body></html>"))
        self.pushButtonEdit.setToolTip(_translate("MainWindowProduct", "<html><head/><body><p><span style=\" font-size:12pt; color:#35b6e8;\">Edit</span></p></body></html>"))
        self.pushButtonDelete.setToolTip(_translate("MainWindowProduct", "<html><head/><body><p><span style=\" font-size:12pt; color:#0581f9;\">Delete</span></p></body></html>"))
        self.pushButtonExcel.setText(_translate("MainWindowProduct", "EXPORT EXCEL"))
        self.groupBox_2.setTitle(_translate("MainWindowProduct", "Search "))
        self.lineEdit.setPlaceholderText(_translate("MainWindowProduct", "*Search term"))
        self.comboBox.setCurrentText(_translate("MainWindowProduct", "All"))
        self.comboBox.setItemText(0, _translate("MainWindowProduct", "All"))
        self.comboBox.setItemText(1, _translate("MainWindowProduct", "ID"))
        self.comboBox.setItemText(2, _translate("MainWindowProduct", "Title"))
        self.comboBox.setItemText(3, _translate("MainWindowProduct", "Artist"))
        self.comboBox.setItemText(4, _translate("MainWindowProduct", "Year"))
        self.comboBox.setItemText(5, _translate("MainWindowProduct", "Category"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowProduct", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowProduct", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowProduct", "Artist"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowProduct", "Year"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowProduct", "Category"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowProduct", "Price"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowProduct", "Stock"))
        self.label_4.setText(_translate("MainWindowProduct", "00:00"))
        self.label_5.setText(_translate("MainWindowProduct", "Hi Admin!"))
        self.pushButton_2.setText(_translate("MainWindowProduct", "EXIT"))
