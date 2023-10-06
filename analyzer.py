# -*- coding: utf-8 -*-
import json
import time
import threading
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import serial.tools.list_ports
import glob
from workWindow import Ui_WorkWindow
from sysMethWindow import Ui_sysMethWindow
from sysMethTask import sysMethTask
from creSampWindow import Ui_creSampWindow
from sampTask import sampleTask
from authWindow import Ui_AuthWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import resources


def portSearch():
    """ Lists serial port names

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def make_connection_request():
    """Формирует команду для проверки связи с контроллером"""
    message = {"cmd": "get_status"}
    return json.dumps(message)


def make_stop_request():
    """Формирует команду для остановки эксперимента и сброса режима"""
    message = {"cmd": "stop"}
    return json.dumps(message)


def make_updateDevicesStatusJson():
    """Формирует команду для получения данных о состоянии анализатора"""
    message = {"cmd": "get_devicesStatus"}
    return json.dumps(message)


def make_updateDevicesDataJson():
    """Формирует команду для получения данных о состоянии анализатора"""
    message = {"cmd": "get_devicesParams"}
    return json.dumps(message)


def make_updatePlotDataJson():
    """Формирует команду для получения данных о состоянии анализатора"""
    message = {"cmd": "get_plotData"}
    return json.dumps(message)


def getRGBFromText(colorText):
    """Принимает текстовую запись цвета и переводет в числовой формат RGB"""
    if colorText == "red":
        return "255, 15, 15"
    if colorText == "green":
        return "15, 255, 15"
    if colorText == "blue":
        return "15, 15, 255"
    if colorText == "yellow":
        return "255, 120, 15"


class ClickableLabel(QtWidgets.QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
    def mousePressEvent(self, event):
        print("клик")


class Ui_ConnectWindow(object):
    '''
    Класс всего приложения, запуск которого начинается с окна подключения.
    '''
    serialAnalyzer = serial.Serial()
    statusMessage = ""
    selectedRow = -1
    taskTable = []
    isUpdatable = False
    isUpdates = False
    echoMode = False
    exitFlag = True
    username = ""

    # Form implementation generated from reading ui file 'authWindow.ui'
    #
    # Created by: PyQt5 UI code generator 5.15.4
    def setupUi(self, ConnectWindow):
        '''
        Метод инициализации окна подключения.
        Преимущественно сгенерирован в Qt Designer.
        :param ConnectWindow:
        :return:
        '''
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.setEnabled(True)
        ConnectWindow.resize(1440, 838)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectWindow.sizePolicy().hasHeightForWidth())
        ConnectWindow.setSizePolicy(sizePolicy)
        ConnectWindow.setMinimumSize(QtCore.QSize(1440, 838))
        ConnectWindow.setMaximumSize(QtCore.QSize(1440, 838))
        ConnectWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        ConnectWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        ConnectWindow.setStyleSheet("background-image: url(:/imgs/authBackground.png);")
        self.centralwidget = QtWidgets.QWidget(ConnectWindow)
        self.centralwidget.setStyleSheet("color:FFFFFF\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(429, 211, 582, 417))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(582, 417))
        self.widget.setMaximumSize(QtCore.QSize(582, 417))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget { /* Auto layout */\n"
                                  "\n"
                                  "\n"
                                  "position: absolute;\n"
                                  "width: 582px;\n"
                                  "height: 439px;\n"
                                  "left: 80px;\n"
                                  "top: 60px;\n"
                                  "\n"
                                  "background: #FFFFFF;\n"
                                  "border-radius: 6px; }")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(70, 24, 70, 50)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(149)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(149, 81))
        self.label.setMaximumSize(QtCore.QSize(149, 81))
        self.label.setStyleSheet("image: url(:/imgs/logo-gazprom-neft.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.devices_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devices_label.sizePolicy().hasHeightForWidth())
        self.devices_label.setSizePolicy(sizePolicy)
        self.devices_label.setStyleSheet("#devices_label{\n"
                                         "font-family: \'Segoe UI\';\n"
                                         "font-style: normal;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 18px;\n"
                                         "line-height: 150%;\n"
                                         "color: rgba(0, 32, 51, 0.6);\n"
                                         "}")
        self.devices_label.setTextFormat(QtCore.Qt.PlainText)
        self.devices_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.devices_label.setIndent(0)
        self.devices_label.setObjectName("devices_label")
        self.verticalLayout_2.addWidget(self.devices_label)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.devices_comboBox = QtWidgets.QComboBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devices_comboBox.sizePolicy().hasHeightForWidth())
        self.devices_comboBox.setSizePolicy(sizePolicy)
        self.devices_comboBox.setMinimumSize(QtCore.QSize(0, 48))
        self.devices_comboBox.setMaximumSize(QtCore.QSize(16777215, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.devices_comboBox.setFont(font)
        self.devices_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.devices_comboBox.setStyleSheet("#devices_comboBox{\n"
                                            "\n"
                                            "height:48px;\n"
                                            "/* control-default/bg */\n"
                                            "font-family: \'Segoe UI\';\n"
                                            "font-weight: 400;\n"
                                            "font-style: normal;\n"
                                            "font-size: 18px;\n"
                                            "\n"
                                            "padding-left: 13px;\n"
                                            "/* control-default/bg-border */\n"
                                            "\n"
                                            "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                            "border-radius: 4px;\n"
                                            "\n"
                                            "color: black;\n"
                                            "outline: 0px;\n"
                                            "}\n"
                                            "\n"
                                            "#devices_comboBox::drop-down{\n"
                                            "border: 0px;\n"
                                            "width: 48px;\n"
                                            "}\n"
                                            "\n"
                                            "#devices_comboBox::down-arrow {\n"
                                            "    image: url(:/imgs/arrowComboBox.png);\n"
                                            "width: 48px;\n"
                                            "}\n"
                                            "\n"
                                            "#devices_comboBox::on {\n"
                                            "border: 1px solid #0091FF;\n"
                                            "outline: 0px;\n"
                                            "}\n"
                                            "\n"
                                            "#devices_comboBox QListView {\n"
                                            "outline-color: #fff;\n"
                                            "background-color: #fff;\n"
                                            "\n"
                                            "font-family: \'Segoe UI\';\n"
                                            "font-weight: 400;\n"
                                            "font-style: normal;\n"
                                            "font-size: 18px;\n"
                                            "\n"
                                            "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                            "\n"
                                            "border-radius: 4px;\n"
                                            "margin-top: 7px;\n"
                                            "outline: 0px;\n"
                                            "\n"
                                            "selection-background-color: rgba(0, 32, 51, 0.05);\n"
                                            "selection-color: black;\n"
                                            "\n"
                                            "padding-top:10px;\n"
                                            "padding-bottom:10px;\n"
                                            "padding-left:12px;\n"
                                            "padding-right:12px;\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "#devices_comboBox QAbstractItemView::text {\n"
                                            "\n"
                                            "padding:10px;\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.devices_comboBox.setEditable(False)
        self.devices_comboBox.setMaxVisibleItems(10)
        self.devices_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.devices_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.devices_comboBox.setIconSize(QtCore.QSize(48, 48))
        self.devices_comboBox.setDuplicatesEnabled(False)
        self.devices_comboBox.setFrame(False)
        self.devices_comboBox.setObjectName("devices_comboBox")
        self.devices_comboBox.addItem("")
        self.devices_comboBox.addItem("")
        self.devices_comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.devices_comboBox)
        self.connect_statusLabel = QtWidgets.QLabel(self.widget_2)
        self.connect_statusLabel.setStyleSheet("#connect_statusLabel{\n"
                                               "min-height:14px;\n"
                                               "max-height:14px;\n"
                                               "height:14px;\n"
                                               "padding-left:13px;\n"
                                               "color: #EB3333;\n"
                                               "font-family: \'Segoe UI\';\n"
                                               "font-style: normal;\n"
                                               "font-weight: 400;\n"
                                               "font-size: 12px;\n"
                                               "line-height: 120%;\n"
                                               "}")
        self.connect_statusLabel.setText("")
        self.connect_statusLabel.setObjectName("connect_statusLabel")
        self.verticalLayout_4.addWidget(self.connect_statusLabel)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.connect_pushButton = QtWidgets.QPushButton(self.widget)
        self.connect_pushButton.setStyleSheet("#connect_pushButton{\n"
                                              "width: 441px;\n"
                                              "height: 40px;\n"
                                              "\n"
                                              "/* control-primary/bg */\n"
                                              "\n"
                                              "\n"
                                              "background: #0078D2;\n"
                                              "border-radius: 20px;\n"
                                              "\n"
                                              "\n"
                                              "font-family: \'Segoe UI\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 16px;\n"
                                              "line-height: 40px;\n"
                                              "\n"
                                              "\n"
                                              "/* control-primary/typo */\n"
                                              "\n"
                                              "color: #FFFFFF;\n"
                                              "}\n"
                                              "\n"
                                              "#connect_pushButton::hover{\n"
                                              "background: rgb(0, 134, 229);\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "#connect_pushButton::pressed{\n"
                                              "\n"
                                              "border: 4px solid rgb(0, 101, 173);\n"
                                              "}")
        self.connect_pushButton.setAutoDefault(False)
        self.connect_pushButton.setDefault(False)
        self.connect_pushButton.setFlat(False)
        self.connect_pushButton.setObjectName("connect_pushButton")
        self.verticalLayout_3.addWidget(self.connect_pushButton)
        self.updateDevices_pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateDevices_pushButton.sizePolicy().hasHeightForWidth())
        self.updateDevices_pushButton.setSizePolicy(sizePolicy)
        self.updateDevices_pushButton.setStyleSheet("#updateDevices_pushButton{\n"
                                                    "width: 441px;\n"
                                                    "height: 40px;\n"
                                                    "\n"
                                                    "/* control-primary/bg */\n"
                                                    "\n"
                                                    "\n"
                                                    "background: #fff;\n"
                                                    "border-radius: 20px;\n"
                                                    "border: 1px solid #0078D2;\n"
                                                    "\n"
                                                    "\n"
                                                    "font-family: \'Segoe UI\';\n"
                                                    "font-style: normal;\n"
                                                    "font-weight: 400;\n"
                                                    "font-size: 16px;\n"
                                                    "line-height: 40px;\n"
                                                    "\n"
                                                    "\n"
                                                    "/* control-primary/typo */\n"
                                                    "\n"
                                                    "color: #0078D2;\n"
                                                    "}\n"
                                                    "\n"
                                                    "#updateDevices_pushButton::hover{\n"
                                                    "background: rgb(205, 238, 255);\n"
                                                    "\n"
                                                    "}\n"
                                                    "\n"
                                                    "#updateDevices_pushButton::pressed{\n"
                                                    "\n"
                                                    "border: 4px solid rgb(139, 205, 255);\n"
                                                    "}")
        self.updateDevices_pushButton.setAutoDefault(False)
        self.updateDevices_pushButton.setDefault(False)
        self.updateDevices_pushButton.setFlat(False)
        self.updateDevices_pushButton.setObjectName("updateDevices_pushButton")
        self.verticalLayout_3.addWidget(self.updateDevices_pushButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        ConnectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConnectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        ConnectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConnectWindow)
        self.statusbar.setObjectName("statusbar")
        ConnectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConnectWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectWindow)
        """Добавленный метод, определяющий логику работы элементов интерфейса приложения"""
        self.add_functions()

    def retranslateUi(self, ConnectWindow):

        """Сгенерировано с помощью Qt Designer"""
        _translate = QtCore.QCoreApplication.translate
        ConnectWindow.setWindowTitle(_translate("ConnectWindow", "Окно подключения"))
        self.devices_label.setText(_translate("ConnectWindow", "Доступные устройства"))

        self.connect_pushButton.setText(_translate("ConnectWindow", "Подключить устройство"))
        self.updateDevices_pushButton.setText(_translate("ConnectWindow", "Обновить устройства"))

    def updatePortList(self):
        """Обновляет выпадающий список портов"""

        clear = self.devices_comboBox.clear()
        portSearch()
        for i in serial.tools.list_ports.comports():
            print(i)
            self.devices_comboBox.addItem(str(i))
        self.statusMessage = "Доступные устройства обновлены"
        self.connect_statusLabel.setText(self.statusMessage)
        self.connect_statusLabel.setStyleSheet("#connect_statusLabel{\n"
                                               "min-height:14px;\n"
                                               "max-height:14px;\n"
                                               "height:14px;\n"
                                               "padding-left:13px;\n"
                                               "color: green;\n"
                                               "font-family: \'Segoe UI\';\n"
                                               "font-style: normal;\n"
                                               "font-weight: 400;\n"
                                               "font-size: 12px;\n"
                                               "line-height: 120%;\n"
                                               "}")

    def sendJson(self, jsonData):
        """Отправляет любую команду и возвращает ответ (если дождется)"""
        try:
            self.serialAnalyzer.write(bytes(jsonData, 'utf-8'))
            answerMessage = self.serialAnalyzer.readline()
            print(answerMessage)
            answerMessage = self.serialAnalyzer.readline()
            print(answerMessage)
            return answerMessage
        except serial.SerialTimeoutException:
            return "Устройство не отвечает"

    def sendJsonNoAnswer(self, jsonData):
        """Отправляет любую команду и не ждет ответ"""
        self.serialAnalyzer.write(bytes(jsonData, 'utf-8'))

    def connectUSB(self, comPort):
        """Подключается к контроллеру по Serial"""
        if not self.serialAnalyzer.port == comPort:
            self.serialAnalyzer.port = comPort
        self.serialAnalyzer.baudrate = 115200
        self.serialAnalyzer.timeout = 3
        self.serialAnalyzer.writeTimeout = 3

        if not self.serialAnalyzer.is_open:
            try:
                self.serialAnalyzer.open()
            except serial.SerialException as e:
                self.statusMessage = "Не удается подключиться к устройству"
                self.connect_statusLabel.setText(self.statusMessage)
                self.connect_statusLabel.setStyleSheet("#connect_statusLabel{\n"
                                                       "min-height:14px;\n"
                                                       "max-height:14px;\n"
                                                       "height:14px;\n"
                                                       "padding-left:13px;\n"
                                                       "color: #EB3333;\n"
                                                       "font-family: \'Segoe UI\';\n"
                                                       "font-style: normal;\n"
                                                       "font-weight: 400;\n"
                                                       "font-size: 12px;\n"
                                                       "line-height: 120%;\n"
                                                       "}")

    def connectToAnalyzer(self, port="COM5"):
        """Обработчик нажатия на кнопку Подключить/Отключить"""
        if port.find("(") > 0:
            port = port[port.find("(") + 1:port.find(")")]

        allPorts = []
        portsCount = self.devices_comboBox.count()
        buttonStartState = self.connect_pushButton.text()
        if buttonStartState == "Подключить устройство":
            for i in range(portsCount):
                if len(self.devices_comboBox.itemText(i)) >= 1:
                    newPort = self.devices_comboBox.itemText(i)[
                              self.devices_comboBox.itemText(i).find("(") + 1:self.devices_comboBox.itemText(i).find(
                                  ")")]
                    allPorts.append(newPort)
            if port in allPorts:

                self.connectUSB(port)
                print("connectUSB done")
                jsonAnswer = ""

                if self.serialAnalyzer.is_open:
                    jsonAnswer = self.sendJson(make_connection_request())
                    print("sendJson done")
                    # print(jsonAnswer)
                ##ЗАГЛУШКА
                if port == "COM5":
                    jsonAnswer = "{\"status\":1}"
                if str(jsonAnswer) == "Устройство не отвечает":
                    self.statusMessage = "Устройство не отвечает"
                    self.connect_statusLabel.setText(self.statusMessage)
                    self.connect_statusLabel.setStyleSheet("#connect_statusLabel{\n"
                                                           "min-height:14px;\n"
                                                           "max-height:14px;\n"
                                                           "height:14px;\n"
                                                           "padding-left:13px;\n"
                                                           "color: #EB3333;\n"
                                                           "font-family: \'Segoe UI\';\n"
                                                           "font-style: normal;\n"
                                                           "font-weight: 400;\n"
                                                           "font-size: 12px;\n"
                                                           "line-height: 120%;\n"
                                                           "}")
                    if self.serialAnalyzer.is_open:
                        self.serialAnalyzer.close()
                if str(jsonAnswer).find("{") >= 0:

                    answer = json.loads(jsonAnswer)

                    if (answer.get("status") == 1):  ##Make checking
                        self.authWindowActivate()
            else:

                self.statusMessage = "Не удается подключиться к устройству"
                self.connect_statusLabel.setText(self.statusMessage)
                self.connect_statusLabel.setStyleSheet("#connect_statusLabel{\n"
                                                       "min-height:14px;\n"
                                                       "max-height:14px;\n"
                                                       "height:14px;\n"
                                                       "padding-left:13px;\n"
                                                       "color: #EB3333;\n"
                                                       "font-family: \'Segoe UI\';\n"
                                                       "font-style: normal;\n"
                                                       "font-weight: 400;\n"
                                                       "font-size: 12px;\n"
                                                       "line-height: 120%;\n"
                                                       "}")

    def authWindowActivate(self):
        """Активирует окно авторизации"""
        self.AuthWindow = QtWidgets.QMainWindow()
        self.uiAuth = Ui_AuthWindow()
        self.uiAuth.setupUi(self.AuthWindow)
        self.AuthWindow.show()
        self.uiAuth.signin_pushButton.clicked.connect(lambda: self.authorization())
        self.uiAuth.eyeBtn.clicked.connect(lambda: self.eyeBtnHandler())
        self.uiAuth.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        try:
            ConnectWindow.close()
        except:
            pass

    def eyeBtnHandler(self):
        """Обработчик нажатий на кнопку скрытия пароля"""
        if (self.echoMode):
            self.uiAuth.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
            self.uiAuth.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.echoMode = not self.echoMode

    def make_auth_request(self):
        """Формирует запрос контроллеру с данными для авторизации"""
        log = str(self.uiAuth.name_comboBox.currentText())
        pas = str(self.uiAuth.password_lineEdit.text())
        message = {"cmd": "auth", "login": log, "password": pas}
        return json.dumps(message)

    def authorization(self):
        """Обработчик нажатия на кнопку Войти"""

        print(self.make_auth_request())
        self.serialAnalyzer.flush()
        self.sendJsonNoAnswer(self.make_auth_request())
        """ ЗАГЛУШКА
        if ((self.uiAuth.name_comboBox.currentText() == "Analyst") or (
                self.uiAuth.name_comboBox.currentText() == "Lab Manager" and self.uiAuth.password_lineEdit.text() == "123")):
            jsonAnswer = "{\"status\":1}"
        else:
            jsonAnswer = "{\"status\":0}"
        """
        time.sleep(0.5)
        jsonAnswer = self.serialAnalyzer.readline()
        jsonAnswer = self.serialAnalyzer.readline()

        print(str(jsonAnswer))
        if str(jsonAnswer).find("{") >= 0:
            answer = json.loads(jsonAnswer)
            if answer.get("status") == 1:
                self.username = self.uiAuth.name_comboBox.currentText()
                if (not updateDevicesThread.is_alive()):
                    updateDevicesThread.start()
                self.exitFlag = True
                self.workWindowActivate()
                self.isUpdatable = True

            if answer.get("status") == 0:
                self.statusMessage = "Неверно имя пользователя и/или пароль"
            if answer.get("status") == -1:
                self.statusMessage = "Неизвестная ошибка"
            if answer.get("status") == 0 or answer.get("status") == -1:
                self.uiAuth.signin_statusLabel.setText(self.statusMessage)
                self.uiAuth.signin_statusLabel.setStyleSheet("#signin_statusLabel{\n"
                                                             "min-height:14px;\n"
                                                             "max-height:14px;\n"
                                                             "height:14px;\n"
                                                             "padding-left:13px;\n"
                                                             "color: #EB3333;\n"
                                                             "font-family: \'Segoe UI\';\n"
                                                             "font-style: normal;\n"
                                                             "font-weight: 400;\n"
                                                             "font-size: 12px;\n"
                                                             "line-height: 120%;\n"
                                                             "}")

    def add_functions(self):
        """Добавленные действия и обработчики элементов интерфейса к интерфейсу приложения. По сути, формирование логики работы"""
        self.updatePortList()
        self.updateDevices_pushButton.clicked.connect(lambda: self.updatePortList())
        self.connect_pushButton.clicked.connect(lambda: self.connectToAnalyzer(self.devices_comboBox.currentText()))

    def updateDevicesStatus(self):
        """Метод обновляющий цветовую индикацию блока Статус устройств"""
        if self.serialAnalyzer.is_open:
            self.sendJsonNoAnswer(make_updateDevicesStatusJson())
            time.sleep(0.1)

            """
                Формат входящих json 
                {"device":"Controller", "color":"red"}
                {"finish":"finish"}
                Возможные "device" : Controller, CLMeter, cellTemp, outerTemp, innerTemp, sampler
                Возможные "color" : red, blue, yellow, green
                """
            while True:
                time.sleep(0.02)

                answerJson = self.serialAnalyzer.readline()

                ##ЗАГЛУШКА
                ##answerJson = input()

                if str(answerJson).find("}") >= 0 and str(answerJson).find("{") >= 0:
                    print(answerJson)
                    try:
                        answer = json.loads(answerJson)
                    except ValueError as e:
                        answer = json.loads("{\"error\":\"error\"}")

                    if answer.get("finish") == "finish":
                        break
                    if answer.get("device") != -1:
                        deviceName = answer.get("device")
                        color = str("\n""background-color:#EB5757;\n""border-radius: 5px;")
                        if answer.get("color") != -1:
                            color = "\nbackground-color: rgb(" + str(
                                getRGBFromText(answer.get("color"))) + ");\nborder-radius: 5px;"
                        if deviceName == "Controller":
                            self.ui.ControllerIndicator_label.setStyleSheet(color)
                        if deviceName == "CLMeter":
                            self.ui.CLMeterIndicator_label.setStyleSheet(color)
                        if deviceName == "cellTemp":
                            self.ui.cellTempIndicator_label.setStyleSheet(color)
                        if deviceName == "outerTemp":
                            self.ui.outerTempIndicator_label.setStyleSheet(color)
                        if deviceName == "innerTemp":
                            self.ui.innerTempIndicator_label.setStyleSheet(color)
                        if deviceName == "sampler":
                            self.ui.samplerIndicator_label.setStyleSheet(color)
        else:
            self.statusMessage = "Устройство отключено"

    def updateDevicesData(self):
        """Метод, обновляющий текущие данные устройств блока Статус устройств"""
        if self.serialAnalyzer.is_open:
            self.sendJsonNoAnswer(make_updateDevicesDataJson())
            time.sleep(0.1)

            """
                Формат входящих json 
                {"device":"Controller", "value": "Готов к работе"}
                {"device":"outerTemp", "value": "40/1000"}
                {"finish":"finish"}
                Возможные "device" : Controller, CLMeter, cellTemp, outerTemp, innerTemp, sampler
                Возможные "value" : любая строка до 20 символов
                """
            while True:
                time.sleep(0.02)

                answerJson = self.serialAnalyzer.readline()

                ##ЗАГЛУШКА
                # answerJson = input()

                if str(answerJson).find("}") >= 0 and str(answerJson).find("{") >= 0:
                    print(answerJson)
                    try:
                        answer = json.loads(answerJson)
                    except ValueError as e:
                        answer = json.loads("{\"error\":\"error\"}")

                    if answer.get("finish") == "finish":
                        break
                    if answer.get("device") != -1:
                        deviceName = answer.get("device")
                        value = "н/д"
                        if answer.get("value") != -1:
                            value = str(answer.get("value"))
                        if deviceName == "Controller":
                            self.ui.Controller_label.setToolTip("Готовность контроллера: " + str(value))
                            self.ui.Controller_label.setStatusTip("Готовность контроллера: " + str(value))
                            self.ui.ControllerIndicator_label.setToolTip("Готовность контроллера: " + str(value))
                            self.ui.ControllerIndicator_label.setStatusTip("Готовность контроллера: " + str(value))
                        if deviceName == "CLMeter":
                            self.ui.CLMeter_label.setToolTip("Готовность кулонометра: " + str(value))
                            self.ui.CLMeter_label.setStatusTip("Готовность кулонометра: " + str(value))
                            self.ui.CLMeterIndicator_label.setToolTip("Готовность кулонометра: " + str(value))
                            self.ui.CLMeterIndicator_label.setStatusTip("Готовность кулонометра: " + str(value))
                        if deviceName == "cellTemp":
                            self.ui.cellTemp_label.setToolTip("Температура ячейки: " + str(value) + "°C")
                            self.ui.cellTemp_label.setStatusTip("Температура ячейки: " + str(value) + "°C")
                            self.ui.cellTempIndicator_label.setToolTip("Температура ячейки: " + str(value) + "°C")
                            self.ui.cellTempIndicator_label.setStatusTip("Температура ячейки: " + str(value) + "°C")
                        if deviceName == "outerTemp":
                            self.ui.outerTemp_label.setToolTip("Температура внешней трубки: " + str(value) + "°C")
                            self.ui.outerTemp_label.setStatusTip("Температура внешней трубки: " + str(value) + "°C")
                            self.ui.outerTempIndicator_label.setToolTip(
                                "Температура внешней трубки: " + str(value) + "°C")
                            self.ui.outerTempIndicator_label.setStatusTip(
                                "Температура внешней трубки: " + str(value) + "°C")
                        if deviceName == "innerTemp":
                            self.ui.innerTemp_label.setToolTip("Температура внутренней трубки: " + str(value) + "°C")
                            self.ui.innerTemp_label.setStatusTip("Температура внутренней трубки: " + str(value) + "°C")
                            self.ui.innerTempIndicator_label.setToolTip(
                                "Температура внутренней трубки: " + str(value) + "°C")
                            self.ui.innerTempIndicator_label.setStatusTip(
                                "Температура внутренней трубки: " + str(value) + "°C")
                        if deviceName == "sampler":
                            self.ui.sampler_label.setToolTip("Готовность устройства ввода: " + str(value))
                            self.ui.sampler_label.setStatusTip("Готовность устройства ввода: " + str(value))
                            self.ui.samplerIndicator_label.setToolTip("Готовность устройства ввода: " + str(value))
                            self.ui.samplerIndicator_label.setStatusTip("Готовность устройства ввода: " + str(value))
        else:
            self.statusMessage = "Устройство отключено"

    def devicesUpd_thread(self):
        """Метод, определяющий порядок выполнения обновлений блока Статус устройств.
        Выполняется в отдельном потоке"""
        self.plotData = {"x": [], "y": []}  # {"x": [1, 2, 3, 4, 5, 6], "y": [1, 3, 2, 4, 3, 1]}
        try:
            while True:
                if self.isUpdatable:
                    self.isUpdates = True
                    self.updateDevicesStatus()
                    self.updateDevicesData()
                    self.updatePlotData()
                    self.updatePlot()
                    print(self.plotData)
                self.isUpdates = False
                time.sleep(0.5)
                print("updTime")
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print('EXCEPTION statusUpd thread ' + str(e))

    def updatePlotData(self):
        """Метод, обновляющий текущие данные графика"""
        if self.serialAnalyzer.is_open:
            self.sendJsonNoAnswer(make_updatePlotDataJson())
            time.sleep(0.02)

            """
                Формат входящих json 
                {"time":0.1, "value": 1}
                {"time":0.2, "value": 2}
                {"time":0.3, "value": 1}
                {"time":0.4, "value": 3}
                {"time":0.5, "value": 2}
                {"finish":"finish"}
                """
            # self.plotData["x"] = []
            # self.plotData["y"] = []
            while True:
                time.sleep(0.04)

                answerJson = self.serialAnalyzer.readline()

                ##ЗАГЛУШКА
                # answerJson = input()

                if str(answerJson).find("}") >= 0 and str(answerJson).find("{") >= 0:
                    print(answerJson)
                    try:
                        answer = json.loads(answerJson)
                    except ValueError as e:
                        answer = json.loads("{\"error\":\"error\"}")

                    if answer.get("finish") == "finish":
                        break
                    if answer.get("time") != -1 and answer.get("value") != -1:
                        value = answer.get("value")
                        timeVal = answer.get("time")
                        if (timeVal is not None and value is not None):
                            self.plotData["x"].append(float(timeVal))
                            self.plotData["y"].append(float(value))

        else:
            self.statusMessage = "Устройство отключено"

    def updatePlot(self):
        """Обновляет график по имеющимся данным"""
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.plotData["x"], self.plotData["y"])
        self.ui.MplWidget.canvas.axes.legend(('time', 'value'), loc='upper right')
        self.ui.MplWidget.canvas.axes.set_title('value of time')
        self.ui.MplWidget.canvas.draw()

    def workWindowActivate(self):
        """Активирует рабочее окно"""
        self.WorkWindow = QtWidgets.QMainWindow()
        self.ui = Ui_WorkWindow()
        self.ui.setupUi(self.WorkWindow)
        self.WorkWindow.show()
        self.AuthWindow.close()
        self.taskStartStopFlag = True

        self.ui.StartBtn.clicked.connect(lambda: self.startBtnHandler())
        self.ui.SysMethBtn.clicked.connect(lambda: self.sysMethBtnHandler())
        self.ui.CreSampBtn.clicked.connect(lambda: self.creSampBtnHandler())
        self.ui.tableWidget.clicked.connect(lambda: self.updDescription())
        self.ui.tableWidget_hist.doubleClicked.connect(lambda: self.showResult())
        self.ui.exit_pushButton.clicked.connect(lambda: self.exit_pushButtonHandler())
        self.ui.user_label.setText(self.username)
        print(self.username)
        self.header = self.ui.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.header.setDefaultAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ui.tableWidget.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.header.setFixedHeight(58)

        self.header_hist = self.ui.tableWidget_hist.horizontalHeader()
        self.header_hist.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.header_hist.setDefaultAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.header_hist.setFixedHeight(58)


        self.ui.tableWidget.setColumnWidth(0, 355)
        self.ui.tableWidget.setColumnWidth(1, 164)
        self.ui.tableWidget.setColumnWidth(2, 164)
        self.ui.tableWidget.setColumnWidth(3, 204)
        self.ui.tableWidget.setColumnWidth(4, 204)
        self.ui.tableWidget.setColumnWidth(5, 204)
        self.ui.tableWidget.setColumnWidth(6, 84)
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor('#E7E7E7'))
        self.palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor('black'))
        self.ui.tableWidget.setPalette(self.palette)

        self.ui.tableWidget_hist.setColumnWidth(0, 76)
        self.ui.tableWidget_hist.setColumnWidth(1, 164)
        self.ui.tableWidget_hist.setColumnWidth(2, 454)
        self.ui.tableWidget_hist.setColumnWidth(3, 237)
        self.ui.tableWidget_hist.setColumnWidth(4, 237)
        self.ui.tableWidget_hist.setColumnWidth(5, 210)
        self.ui.tableWidget_hist.setPalette(self.palette)



    def creSampBtnHandler(self):
        """Обработчик кнопки создания группы образцов"""
        self.creSampWindow = QtWidgets.QDialog()
        self.WorkWindow.setEnabled(False)

        self.uiSamp = Ui_creSampWindow()
        self.uiSamp.setupUi(self.creSampWindow)
        self.creSampWindow.show()
        self.uiSamp.addSampButton.clicked.connect(lambda: self.addSampBtnHandler())
        self.uiSamp.autosampler_rButton.clicked.connect(lambda: self.updSampSettings())

        self.uiSamp.cancelSampButton.clicked.connect(lambda: self.cancelSampBtnHandler())

    def updSampSettings(self):
        """Определяет активность параметров автосемплера"""
        flag = self.uiSamp.autosampler_rButton.isChecked()

        self.uiSamp.sampleNum_spinBox.setEnabled(flag)
        self.uiSamp.repeatSampleNum_spinBox_2.setEnabled(flag)
        self.uiSamp.pos_comboBox_2.setEnabled(flag)
        self.uiSamp.pos_spinBox_2.setEnabled(flag)
        self.uiSamp.razbav_lineEdit_2.setEnabled(flag)
        self.uiSamp.plotn_lineEdit_2.setEnabled(flag)

    def addTask(self, task):
        """Добавляет задачу в диспетчер задач"""
        color1 = "rgba(0, 32, 51, 0.6)"
        if (task.status == "Выполнено"):
            color1 = "rgba(34, 195, 142, 1)"
        if (task.status == "В процессе"):
            color1 = "rgba(0, 120, 210, 1)"
        if (task.status == "Прервано"):
            color1 = "rgba(235, 87, 87, 1)"
        style1 = str("margin:12px;" + "padding:6px;" + "border:1px solid " + color1 + ";" +
                     "color:" + color1 + ";" + "border-radius:8px;" + "background:transparent;" +
                     "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                     "font-weight: 400;" + "font-size: 16px;" + "line-height: 150%;")

        label1 = QtWidgets.QLabel()
        label1.setText(str(task.status))
        label1.setStyleSheet(style1)

        label1.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setCellWidget(task.position, 1, label1)
        descriptionPrefix = ""
        if type(task) is sysMethTask:
            descriptionPrefix = ""
        if type(task) is sampleTask:
            descriptionPrefix = ""
        self.ui.tableWidget.setRowHeight(task.position, 58)

        style0 = str("margin:12px;" + "background:transparent;" +
                     "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                     "font-weight: 400;" + "font-size: 14px;" + "line-height: 150%;")

        label0 = QtWidgets.QLabel()
        label0.setText(str(task.description))
        label0.setStyleSheet(style0)

        label0.setAlignment(QtCore.Qt.AlignLeft)
        label0.setAlignment(QtCore.Qt.AlignVCenter)
        self.ui.tableWidget.setCellWidget(task.position, 0, label0)

        style2 = str("margin:12px;" + "background:transparent;" +
                     "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                     "font-weight: 400;" + "font-size: 14px;" + "line-height: 150%;")

        label2 = QtWidgets.QLabel()
        label2.setText(str(task.creationDate.strftime("%d.%m.%Y %H:%M:%S")))
        label2.setStyleSheet(style2)

        label2.setAlignment(QtCore.Qt.AlignLeft)
        label2.setAlignment(QtCore.Qt.AlignVCenter)
        label2.setWordWrap(True)
        self.ui.tableWidget.setCellWidget(task.position, 2, label2)

        self.ui.tableWidget.setItem(task.position, 3,
                                    QtWidgets.QTableWidgetItem(str(task.startDate)))
        self.ui.tableWidget.setItem(task.position, 4,
                                    QtWidgets.QTableWidgetItem(str(task.stopDate)))
        self.ui.tableWidget.setItem(task.position, 5,
                                    QtWidgets.QTableWidgetItem(str(task.totalTime)))
        self.ui.BinBtn = QtWidgets.QLabel(self.ui.tableWidget)
        self.ui.BinBtn.setMinimumSize(QtCore.QSize(32, 32))
        self.ui.BinBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.ui.BinBtn.setStyleSheet("QLabel{"
                                     "image: url(:/imgs/BinBtnIcon.png);"
                                     "min-width:32px;"
                                     "max-width:32px;"
                                     "min-height:32px;"
                                     "max-height:32px;"
                                     "box-sizing: border-box;\n"
                                     "\n"
                                     "alignment: center;\n"
                                     "\n"
                                     "/* control-default/bg */\n"
                                     "\n"
                                     "background: transparent;\n"
                                     "/* control-default/typo-placeholder */\n"
                                     "\n"
                                     "border: 1px solid rgba(0, 32, 51, 0.35);\n"
                                     "border-radius: 4px;"
                                     "}"
                                     "QLabel::hover{"
                                     "border: 1px dashed rgba(0, 50, 80, 0.50);\n"
                                     "}"
                                     "QLabel::pressed{"
                                     "border: 2px solid rgba(0, 50, 80, 0.35);\n"
                                     "}"
                                     )
        self.ui.BinBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/BinBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.BinBtn.setObjectName("BinBtn" + str(task.position))
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QHBoxLayout(self.widget)
        self.layout.addWidget(self.ui.BinBtn)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setStyleSheet("margin-right:12px;"
                                  "margin-left:12px;"
                                  "background:transparent;")
        self.ui.tableWidget.setCellWidget(task.position, 6, self.widget)
        self.taskTable.append(task)
        self.ui.tableWidget.setRowCount(len(self.taskTable) + 1)
        self.ui.tableWidget.setRowHeight(task.position + 1, 58)

    def addSampBtnHandler(self):
        """Обработчк кнопки добавления новой группы образцов"""

        newCreSampTask = sampleTask(str(self.uiSamp.groupName_lineEdit.text()),
                                    len(self.taskTable),
                                    str(self.uiSamp.expType_comboBox.currentText()),
                                    str(self.uiSamp.sampleName_lineEdit_2.text()),
                                    str(self.uiSamp.value_lineEdit_2.text()),
                                    str(""),
                                    str(self.uiSamp.razmConcentr_comboBox_2.currentText()),
                                    str(self.uiSamp.operator_lineEdit_2.text()),
                                    str(self.uiSamp.comment_plainTextEdit_2.toPlainText()),
                                    autosamplerEnable=self.uiSamp.autosampler_rButton.isChecked(),
                                    sampleNum=str(self.uiSamp.sampleNum_spinBox.value()),
                                    repeatSampleNum=str(self.uiSamp.repeatSampleNum_spinBox_2.value()),
                                    posTray=str(self.uiSamp.pos_comboBox_2.currentText()),
                                    posTube=str(self.uiSamp.pos_spinBox_2.value()),
                                    razbav=str(self.uiSamp.razbav_lineEdit_2.text()),
                                    plotn=str(self.uiSamp.plotn_lineEdit_2.text()))
        self.WorkWindow.setEnabled(True)
        self.addTask(newCreSampTask)
        self.creSampWindow.close()

    def cancelSampBtnHandler(self):
        """Обработчик кнопки отмены добавления группы образцов"""
        self.WorkWindow.setEnabled(True)
        self.creSampWindow.close()

    def binBtnHandler(self, pos):
        """Обработчик нажатий любой из кнопок корзины диспетчера задач"""
        if -1 < pos < len(self.taskTable):
            self.ui.tableWidget.removeRow(pos)
            self.updateTaskTable(pos)

    def exit_pushButtonHandler(self):
        """Обработчик нажатий на кнопку выхода из профиля"""
        self.selectedRow = -1
        self.taskTable = []
        self.exitFlag = False
        self.isUpdatable = False
        time.sleep(1)
        self.WorkWindow.close()
        self.authWindowActivate()

    def updDescription(self):
        """Обновляет описание в нижнем поле диспетчера задач по выбранной задаче"""
        pos = self.ui.tableWidget.currentRow()
        if(self.ui.tableWidget.currentColumn()==6):
            self.binBtnHandler(pos)
        else:
            if -1 < pos < len(self.taskTable):
                if type(self.taskTable[pos]) is sysMethTask:
                    self.ui.descriptin_label.setText("Параметры. T(внут): " + str(self.taskTable[pos].innerTemp) +
                                                     "; T(внеш): " + str(self.taskTable[pos].outerTemp) +
                                                     "; T(мешалки): " + str(self.taskTable[pos].shakerTemp) +
                                                     "; V: " + str(self.taskTable[pos].injectionSpeed) +
                                                     "; T(трансп): " + str(self.taskTable[pos].transpLineTemp))
                if type(self.taskTable[pos]) is sampleTask:
                    descripMessage = str(
                        "Имя группы: " + str(self.taskTable[pos].description) + "; Тип: " + str(self.taskTable[pos].expType)
                        + "\nИмя пробы: " + str(self.taskTable[pos].sampleName)
                        + "; Количество: " + str(self.taskTable[pos].value) + " " + str(self.taskTable[pos].valueRazm)
                        + "; Размерность концентрации: " + str(self.taskTable[pos].razmConcentr)
                        + "\nОператор: " + str(self.taskTable[pos].operator)
                        + "\nКомментарий: " + str(self.taskTable[pos].comment)
                        + "\nАвтосемплер: " + str(self.taskTable[pos].autosamplerEnable))
                    # print(descripMessage)
                    if (self.taskTable[pos].autosamplerEnable):
                        descripMessage = descripMessage + str(
                            "; Число образцов: " + str(self.taskTable[pos].sampleNum)
                            + "; Количество повторов: " + str(self.taskTable[pos].repeatSampleNum)
                            + "; Первая позиция: " + str(self.taskTable[pos].posTray)
                            + ", ячейка: " + str(self.taskTable[pos].posTube)
                            + "; Разбавление: " + str(self.taskTable[pos].razbav)
                            + "; Плотность: " + str(self.taskTable[pos].plotn)
                        )
                    self.ui.descriptin_label.setText(descripMessage)



            else:
                self.ui.descriptin_label.clear()
            # self.ui.descriptin_label.wordWrap()
            # self.ui.descriptin_label.adjustSize()

    def updateTaskTable(self, pos):
        """Обновляет массив задач (убирает пустые строки)"""
        for index, item in enumerate(self.taskTable):
            if pos < index:
                self.taskTable[index].position -= 1
        self.taskTable.pop(pos)

    def make_setMode_request(self, task):
        """Формирует JSON-запрос установки режима"""
        messageList = []
        mode = str(task.description)
        innerTemp = str(task.innerTemp)
        outerTemp = str(task.outerTemp)
        shakerTemp = str(task.shakerTemp)
        injectionSpeed = str(task.injectionSpeed)
        transpLineTemp = str(task.transpLineTemp)
        messageList.append({"cmd": "start"})
        messageList.append({"mode": mode})
        messageList.append({"innerTemp": innerTemp})
        messageList.append({"outerTemp": outerTemp})
        messageList.append({"shakerTemp": shakerTemp})
        messageList.append({"injectionSpeed": injectionSpeed})
        messageList.append({"transpLineTemp": transpLineTemp})
        return messageList

    def make_startSamp_request(self, task):
        """Формирует JSON-запрос запуска эксперимента"""
        messageList = []
        mode = str(task.description)
        value = str(task.value)
        valueRazm = str(task.valueRazm)
        razmConcentr = str(task.razmConcentr)
        autosamplerEnable = str(task.autosamplerEnable)
        sampleNum = str(task.sampleNum)
        repeatSampleNum = str(task.repeatSampleNum)
        posTray = str(task.posTray)
        posTube = str(task.posTube)
        razbav = str(task.razbav)
        plotn = str(task.plotn)

        messageList.append({"cmd": "start"})
        messageList.append({"mode": mode})
        messageList.append({"value": value})
        # messageList.append({"valueRazm": valueRazm})
        messageList.append({"razmConcentr": razmConcentr})
        messageList.append({"autosamplerEnable": autosamplerEnable})
        if (autosamplerEnable):
            messageList.append({"sampleNum": sampleNum})
            messageList.append({"repeatSampleNum": repeatSampleNum})
            messageList.append({"posTray": posTray})
            messageList.append({"posTube": posTube})
            messageList.append({"razbav": razbav})
            messageList.append({"plotn": plotn})

        return messageList

    def startBtnHandler(self):
        """Обработчик конпки запуска задачи"""
        self.ui.StartBtn.setEnabled(False)
        if self.taskStartStopFlag:
            try:
                pos = self.ui.tableWidget.currentRow()
                if pos >= 0:  # добавить проверку на павильность задачи когда уточнятся диапазоны данных
                    task = self.taskTable[pos]
                    messageList = []
                    """Формирует запрос контроллеру с параметрами задачи"""
                    if type(task) is sysMethTask:
                        messageList = self.make_setMode_request(task)
                    if type(task) is sampleTask:
                        messageList = self.make_startSamp_request(task)
                    flagAutosampler = True
                    messageList.append({"cmd": "finish"})
                    self.isUpdatable = False
                    time.sleep(0.5)
                    for index, message in enumerate(messageList):
                        jsonAnswer = ""
                        answer = None
                        if message.get("autosamplerEnable") == "False":
                            flagAutosampler = False
                        messageStr = json.dumps(message, ensure_ascii=False)
                        if flagAutosampler or message.get("cmd") == "finish":
                            self.sendJsonNoAnswer(str(messageStr))
                            time.sleep(0.2)
                            jsonAnswer = self.serialAnalyzer.readline()
                            time.sleep(0.1)
                        if str(jsonAnswer).find("}") >= 0 and str(jsonAnswer).find("{") >= 0:
                            try:
                                answer = json.loads(jsonAnswer)
                            except ValueError as e:
                                answer = json.loads("{\"error\":\"error\"}")
                        if (answer is not None and answer.get("status") == "1") or True:
                            print("status1")
                        else:
                            self.stopBtnHandler()
                            self.isUpdatable = True
                            break
                    time.sleep(0.3)
                    self.isUpdatable = True
                    if str(self.ui.tableWidget.cellWidget(pos, 1).text()) in ["Ожидание", "Прервано"]:
                        self.ui.tableWidget.cellWidget(pos, 1).setText("В процессе")
                        color1 = "rgba(0, 120, 210, 1)"
                        style1 = str("margin:12px;" + "padding:6px;" + "border:1px solid " + color1 + ";" +
                                     "color:" + color1 + ";" + "border-radius:8px;" + "background:transparent;" +
                                     "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                                     "font-weight: 400;" + "font-size: 16px;" + "line-height: 150%;")

                        self.ui.tableWidget.cellWidget(pos, 1).setStyleSheet(style1)

                        style3 = str("margin:12px;" + "background:transparent;" +
                                     "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                                     "font-weight: 400;" + "font-size: 14px;" + "line-height: 150%;")

                        label3 = QtWidgets.QLabel()
                        self.taskTable[pos].startDate=datetime.datetime.now()
                        label3.setText(str(self.taskTable[pos].startDate.strftime("%d.%m.%Y %H:%M:%S")))
                        label3.setStyleSheet(style3)

                        label3.setAlignment(QtCore.Qt.AlignLeft)
                        label3.setAlignment(QtCore.Qt.AlignVCenter)
                        label3.setWordWrap(True)
                        self.ui.tableWidget.setCellWidget(task.position, 3, label3)

                        self.ui.tableWidget.setItem(pos, 4, QtWidgets.QTableWidgetItem(str("")))
                        self.ui.tableWidget.setItem(pos, 5, QtWidgets.QTableWidgetItem(str("")))
                    self.isUpdatable = True
                    self.taskStartStopFlag = False

                    self.ui.StartBtn.setStyleSheet("#StartBtn{\n"
                                                   "box-sizing: border-box;\n"
                                                   "\n"
                                                   "align: top;\n"
                                                   "\n"
                                                   "/* control-default/bg */\n"
                                                   "\n"
                                                   "background: #FFFFFF;\n"
                                                   "/* control-default/typo-placeholder */\n"
                                                   "\n"
                                                   "border: 1px solid rgba(235, 51, 51, 1);\n"
                                                   "\n"
                                                   "border-radius: 4px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "#StartBtn::hover {\n"
                                                   "border: 1px solid rgba(235, 51, 51, 0.3);\n"
                                                   "\n"
                                                   "}\n"
                                                   "\n"
                                                   "#StartBtn::pressed {\n"
                                                   "border: 2px solid rgba(235, 51, 51, 1);\n"
                                                   "}")
                    self.ui.StartBtn.setText("")
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/imgs/StopBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.StartBtn.setIcon(icon)
                    self.ui.StartBtn.setIconSize(QtCore.QSize(20, 20))

                    if type(task) is sysMethTask:
                        self.stopBtnHandler()
            except Exception as e:
                print(e)
                # self.taskStartStopFlag = False
        else:
            self.stopBtnHandler()
            self.taskStartStopFlag = True
        self.ui.StartBtn.setEnabled(True)

    def stopBtnHandler(self):
        """Обработчик кнопки остановки задачи"""
        self.isUpdatable = True
        self.ui.StartBtn.setEnabled(False)
        try:
            pos = self.ui.tableWidget.currentRow()
            if pos >= 0 and str(self.ui.tableWidget.cellWidget(pos, 1).text()) == "В процессе":

                self.ui.tableWidget.cellWidget(pos, 1).setText("Прервано")

                style4 = str("margin:12px;" + "background:transparent;" +
                             "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                             "font-weight: 400;" + "font-size: 14px;" + "line-height: 150%;")

                label4 = QtWidgets.QLabel()
                self.taskTable[pos].stopDate = datetime.datetime.now()
                label4.setText(self.taskTable[pos].stopDate.strftime("%d.%m.%Y %H:%M:%S"))
                label4.setStyleSheet(style4)

                label4.setAlignment(QtCore.Qt.AlignLeft)
                label4.setAlignment(QtCore.Qt.AlignVCenter)
                label4.setWordWrap(True)
                self.ui.tableWidget.setCellWidget(pos, 4, label4)


                self.taskTable[pos].totalTime = self.taskTable[pos].stopDate - self.taskTable[pos].startDate
                total_seconds = self.taskTable[pos].totalTime.total_seconds()
                hours, remainder = divmod(total_seconds,3600)
                minutes, seconds = divmod(remainder, 60)
                formatted_delta = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
                label5 = QtWidgets.QLabel()
                label5.setText(str(formatted_delta))
                label5.setStyleSheet(style4)

                label5.setAlignment(QtCore.Qt.AlignLeft)
                label5.setAlignment(QtCore.Qt.AlignVCenter)
                label5.setWordWrap(True)
                self.ui.tableWidget.setCellWidget(pos, 5, label5)

                color1 = "rgba(235, 87, 87, 1)"
                if (type(self.taskTable[pos]) is sysMethTask):
                    self.ui.tableWidget.cellWidget(pos, 1).setText("Выполнено")
                    color1 = "rgba(34, 195, 142, 1)"
                style1 = str("margin:12px;" + "padding:6px;" + "border:1px solid " + color1 + ";" +
                             "color:" + color1 + ";" + "border-radius:8px;" + "background:transparent;" +
                             "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                             "font-weight: 400;" + "font-size: 16px;" + "line-height: 150%;")
                self.ui.tableWidget.cellWidget(pos, 1).setStyleSheet(style1)
                if (type(self.taskTable[pos]) is sampleTask):

                    self.ui.tableWidget_hist.setRowCount(self.ui.tableWidget_hist.rowCount() + 1)
                    style0h = str("margin:12px;" + "background:transparent;" +
                                 "text-align:center;" + "font-family: \"Inter\";" + "font-style: normal;" +
                                 "font-weight: 400;" + "font-size: 14px;" + "line-height: 150%;")

                    label0h = QtWidgets.QLabel()
                    label0h.setText(str(self.ui.tableWidget_hist.rowCount()-1))
                    label0h.setStyleSheet(style0h)

                    label0h.setAlignment(QtCore.Qt.AlignLeft)
                    label0h.setAlignment(QtCore.Qt.AlignVCenter)
                    label0h.setWordWrap(True)
                    self.ui.tableWidget_hist.setCellWidget(self.ui.tableWidget_hist.rowCount() - 1, 0, label0h)



                    label1h = QtWidgets.QLabel()
                    label1h.setText(str(self.taskTable[pos].stopDate.strftime("%d.%m.%Y %H:%M:%S")))
                    label1h.setStyleSheet(style0h)

                    label1h.setAlignment(QtCore.Qt.AlignLeft)
                    label1h.setAlignment(QtCore.Qt.AlignVCenter)
                    label1h.setWordWrap(True)
                    self.ui.tableWidget_hist.setCellWidget(self.ui.tableWidget_hist.rowCount() - 1, 1, label1h)

                    label2h = QtWidgets.QLabel()
                    label2h.setText(str(self.taskTable[pos].description))
                    label2h.setStyleSheet(style0h)

                    label2h.setAlignment(QtCore.Qt.AlignLeft)
                    label2h.setAlignment(QtCore.Qt.AlignVCenter)
                    label2h.setWordWrap(True)
                    self.ui.tableWidget_hist.setCellWidget(self.ui.tableWidget_hist.rowCount() - 1, 2, label2h)

                    total_seconds = self.taskTable[pos].totalTime.total_seconds()
                    hours, remainder = divmod(total_seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    formatted_delta = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

                    label5h = QtWidgets.QLabel()
                    label5h.setText(str(formatted_delta))
                    label5h.setStyleSheet(style0h)

                    label5h.setAlignment(QtCore.Qt.AlignLeft)
                    label5h.setAlignment(QtCore.Qt.AlignVCenter)
                    label5h.setWordWrap(True)
                    self.ui.tableWidget_hist.setCellWidget(self.ui.tableWidget_hist.rowCount() - 1, 5, label5h)



                    self.ui.tableWidget_hist.setRowHeight(self.ui.tableWidget_hist.rowCount()-1, 58)
                    self.isUpdatable = False
                    time.sleep(0.5)
                    self.sendJsonNoAnswer(make_stop_request())
                    time.sleep(0.05)
                    jsonAnswer = ""
                    answer = None
                    jsonAnswer = self.serialAnalyzer.readline()
                    time.sleep(0.5)
                    self.isUpdatable = True
                    if str(jsonAnswer).find("}") >= 0 and str(jsonAnswer).find("{") >= 0:
                        try:
                            answer = json.loads(jsonAnswer)
                        except ValueError as e:
                            answer = json.loads("{\"error\":\"error\"}")
                    if (answer is not None and answer.get("status") == "1") or True:
                        print("status2")
                    else:
                        print("нет ответа")
                self.isUpdatable = True

                self.ui.StartBtn.setStyleSheet("#StartBtn{\n"
                                               "box-sizing: border-box;\n"
                                               "\n"
                                               "align: top;\n"
                                               "\n"
                                               "/* control-default/bg */\n"
                                               "\n"
                                               "background: #FFFFFF;\n"
                                               "/* control-default/typo-placeholder */\n"
                                               "\n"
                                               "border: 1px solid #09B37B;\n"
                                               "\n"
                                               "border-radius: 4px;\n"
                                               "}\n"
                                               "\n"
                                               "#StartBtn::hover {\n"
                                               "border: 1px solid rgb(10, 221, 151);\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "#StartBtn::pressed {\n"
                                               "border: 2px solid #09B37B;\n"
                                               "}")
                self.ui.StartBtn.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/imgs/StartBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ui.StartBtn.setIcon(icon)
                self.ui.StartBtn.setIconSize(QtCore.QSize(20, 20))
                self.taskStartStopFlag = True

        except Exception as e:
            print(e)
        self.ui.StartBtn.setEnabled(True)

    def sysMethBtnHandler(self):
        """Обработчик кнопки установки режима"""
        self.sysMethWindow = QtWidgets.QDialog()
        self.WorkWindow.setEnabled(False)
        self.uiMeth = Ui_sysMethWindow()
        self.uiMeth.setupUi(self.sysMethWindow)
        self.sysMethWindow.show()
        self.uiMeth.Startup_rButton.clicked.connect(lambda: self.setStartupMethTask())
        self.uiMeth.Standby_rButton.clicked.connect(lambda: self.setStandbyMethTask())
        self.uiMeth.Shutdown_rButton.clicked.connect(lambda: self.setShutdownMethTask())

        self.uiMeth.addMethButton.clicked.connect(lambda: self.addMethBtnHandler())
        self.uiMeth.cancelMethButton.clicked.connect(lambda: self.cancelMethBtnHandler())

    def setStartupMethTask(self):
        """Записывает параметры рабочего режима в поля диалогово окна установки режима"""
        self.uiMeth.innerTemp_lineEdit.setText(str(1000))
        self.uiMeth.outerTemp_lineEdit.setText(str(500))
        self.uiMeth.shakerTemp_lineEdit.setText(str(20))
        self.uiMeth.injectionSpeed_lineEdit.setText(str(5))
        self.uiMeth.transpLineTemp_lineEdit.setText(str(200))

    def setStandbyMethTask(self):
        """Записывает параметры режима ожидания в поля диалогово окна установки режима"""
        self.uiMeth.innerTemp_lineEdit.setText(str(800))
        self.uiMeth.outerTemp_lineEdit.setText(str(300))
        self.uiMeth.shakerTemp_lineEdit.setText(str(20))
        self.uiMeth.injectionSpeed_lineEdit.setText(str(0))
        self.uiMeth.transpLineTemp_lineEdit.setText(str(100))

    def setShutdownMethTask(self):
        """Записывает параметры режима остановки в поля диалогово окна установки режима"""
        self.uiMeth.innerTemp_lineEdit.setText(str(20))
        self.uiMeth.outerTemp_lineEdit.setText(str(20))
        self.uiMeth.shakerTemp_lineEdit.setText(str(20))
        self.uiMeth.injectionSpeed_lineEdit.setText(str(0))
        self.uiMeth.transpLineTemp_lineEdit.setText(str(20))

    def addMethBtnHandler(self):
        """Обработчик кнопки добавления режима в диспетчер задач"""
        methType = ""
        if (self.uiMeth.Startup_rButton.isChecked()):
            methType = "Рабочий режим"
        if (self.uiMeth.Standby_rButton.isChecked()):
            methType = "Ожидание"
        if (self.uiMeth.Shutdown_rButton.isChecked()):
            methType = "Отключение"
        newSysMethTask = sysMethTask(str(methType),
                                     len(self.taskTable),
                                     self.uiMeth.innerTemp_lineEdit.text(),
                                     self.uiMeth.outerTemp_lineEdit.text(),
                                     self.uiMeth.shakerTemp_lineEdit.text(),
                                     self.uiMeth.injectionSpeed_lineEdit.text(),
                                     self.uiMeth.transpLineTemp_lineEdit.text())

        self.WorkWindow.setEnabled(True)
        self.addTask(newSysMethTask)
        self.sysMethWindow.close()

    def cancelMethBtnHandler(self):
        """Обработчки кнопки отмены добавления режима"""
        self.WorkWindow.setEnabled(True)
        self.sysMethWindow.close()


if __name__ == "__main__":
    """Запуск приложения"""
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ConnectWindow = QtWidgets.QMainWindow()
    ui = Ui_ConnectWindow()
    ui.setupUi(ConnectWindow)
    ConnectWindow.show()
    updateDevicesThread = threading.Thread(target=ui.devicesUpd_thread)
    updateDevicesThread.daemon = True
    sys.exit(app.exec_())
