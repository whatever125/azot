# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'azot.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setStyleSheet("padding-left: 12px")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.error.setObjectName("error")
        self.gridLayout.addWidget(self.error, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 4)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 2, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 5, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 2, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 5)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 2, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAM (System Administrator Mate)"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Администраторы"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Пользователи УРС"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "HDD"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Объём RAM"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CPU"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Время работы"))
        self.label_2.setText(_translate("MainWindow", "Опрос машин каждые:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.pushButton_5.setText(_translate("MainWindow", "Опрос машин"))
        self.pushButton_3.setText(_translate("MainWindow", "Показать данные о выбранном ПК"))
        self.pushButton_2.setText(_translate("MainWindow", "Экспорт"))
        self.pushButton_4.setText(_translate("MainWindow", "Управление выбранным ПК"))
        self.label_3.setText(_translate("MainWindow", "минут"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Компьютеры"))
        self.pushButton_10.setText(_translate("MainWindow", "Показать данные о пользователе"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отображаемое имя"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID пользователя"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Последняя смена пароля"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Активирован"))
        self.pushButton_9.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_7.setText(_translate("MainWindow", "Экспорт"))
        self.pushButton_8.setText(_translate("MainWindow", "Управление пользователем"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пользователи"))

class Ui_user_management(object):
    def setupUi(self, user_management):
        user_management.setObjectName("user_management")
        user_management.resize(320, 320)
        user_management.setMinimumSize(QtCore.QSize(320, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        user_management.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(user_management)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(user_management)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(user_management)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(user_management)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 9, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(user_management)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 1, 1, 1)
        self.line = QtWidgets.QFrame(user_management)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(user_management)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(user_management)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(user_management)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(user_management)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.error = QtWidgets.QLabel(user_management)
        self.error.setMaximumSize(QtCore.QSize(16777215, 10))
        self.error.setText("")
        self.error.setObjectName("error")
        self.gridLayout.addWidget(self.error, 11, 1, 1, 1)

        self.retranslateUi(user_management)
        QtCore.QMetaObject.connectSlotsByName(user_management)

    def retranslateUi(self, user_management):
        _translate = QtCore.QCoreApplication.translate
        user_management.setWindowTitle(_translate("user_management", "Управление пользователем"))
        self.label_2.setText(_translate("user_management", "Переместить пользователя в группу"))
        self.lineEdit_2.setPlaceholderText(_translate("user_management", "Название группы (без кавычек)"))
        self.pushButton_3.setText(_translate("user_management", "Поиск"))
        self.pushButton.setText(_translate("user_management", "Заблокировать пользователя"))
        self.pushButton_2.setText(_translate("user_management", "Разблокировать пользователя"))
        self.pushButton_4.setText(_translate("user_management", "Переместить"))
        self.label.setText(_translate("user_management", "Найти машину с которой был заблокирован пользователь"))

class Ui_management(object):
    def setupUi(self, management):
        management.setObjectName("management")
        management.resize(640, 480)
        management.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        management.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(management)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.error = QtWidgets.QLabel(management)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        self.error.setText("")
        self.error.setObjectName("error")
        self.gridLayout_2.addWidget(self.error, 9, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(management)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 9, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(management)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 2, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setContentsMargins(9, 9, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 8, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 8, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 5, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 6, 0, 1, 2)

        self.retranslateUi(management)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(management)

    def retranslateUi(self, management):
        _translate = QtCore.QCoreApplication.translate
        management.setWindowTitle(_translate("management", "Управление ПК"))
        self.pushButton_10.setText(_translate("management", "Обновить данные"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("management", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("management", "ID"))
        self.pushButton_4.setText(_translate("management", "Завершить процесс"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("management", "Процессы"))
        self.pushButton_6.setText(_translate("management", "Завершить"))
        self.pushButton_5.setText(_translate("management", "Запустить"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("management", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("management", "Режим запуска"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("management", "Состояние"))
        self.comboBox.setItemText(0, _translate("management", "Manual"))
        self.comboBox.setItemText(1, _translate("management", "Automatic"))
        self.comboBox.setItemText(2, _translate("management", "Disabled"))
        self.comboBox.setItemText(3, _translate("management", "Boot"))
        self.comboBox.setItemText(4, _translate("management", "System"))
        self.pushButton_7.setText(_translate("management", "Изменить режим запуска"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("management", "Службы"))
        self.pushButton_3.setText(_translate("management", "Перезагрузить ПК"))
        self.pushButton.setText(_translate("management", "Открыть редактор реестра"))
        self.pushButton_2.setText(_translate("management", "Выключить ПК"))
        self.pushButton_8.setText(_translate("management", "Вывести из домена"))
        self.lineEdit.setPlaceholderText(_translate("management", "Имя домена"))
        self.pushButton_9.setText(_translate("management", "Добавить в домен"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("management", "Управление ПК"))

class Ui_information(object):
    def setupUi(self, information):
        information.setObjectName("information")
        information.resize(640, 480)
        information.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        information.setWindowIcon(icon)
        information.setStyleSheet("font: 8pt \"Consolas\";")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(information)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(information)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.horizontalLayout_3.addWidget(self.textEdit_7)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_2.addWidget(self.textEdit_3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_3.addWidget(self.textEdit_5)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_4.addWidget(self.textEdit_4)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_4.addWidget(self.textEdit_6)
        self.tabWidget.addTab(self.tab_9, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.error = QtWidgets.QLabel(information)
        self.error.setText("")
        self.error.setObjectName("error")
        self.verticalLayout_2.addWidget(self.error)

        self.retranslateUi(information)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(information)

    def retranslateUi(self, information):
        _translate = QtCore.QCoreApplication.translate
        information.setWindowTitle(_translate("information", "Информация о ПК"))
        self.treeWidget.headerItem().setText(0, _translate("information", "Имя"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("information", "Пользователи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("information", "HDD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("information", "Разделы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("information", "OS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("information", "CPU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("information", "RAM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("information", "Видеокарты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("information", "Сеть"))

class Ui_user_info(object):
    def setupUi(self, user_info):
        user_info.setObjectName("user_info")
        user_info.resize(640, 480)
        user_info.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        user_info.setWindowIcon(icon)
        user_info.setStyleSheet("font: 8pt \"Consolas\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(user_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(user_info)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.error = QtWidgets.QLabel(user_info)
        self.error.setText("")
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)

        self.retranslateUi(user_info)
        QtCore.QMetaObject.connectSlotsByName(user_info)

    def retranslateUi(self, user_info):
        _translate = QtCore.QCoreApplication.translate
        user_info.setWindowTitle(_translate("user_info", "Информация о пользователе"))
