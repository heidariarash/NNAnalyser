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
        ChangeClasses.resize(345, 402)
        ChangeClasses.setStyleSheet("background-color: rgb(22, 26, 29);")
        self.centralwidget = QtWidgets.QWidget(ChangeClasses)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 281, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(59, 110, 231, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #F5F3F4;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.add_class = QtWidgets.QPushButton(self.centralwidget)
        self.add_class.setGeometry(QtCore.QRect(117, 280, 121, 30))
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.add_class.setObjectName("add_class")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(50, 330, 100, 30))
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(210, 330, 100, 30))
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4161A;\n"
"}")
        self.cancel.setObjectName("cancel")
        ChangeClasses.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChangeClasses)
        self.statusbar.setObjectName("statusbar")
        ChangeClasses.setStatusBar(self.statusbar)

        self.retranslateUi(ChangeClasses)
        QtCore.QMetaObject.connectSlotsByName(ChangeClasses)

    def retranslateUi(self, ChangeClasses):
        _translate = QtCore.QCoreApplication.translate
        ChangeClasses.setWindowTitle(_translate("ChangeClasses", "Change Output Classes"))
        self.label.setText(_translate("ChangeClasses", "Edit Output Classes Names"))
        self.label_2.setText(_translate("ChangeClasses", "0"))
        self.label_3.setText(_translate("ChangeClasses", "1"))
        self.add_class.setText(_translate("ChangeClasses", "Add Class"))
        self.ok.setText(_translate("ChangeClasses", "OK"))
        self.cancel.setText(_translate("ChangeClasses", "Cancel"))