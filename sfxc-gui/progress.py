# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(996, 363)
        self.gridLayout = QtWidgets.QGridLayout(Dialog1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.scanLabel = QtWidgets.QLabel(Dialog1)
        self.scanLabel.setWordWrap(False)
        self.scanLabel.setObjectName("scanLabel")
        self.hboxlayout.addWidget(self.scanLabel)
        self.scanEdit = QtWidgets.QLineEdit(Dialog1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanEdit.sizePolicy().hasHeightForWidth())
        self.scanEdit.setSizePolicy(sizePolicy)
        self.scanEdit.setReadOnly(True)
        self.scanEdit.setObjectName("scanEdit")
        self.hboxlayout.addWidget(self.scanEdit)
        spacerItem = QtWidgets.QSpacerItem(93, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.hboxlayout, 0, 0, 1, 1)
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(6)
        self._2.setObjectName("_2")
        self.jobLabel = QtWidgets.QLabel(Dialog1)
        self.jobLabel.setWordWrap(False)
        self.jobLabel.setObjectName("jobLabel")
        self._2.addWidget(self.jobLabel)
        self.jobEdit = QtWidgets.QLineEdit(Dialog1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jobEdit.sizePolicy().hasHeightForWidth())
        self.jobEdit.setSizePolicy(sizePolicy)
        self.jobEdit.setReadOnly(True)
        self.jobEdit.setObjectName("jobEdit")
        self._2.addWidget(self.jobEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem1)
        self.gridLayout.addLayout(self._2, 0, 1, 1, 1)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.timeLabel = QtWidgets.QLabel(Dialog1)
        self.timeLabel.setWordWrap(False)
        self.timeLabel.setObjectName("timeLabel")
        self.hboxlayout1.addWidget(self.timeLabel)
        self.timeEdit = QtWidgets.QLineEdit(Dialog1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setObjectName("timeEdit")
        self.hboxlayout1.addWidget(self.timeEdit)
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.gridLayout.addLayout(self.hboxlayout1, 1, 0, 1, 1)
        self._3 = QtWidgets.QHBoxLayout()
        self._3.setContentsMargins(0, 0, 0, 0)
        self._3.setSpacing(6)
        self._3.setObjectName("_3")
        self.subjobLabel = QtWidgets.QLabel(Dialog1)
        self.subjobLabel.setWordWrap(False)
        self.subjobLabel.setObjectName("subjobLabel")
        self._3.addWidget(self.subjobLabel)
        self.subjobEdit = QtWidgets.QLineEdit(Dialog1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subjobEdit.sizePolicy().hasHeightForWidth())
        self.subjobEdit.setSizePolicy(sizePolicy)
        self.subjobEdit.setReadOnly(True)
        self.subjobEdit.setObjectName("subjobEdit")
        self._3.addWidget(self.subjobEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._3.addItem(spacerItem3)
        self.gridLayout.addLayout(self._3, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog1)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
        self.logEdit = QtWidgets.QPlainTextEdit(Dialog1)
        self.logEdit.setReadOnly(True)
        self.logEdit.setObjectName("logEdit")
        self.gridLayout.addWidget(self.logEdit, 3, 0, 1, 2)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.buttonDebug = QtWidgets.QPushButton(Dialog1)
        self.buttonDebug.setEnabled(True)
        self.buttonDebug.setAutoDefault(False)
        self.buttonDebug.setObjectName("buttonDebug")
        self.hboxlayout2.addWidget(self.buttonDebug)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem4)
        self.buttonAbort = QtWidgets.QPushButton(Dialog1)
        self.buttonAbort.setAutoDefault(False)
        self.buttonAbort.setDefault(False)
        self.buttonAbort.setObjectName("buttonAbort")
        self.hboxlayout2.addWidget(self.buttonAbort)
        self.gridLayout.addLayout(self.hboxlayout2, 4, 0, 1, 2)

        self.retranslateUi(Dialog1)
        self.buttonAbort.clicked.connect(Dialog1.abort)
        self.buttonDebug.clicked.connect(Dialog1.create_debug)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Progress"))
        self.scanLabel.setText(_translate("Dialog1", "Scan:"))
        self.jobLabel.setText(_translate("Dialog1", "      Job ID:"))
        self.timeLabel.setText(_translate("Dialog1", "Time:"))
        self.subjobLabel.setText(_translate("Dialog1", "Subjob ID:"))
        self.buttonDebug.setToolTip(_translate("Dialog1", "Let all SFXC processes dump their state"))
        self.buttonDebug.setText(_translate("Dialog1", "Create &Debug"))
        self.buttonDebug.setShortcut(_translate("Dialog1", "Alt+D"))
        self.buttonAbort.setText(_translate("Dialog1", "&Abort"))
        self.buttonAbort.setShortcut(_translate("Dialog1", "Alt+A"))

