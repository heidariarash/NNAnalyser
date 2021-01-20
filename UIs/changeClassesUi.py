# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change-classes.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeClasses(object):
    def setupUi(self, ChangeClasses):
        ChangeClasses.setObjectName("ChangeClasses")
        ChangeClasses.resize(345, 421)
        ChangeClasses.setMinimumSize(QtCore.QSize(345, 421))
        ChangeClasses.setMaximumSize(QtCore.QSize(345, 16777215))
        ChangeClasses.setStyleSheet("background-color: rgb(22, 26, 29);")
        self.centralwidget = QtWidgets.QWidget(ChangeClasses)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMaximumSize(QtCore.QSize(153, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        self.ok.setFont(font)
        self.ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok.setStyleSheet("QPushButton {\n"
"    color: #F5F3F4;\n"
"    border: 2px solid #E5383B;\n"
"    border-radius: 15px;\n"
"    background-color: #0B090A;\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.add_class = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.add_class.sizePolicy().hasHeightForWidth())
        self.add_class.setSizePolicy(sizePolicy)
        self.add_class.setMaximumSize(QtCore.QSize(325, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        self.add_class.setFont(font)
        self.add_class.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_class.setStyleSheet("QPushButton {\n"
"    color: #F5F3F4;\n"
"    border: 2px solid #E5383B;\n"
"    border-radius: 15px;\n"
"    background-color: #0B090A;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.add_class.setObjectName("add_class")
        self.gridLayout.addWidget(self.add_class, 1, 0, 1, 2)
        self.delete_class = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.delete_class.sizePolicy().hasHeightForWidth())
        self.delete_class.setSizePolicy(sizePolicy)
        self.delete_class.setMinimumSize(QtCore.QSize(325, 0))
        self.delete_class.setMaximumSize(QtCore.QSize(325, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        self.delete_class.setFont(font)
        self.delete_class.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_class.setStyleSheet("QPushButton {\n"
"    color: #F5F3F4;\n"
"    border: 2px solid #E5383B;\n"
"    border-radius: 15px;\n"
"    background-color: #0B090A;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #BA181B;\n"
"}")
        self.delete_class.setObjectName("delete_class")
        self.gridLayout.addWidget(self.delete_class, 5, 0, 1, 2)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setMaximumSize(QtCore.QSize(152, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        self.cancel.setFont(font)
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel.setStyleSheet("QPushButton {\n"
"    color: #F5F3F4;\n"
"    border: 2px solid #E5383B;\n"
"    border-radius: 15px;\n"
"    background-color: #0B090A;\n"
"    margin-left: 20px;\n"
"    margin-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 6, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"    border:0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border-width: 0px;\n"
"    background-color:#0B090A;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color:#E5383B;\n"
"    border-radius: 4px;    \n"
"    width: 8px;\n"
"    margin-left: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"    background-color:#0B090A;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"     background-color: :#0B090A;\n"
"     height: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 325, 182))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.class0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class0.sizePolicy().hasHeightForWidth())
        self.class0.setSizePolicy(sizePolicy)
        self.class0.setMinimumSize(QtCore.QSize(50, 50))
        self.class0.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.class0.setFont(font)
        self.class0.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.class0.setAlignment(QtCore.Qt.AlignCenter)
        self.class0.setObjectName("class0")
        self.gridLayout_3.addWidget(self.class0, 0, 0, 1, 1)
        self.class0_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class0_name.sizePolicy().hasHeightForWidth())
        self.class0_name.setSizePolicy(sizePolicy)
        self.class0_name.setMinimumSize(QtCore.QSize(100, 50))
        self.class0_name.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setUnderline(False)
        self.class0_name.setFont(font)
        self.class0_name.setStyleSheet("QLineEdit{\n"
"    border: 0px;\n"
"    border-bottom: 1px;\n"
"    color: #F5F3F4;\n"
"}")
        self.class0_name.setAlignment(QtCore.Qt.AlignCenter)
        self.class0_name.setObjectName("class0_name")
        self.gridLayout_3.addWidget(self.class0_name, 0, 1, 1, 1)
        self.class1_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class1_name.sizePolicy().hasHeightForWidth())
        self.class1_name.setSizePolicy(sizePolicy)
        self.class1_name.setMinimumSize(QtCore.QSize(100, 50))
        self.class1_name.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setUnderline(False)
        self.class1_name.setFont(font)
        self.class1_name.setStyleSheet("QLineEdit{\n"
"    border: 0px;\n"
"    color: #F5F3F4;\n"
"}")
        self.class1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.class1_name.setObjectName("class1_name")
        self.gridLayout_3.addWidget(self.class1_name, 2, 1, 1, 1)
        self.class1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class1.sizePolicy().hasHeightForWidth())
        self.class1.setSizePolicy(sizePolicy)
        self.class1.setMinimumSize(QtCore.QSize(50, 50))
        self.class1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.class1.setFont(font)
        self.class1.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.class1.setAlignment(QtCore.Qt.AlignCenter)
        self.class1.setObjectName("class1")
        self.gridLayout_3.addWidget(self.class1, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 2)
        ChangeClasses.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChangeClasses)
        self.statusbar.setObjectName("statusbar")
        ChangeClasses.setStatusBar(self.statusbar)

        self.retranslateUi(ChangeClasses)
        QtCore.QMetaObject.connectSlotsByName(ChangeClasses)

    def retranslateUi(self, ChangeClasses):
        _translate = QtCore.QCoreApplication.translate
        ChangeClasses.setWindowTitle(_translate("ChangeClasses", "Change Output Classes"))
        self.ok.setText(_translate("ChangeClasses", "OK"))
        self.label.setText(_translate("ChangeClasses", "Edit Output Classes Names"))
        self.add_class.setText(_translate("ChangeClasses", "Add Another Class"))
        self.delete_class.setText(_translate("ChangeClasses", "Delete A Class"))
        self.cancel.setText(_translate("ChangeClasses", "Cancel"))
        self.class0.setText(_translate("ChangeClasses", "0"))
        self.class0_name.setText(_translate("ChangeClasses", "Class 0"))
        self.class1_name.setText(_translate("ChangeClasses", "Class 1"))
        self.class1.setText(_translate("ChangeClasses", "1"))