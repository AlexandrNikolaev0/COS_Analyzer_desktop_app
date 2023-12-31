# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkWindow(object):
    """Класс рабочего окна. Сгенерировано в Qt Designer"""

    def setupUi(self, WorkWindow):
        WorkWindow.setObjectName("WorkWindow")
        WorkWindow.setEnabled(True)
        WorkWindow.resize(808, 641)
        WorkWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(WorkWindow)
        self.centralwidget.setStyleSheet("color:FFFFFF\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 591))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
                                     "    alignment: center;\n"
                                     "}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(64, 40, 331, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Controller_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Controller_label.setFont(font)
        self.Controller_label.setWordWrap(True)
        self.Controller_label.setObjectName("Controller_label")
        self.verticalLayout.addWidget(self.Controller_label)
        self.outerTemp_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outerTemp_label.setFont(font)
        self.outerTemp_label.setWordWrap(True)
        self.outerTemp_label.setObjectName("outerTemp_label")
        self.verticalLayout.addWidget(self.outerTemp_label)
        self.innerTemp_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.innerTemp_label.setFont(font)
        self.innerTemp_label.setWordWrap(True)
        self.innerTemp_label.setObjectName("innerTemp_label")
        self.verticalLayout.addWidget(self.innerTemp_label)
        self.cellTemp_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cellTemp_label.setFont(font)
        self.cellTemp_label.setWordWrap(True)
        self.cellTemp_label.setObjectName("cellTemp_label")
        self.verticalLayout.addWidget(self.cellTemp_label)
        self.sampler_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sampler_label.setFont(font)
        self.sampler_label.setWordWrap(True)
        self.sampler_label.setObjectName("sampler_label")
        self.verticalLayout.addWidget(self.sampler_label)
        self.CLMeter_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CLMeter_label.setFont(font)
        self.CLMeter_label.setToolTipDuration(-2)
        self.CLMeter_label.setWordWrap(True)
        self.CLMeter_label.setObjectName("CLMeter_label")
        self.verticalLayout.addWidget(self.CLMeter_label)
        self.statusHeader_label = QtWidgets.QLabel(self.tab)
        self.statusHeader_label.setGeometry(QtCore.QRect(20, 10, 178, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.statusHeader_label.setFont(font)
        self.statusHeader_label.setObjectName("statusHeader_label")
        self.ControllerIndicator_label = QtWidgets.QLabel(self.tab)
        self.ControllerIndicator_label.setGeometry(QtCore.QRect(30, 55, 20, 20))
        self.ControllerIndicator_label.setStyleSheet("\n"
                                                     "background-color: rgb(255, 15, 15);\n"
                                                     "border-radius: 10px;")
        self.ControllerIndicator_label.setText("")
        self.ControllerIndicator_label.setObjectName("ControllerIndicator_label")
        self.outerTempIndicator_label = QtWidgets.QLabel(self.tab)
        self.outerTempIndicator_label.setGeometry(QtCore.QRect(30, 110, 20, 20))
        self.outerTempIndicator_label.setStyleSheet("\n"
                                                    "background-color: rgb(255, 15, 15);\n"
                                                    "border-radius: 10px;")
        self.outerTempIndicator_label.setText("")
        self.outerTempIndicator_label.setObjectName("outerTempIndicator_label")
        self.innerTempIndicator_label = QtWidgets.QLabel(self.tab)
        self.innerTempIndicator_label.setGeometry(QtCore.QRect(30, 170, 20, 20))
        self.innerTempIndicator_label.setStyleSheet("\n"
                                                    "background-color: rgb(255, 15, 15);\n"
                                                    "border-radius: 10px;")
        self.innerTempIndicator_label.setText("")
        self.innerTempIndicator_label.setObjectName("innerTempIndicator_label")
        self.CLMeterIndicator_label = QtWidgets.QLabel(self.tab)
        self.CLMeterIndicator_label.setGeometry(QtCore.QRect(30, 335, 20, 20))
        self.CLMeterIndicator_label.setToolTipDuration(-1)
        self.CLMeterIndicator_label.setWhatsThis("")
        self.CLMeterIndicator_label.setStyleSheet("\n"
                                                  "background-color: rgb(255, 15, 15);\n"
                                                  "border-radius: 10px;")
        self.CLMeterIndicator_label.setText("")
        self.CLMeterIndicator_label.setObjectName("CLMeterIndicator_label")
        self.samplerIndicator_label = QtWidgets.QLabel(self.tab)
        self.samplerIndicator_label.setGeometry(QtCore.QRect(30, 280, 20, 20))
        self.samplerIndicator_label.setStyleSheet("\n"
                                                  "background-color: rgb(255, 15, 15);\n"
                                                  "border-radius: 10px;")
        self.samplerIndicator_label.setText("")
        self.samplerIndicator_label.setObjectName("samplerIndicator_label")
        self.cellTempIndicator_label = QtWidgets.QLabel(self.tab)
        self.cellTempIndicator_label.setGeometry(QtCore.QRect(30, 225, 20, 20))
        self.cellTempIndicator_label.setStyleSheet("\n"
                                                   "background-color: rgb(255, 15, 15);\n"
                                                   "border-radius: 10px;")
        self.cellTempIndicator_label.setText("")
        self.cellTempIndicator_label.setObjectName("cellTempIndicator_label")
        self.graph_label = QtWidgets.QLabel(self.tab)
        self.graph_label.setGeometry(QtCore.QRect(415, 45, 371, 321))
        self.graph_label.setAutoFillBackground(False)
        self.graph_label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: black;")
        self.graph_label.setLineWidth(1)
        self.graph_label.setText("")
        self.graph_label.setObjectName("graph_label")
        self.graphHeader_label = QtWidgets.QLabel(self.tab)
        self.graphHeader_label.setGeometry(QtCore.QRect(420, 10, 178, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graphHeader_label.setFont(font)
        self.graphHeader_label.setObjectName("graphHeader_label")
        self.MplWidget = MplWidget(self.tab)
        self.MplWidget.setGeometry(QtCore.QRect(420, 50, 360, 300))
        self.MplWidget.setObjectName("MplWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 801, 391))
        self.tableWidget.setMinimumSize(QtCore.QSize(801, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScrollMargin(12)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ControllPanel = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ControllPanel.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ControllPanel.setContentsMargins(0, 0, 0, 0)
        self.ControllPanel.setSpacing(10)
        self.ControllPanel.setObjectName("ControllPanel")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem)
        self.StartBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/StartBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartBtn.setIcon(icon)
        self.StartBtn.setObjectName("StartBtn")
        self.ControllPanel.addWidget(self.StartBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem1)
        self.StopBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/StopBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopBtn.setIcon(icon1)
        self.StopBtn.setObjectName("StopBtn")
        self.ControllPanel.addWidget(self.StopBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem2)
        self.SysMethBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/StateBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SysMethBtn.setIcon(icon2)
        self.SysMethBtn.setObjectName("SysMethBtn")
        self.ControllPanel.addWidget(self.SysMethBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem3)
        self.CreSampBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/SampleBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreSampBtn.setIcon(icon3)
        self.CreSampBtn.setObjectName("CreSampBtn")
        self.ControllPanel.addWidget(self.CreSampBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem4)
        self.BinBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BinBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/BinBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BinBtn.setIcon(icon4)
        self.BinBtn.setObjectName("BinBtn")
        self.ControllPanel.addWidget(self.BinBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel.addItem(spacerItem5)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(0, 440, 801, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.descriptin_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.descriptin_label.setGeometry(QtCore.QRect(0, 0, 801, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.descriptin_label.setFont(font)
        self.descriptin_label.setText("")
        self.descriptin_label.setScaledContents(False)
        self.descriptin_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.descriptin_label.setWordWrap(True)
        self.descriptin_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.descriptin_label.setObjectName("descriptin_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ControllPanel_hist = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ControllPanel_hist.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ControllPanel_hist.setContentsMargins(0, 0, 0, 0)
        self.ControllPanel_hist.setSpacing(10)
        self.ControllPanel_hist.setObjectName("ControllPanel_hist")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ControllPanel_hist.addItem(spacerItem11)
        self.tableWidget_hist = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_hist.setGeometry(QtCore.QRect(0, 50, 801, 501))
        self.tableWidget_hist.setMinimumSize(QtCore.QSize(801, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_hist.setFont(font)
        self.tableWidget_hist.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget_hist.setMidLineWidth(0)
        self.tableWidget_hist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_hist.setAutoScrollMargin(12)
        self.tableWidget_hist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_hist.setDragDropOverwriteMode(False)
        self.tableWidget_hist.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_hist.setAlternatingRowColors(True)
        self.tableWidget_hist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_hist.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_hist.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_hist.setWordWrap(True)
        self.tableWidget_hist.setCornerButtonEnabled(False)
        self.tableWidget_hist.setRowCount(1)
        self.tableWidget_hist.setObjectName("tableWidget_hist")
        self.tableWidget_hist.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_hist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_hist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_hist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_hist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_hist.setHorizontalHeaderItem(4, item)
        self.tableWidget_hist.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_hist.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_hist.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_hist.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_hist.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_4, "")
        WorkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        WorkWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkWindow)
        self.statusbar.setObjectName("statusbar")
        WorkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WorkWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(WorkWindow)

    def retranslateUi(self, WorkWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkWindow.setWindowTitle(_translate("WorkWindow", "Рабочее окно"))
        self.Controller_label.setToolTip(_translate("WorkWindow", "Информация о контроллере"))
        self.Controller_label.setStatusTip(_translate("WorkWindow", "Информация о контроллере"))
        self.Controller_label.setText(_translate("WorkWindow", "Контроллер анализатора"))
        self.outerTemp_label.setToolTip(_translate("WorkWindow", "Информация о температуре регулятора внешней трубки1"))
        self.outerTemp_label.setStatusTip(
            _translate("WorkWindow", "Информация о температуре регулятора внешней трубки2"))
        self.outerTemp_label.setText(_translate("WorkWindow", "Регулятор температуры внешней трубки"))
        self.innerTemp_label.setToolTip(
            _translate("WorkWindow", "Информация о температуре регулятора внутренней трубки1"))
        self.innerTemp_label.setStatusTip(
            _translate("WorkWindow", "Информация о температуре регулятора внутренней трубки2"))
        self.innerTemp_label.setText(_translate("WorkWindow", "Регулятор температуры внутренней трубки"))
        self.cellTemp_label.setToolTip(_translate("WorkWindow", "Информация о температуре ячейки1"))
        self.cellTemp_label.setStatusTip(_translate("WorkWindow", "Информация о температуре ячейки2"))
        self.cellTemp_label.setText(_translate("WorkWindow", "Регулятор температуры ячейки"))
        self.sampler_label.setToolTip(_translate("WorkWindow", "Информация об устройстве ввода проб1"))
        self.sampler_label.setStatusTip(_translate("WorkWindow", "Информация об устройстве ввода проб2"))
        self.sampler_label.setText(_translate("WorkWindow", "Устройство ввода проб"))
        self.CLMeter_label.setToolTip(_translate("WorkWindow", "Информация о кулонометре1"))
        self.CLMeter_label.setStatusTip(_translate("WorkWindow", "Информация о кулонометре2"))
        self.CLMeter_label.setText(_translate("WorkWindow", "Кулонометр"))
        self.statusHeader_label.setText(_translate("WorkWindow", "Статус устройств"))
        self.ControllerIndicator_label.setToolTip(_translate("WorkWindow", "Информация о контроллере"))
        self.ControllerIndicator_label.setStatusTip(_translate("WorkWindow", "Информация о контроллере"))
        self.outerTempIndicator_label.setToolTip(
            _translate("WorkWindow", "Информация о температуре регулятора внешней трубки1"))
        self.outerTempIndicator_label.setStatusTip(
            _translate("WorkWindow", "Информация о температуре регулятора внешней трубки2"))
        self.innerTempIndicator_label.setToolTip(
            _translate("WorkWindow", "Информация о температуре регулятора внутренней трубки1"))
        self.innerTempIndicator_label.setStatusTip(
            _translate("WorkWindow", "Информация о температуре регулятора внутренней трубки2"))
        self.CLMeterIndicator_label.setToolTip(_translate("WorkWindow", "Информация о кулонометре1"))
        self.CLMeterIndicator_label.setStatusTip(_translate("WorkWindow", "Информация о кулонометре2"))
        self.samplerIndicator_label.setToolTip(_translate("WorkWindow", "Информация об устройстве ввода проб1"))
        self.samplerIndicator_label.setStatusTip(_translate("WorkWindow", "Информация об устройстве ввода проб2"))
        self.cellTempIndicator_label.setToolTip(_translate("WorkWindow", "Информация о температуре ячейки1"))
        self.cellTempIndicator_label.setStatusTip(_translate("WorkWindow", "Информация о температуре ячейки2"))
        self.graphHeader_label.setText(_translate("WorkWindow", "График"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("WorkWindow", "Статус системы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("WorkWindow", "Визуальный статус устройств"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("WorkWindow", "Состояние"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("WorkWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("WorkWindow", "Время создания"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("WorkWindow", "Запуск отсчета времени"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("WorkWindow", "Время остановки"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("WorkWindow", "Общее время"))
        self.StartBtn.setText(_translate("WorkWindow", "Запуск"))
        self.StopBtn.setText(_translate("WorkWindow", "Стоп"))
        self.SysMethBtn.setText(_translate("WorkWindow", "Системный метод"))
        self.CreSampBtn.setText(_translate("WorkWindow", "Создание группы образцов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("WorkWindow", "Диспетчер задач"))
        self.tableWidget_hist.setSortingEnabled(False)
        item = self.tableWidget_hist.horizontalHeaderItem(0)
        item.setText(_translate("WorkWindow", "Дата"))
        item = self.tableWidget_hist.horizontalHeaderItem(1)
        item.setText(_translate("WorkWindow", "Наименование"))
        item = self.tableWidget_hist.horizontalHeaderItem(2)
        item.setText(_translate("WorkWindow", "Результат 1"))
        item = self.tableWidget_hist.horizontalHeaderItem(3)
        item.setText(_translate("WorkWindow", "Результат 2"))
        item = self.tableWidget_hist.horizontalHeaderItem(4)
        item.setText(_translate("WorkWindow", "Длительность"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("WorkWindow", "История"))


from mplwidget import MplWidget

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WorkWindow = QtWidgets.QMainWindow()
    ui = Ui_WorkWindow()
    ui.setupUi(WorkWindow)
    WorkWindow.show()
    sys.exit(app.exec_())
