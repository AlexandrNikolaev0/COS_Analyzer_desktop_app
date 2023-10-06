# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sysMethWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sysMethWindow(object):
    """Класс диалогового окна установки режима. Сгенерировано в Qt Designer"""
    def setupUi(self, sysMethWindow):
        sysMethWindow.setObjectName("sysMethWindow")
        sysMethWindow.resize(633, 576)
        sysMethWindow.setMinimumSize(QtCore.QSize(633, 576))
        sysMethWindow.setMaximumSize(QtCore.QSize(633, 576))
        sysMethWindow.setStyleSheet("background: #fff;\n"
                                    "border-radius: 8px;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(sysMethWindow)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(32)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_label = QtWidgets.QLabel(sysMethWindow)
        self.header_label.setMinimumSize(QtCore.QSize(0, 30))
        self.header_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.header_label.setStyleSheet("/* XL */\n"
                                        "\n"
                                        "font-family: \'Inter\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "font-size: 20px;\n"
                                        "line-height: 150%;\n"
                                        "\n"
                                        "/* bg/tone */\n"
                                        "\n"
                                        "color: rgba(0, 32, 51, 0.85);\n"
                                        "")
        self.header_label.setObjectName("header_label")
        self.verticalLayout_2.addWidget(self.header_label)
        self.widget = QtWidgets.QWidget(sysMethWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mode_label = QtWidgets.QLabel(self.widget)
        self.mode_label.setMinimumSize(QtCore.QSize(0, 24))
        self.mode_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.mode_label.setStyleSheet("/* M */\n"
                                      "\n"
                                      "font-family: \'Inter\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 16px;\n"
                                      "line-height: 150%;\n"
                                      "\n"
                                      "/* typo/primary */\n"
                                      "\n"
                                      "color: #002033;")
        self.mode_label.setObjectName("mode_label")
        self.verticalLayout_3.addWidget(self.mode_label)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Startup_rButton = QtWidgets.QRadioButton(self.widget_2)
        self.Startup_rButton.setStyleSheet("QRadioButton{\n"
                                           "font-family: \'Segoe UI\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "font-size: 16px;\n"
                                           "line-height: 120%;\n"
                                           "/* or 19px */\n"
                                           "\n"
                                           "spacing: 12px;\n"
                                           "/* control-default/typo */\n"
                                           "\n"
                                           "color: #002033;\n"
                                           "}\n"
                                           "\n"
                                           "QRadioButton::indicator{\n"
                                           "width: 16px;\n"
                                           "height: 16px;\n"
                                           "}\n"
                                           "")
        self.Startup_rButton.setChecked(True)
        self.Startup_rButton.setObjectName("Startup_rButton")
        self.verticalLayout_5.addWidget(self.Startup_rButton)
        self.Standby_rButton = QtWidgets.QRadioButton(self.widget_2)
        self.Standby_rButton.setStyleSheet("QRadioButton{\n"
                                           "font-family: \'Segoe UI\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "font-size: 16px;\n"
                                           "line-height: 120%;\n"
                                           "/* or 19px */\n"
                                           "\n"
                                           "spacing: 12px;\n"
                                           "/* control-default/typo */\n"
                                           "\n"
                                           "color: #002033;\n"
                                           "}\n"
                                           "\n"
                                           "QRadioButton::indicator{\n"
                                           "width: 16px;\n"
                                           "height: 16px;\n"
                                           "}\n"
                                           "")
        self.Standby_rButton.setObjectName("Standby_rButton")
        self.verticalLayout_5.addWidget(self.Standby_rButton)
        self.Shutdown_rButton = QtWidgets.QRadioButton(self.widget_2)
        self.Shutdown_rButton.setStyleSheet("QRadioButton{\n"
                                            "font-family: \'Segoe UI\';\n"
                                            "font-style: normal;\n"
                                            "font-weight: 400;\n"
                                            "font-size: 16px;\n"
                                            "line-height: 120%;\n"
                                            "/* or 19px */\n"
                                            "\n"
                                            "spacing: 12px;\n"
                                            "/* control-default/typo */\n"
                                            "\n"
                                            "color: #002033;\n"
                                            "}\n"
                                            "\n"
                                            "QRadioButton::indicator{\n"
                                            "width: 16px;\n"
                                            "height: 16px;\n"
                                            "}\n"
                                            "")
        self.Shutdown_rButton.setObjectName("Shutdown_rButton")
        self.verticalLayout_5.addWidget(self.Shutdown_rButton)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(sysMethWindow)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(24)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.shakerTemp_label = QtWidgets.QLabel(self.widget_6)
        self.shakerTemp_label.setStyleSheet("font-family: \'Inter\';\n"
                                            "font-style: normal;\n"
                                            "font-weight: 400;\n"
                                            "font-size: 14px;\n"
                                            "line-height: 150%;\n"
                                            "width: 257px;\n"
                                            "height: 21px;\n"
                                            "\n"
                                            "/* typo/primary */\n"
                                            "\n"
                                            "color: #002033;")
        self.shakerTemp_label.setObjectName("shakerTemp_label")
        self.verticalLayout_8.addWidget(self.shakerTemp_label)
        self.shakerTemp_lineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.shakerTemp_lineEdit.setStyleSheet("padding: 0px 11px;\n"
                                               "gap: 12px;\n"
                                               "\n"
                                               "position: absolute;\n"
                                               "height: 40px;\n"
                                               "left: 0px;\n"
                                               "right: 0px;\n"
                                               "top: 0px;\n"
                                               "\n"
                                               "/* control-default/bg */\n"
                                               "\n"
                                               "background: #FFFFFF;\n"
                                               "/* control-default/bg-border */\n"
                                               "\n"
                                               "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                               "border-radius: 4px;\n"
                                               "\n"
                                               "\n"
                                               "font-family: \'Segoe UI\';\n"
                                               "font-style: normal;\n"
                                               "font-weight: 400;\n"
                                               "font-size: 16px;\n"
                                               "line-height: 150%;")
        self.shakerTemp_lineEdit.setObjectName("shakerTemp_lineEdit")
        self.verticalLayout_8.addWidget(self.shakerTemp_lineEdit)
        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.injectionSpeed_label = QtWidgets.QLabel(self.widget_7)
        self.injectionSpeed_label.setStyleSheet("font-family: \'Inter\';\n"
                                                "font-style: normal;\n"
                                                "font-weight: 400;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 150%;\n"
                                                "width: 257px;\n"
                                                "height: 21px;\n"
                                                "\n"
                                                "/* typo/primary */\n"
                                                "\n"
                                                "color: #002033;")
        self.injectionSpeed_label.setObjectName("injectionSpeed_label")
        self.verticalLayout.addWidget(self.injectionSpeed_label)
        self.injectionSpeed_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.injectionSpeed_lineEdit.setStyleSheet("padding: 0px 11px;\n"
                                                   "gap: 12px;\n"
                                                   "\n"
                                                   "position: absolute;\n"
                                                   "height: 40px;\n"
                                                   "left: 0px;\n"
                                                   "right: 0px;\n"
                                                   "top: 0px;\n"
                                                   "\n"
                                                   "/* control-default/bg */\n"
                                                   "\n"
                                                   "background: #FFFFFF;\n"
                                                   "/* control-default/bg-border */\n"
                                                   "\n"
                                                   "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                                   "border-radius: 4px;\n"
                                                   "\n"
                                                   "\n"
                                                   "font-family: \'Segoe UI\';\n"
                                                   "font-style: normal;\n"
                                                   "font-weight: 400;\n"
                                                   "font-size: 16px;\n"
                                                   "line-height: 150%;")
        self.injectionSpeed_lineEdit.setObjectName("injectionSpeed_lineEdit")
        self.verticalLayout.addWidget(self.injectionSpeed_lineEdit)
        self.gridLayout_2.addWidget(self.widget_7, 1, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.outerTemp_label = QtWidgets.QLabel(self.widget_5)
        self.outerTemp_label.setStyleSheet("font-family: \'Inter\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 150%;\n"
                                           "width: 257px;\n"
                                           "height: 21px;\n"
                                           "\n"
                                           "/* typo/primary */\n"
                                           "\n"
                                           "color: #002033;")
        self.outerTemp_label.setObjectName("outerTemp_label")
        self.verticalLayout_7.addWidget(self.outerTemp_label)
        self.outerTemp_lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.outerTemp_lineEdit.setStyleSheet("padding: 0px 11px;\n"
                                              "gap: 12px;\n"
                                              "\n"
                                              "position: absolute;\n"
                                              "height: 40px;\n"
                                              "left: 0px;\n"
                                              "right: 0px;\n"
                                              "top: 0px;\n"
                                              "\n"
                                              "/* control-default/bg */\n"
                                              "\n"
                                              "background: #FFFFFF;\n"
                                              "/* control-default/bg-border */\n"
                                              "\n"
                                              "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                              "border-radius: 4px;\n"
                                              "\n"
                                              "\n"
                                              "font-family: \'Segoe UI\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 16px;\n"
                                              "line-height: 150%;")
        self.outerTemp_lineEdit.setObjectName("outerTemp_lineEdit")
        self.verticalLayout_7.addWidget(self.outerTemp_lineEdit)
        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.innerTemp_label = QtWidgets.QLabel(self.widget_4)
        self.innerTemp_label.setStyleSheet("font-family: \'Inter\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 150%;\n"
                                           "width: 257px;\n"
                                           "height: 21px;\n"
                                           "\n"
                                           "/* typo/primary */\n"
                                           "\n"
                                           "color: #002033;")
        self.innerTemp_label.setObjectName("innerTemp_label")
        self.verticalLayout_6.addWidget(self.innerTemp_label)
        self.innerTemp_lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.innerTemp_lineEdit.setStyleSheet("padding: 0px 11px;\n"
                                              "gap: 12px;\n"
                                              "\n"
                                              "position: absolute;\n"
                                              "height: 40px;\n"
                                              "left: 0px;\n"
                                              "right: 0px;\n"
                                              "top: 0px;\n"
                                              "\n"
                                              "/* control-default/bg */\n"
                                              "\n"
                                              "background: #FFFFFF;\n"
                                              "/* control-default/bg-border */\n"
                                              "\n"
                                              "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                              "border-radius: 4px;\n"
                                              "\n"
                                              "\n"
                                              "font-family: \'Segoe UI\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 16px;\n"
                                              "line-height: 150%;")
        self.innerTemp_lineEdit.setText("")
        self.innerTemp_lineEdit.setMaxLength(32767)
        self.innerTemp_lineEdit.setFrame(True)
        self.innerTemp_lineEdit.setObjectName("innerTemp_lineEdit")
        self.verticalLayout_6.addWidget(self.innerTemp_lineEdit)
        self.gridLayout_2.addWidget(self.widget_4, 0, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.transpLineTemp_label = QtWidgets.QLabel(self.widget_8)
        self.transpLineTemp_label.setStyleSheet("font-family: \'Inter\';\n"
                                                "font-style: normal;\n"
                                                "font-weight: 400;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 150%;\n"
                                                "width: 257px;\n"
                                                "height: 21px;\n"
                                                "\n"
                                                "/* typo/primary */\n"
                                                "\n"
                                                "color: #002033;")
        self.transpLineTemp_label.setObjectName("transpLineTemp_label")
        self.verticalLayout_4.addWidget(self.transpLineTemp_label)
        self.transpLineTemp_lineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.transpLineTemp_lineEdit.setStyleSheet("padding: 0px 11px;\n"
                                                   "gap: 12px;\n"
                                                   "\n"
                                                   "position: absolute;\n"
                                                   "height: 40px;\n"
                                                   "left: 0px;\n"
                                                   "right: 0px;\n"
                                                   "top: 0px;\n"
                                                   "\n"
                                                   "/* control-default/bg */\n"
                                                   "\n"
                                                   "background: #FFFFFF;\n"
                                                   "/* control-default/bg-border */\n"
                                                   "\n"
                                                   "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                                   "border-radius: 4px;\n"
                                                   "\n"
                                                   "\n"
                                                   "font-family: \'Segoe UI\';\n"
                                                   "font-style: normal;\n"
                                                   "font-weight: 400;\n"
                                                   "font-size: 16px;\n"
                                                   "line-height: 150%;")
        self.transpLineTemp_lineEdit.setObjectName("transpLineTemp_lineEdit")
        self.verticalLayout_4.addWidget(self.transpLineTemp_lineEdit)
        self.gridLayout_2.addWidget(self.widget_8, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.frame = QtWidgets.QFrame(sysMethWindow)
        self.frame.setMinimumSize(QtCore.QSize(593, 33))
        self.frame.setMaximumSize(QtCore.QSize(593, 33))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelMethButton = QtWidgets.QPushButton(self.frame)
        self.cancelMethButton.setMinimumSize(QtCore.QSize(0, 32))
        self.cancelMethButton.setMaximumSize(QtCore.QSize(16777215, 32))
        self.cancelMethButton.setStyleSheet("#cancelMethButton{\n"
                                            "\n"
                                            "height: 32px;\n"
                                            "width: 81px;\n"
                                            "/* control-primary/bg */\n"
                                            "\n"
                                            "\n"
                                            "background: #fff;\n"
                                            "border-radius: 16px;\n"
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
                                            "#cancelMethButton::hover{\n"
                                            "background: rgb(205, 238, 255);\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "#cancelMethButton::pressed{\n"
                                            "\n"
                                            "border: 4px solid rgb(139, 205, 255);\n"
                                            "}")
        self.cancelMethButton.setObjectName("cancelMethButton")
        self.horizontalLayout.addWidget(self.cancelMethButton)
        self.addMethButton = QtWidgets.QPushButton(self.frame)
        self.addMethButton.setMinimumSize(QtCore.QSize(94, 32))
        self.addMethButton.setMaximumSize(QtCore.QSize(94, 32))
        self.addMethButton.setStyleSheet("#addMethButton{\n"
                                         "\n"
                                         "\n"
                                         "/* control-primary/bg */\n"
                                         "\n"
                                         "\n"
                                         "background: #0078D2;\n"
                                         "border-radius: 16px;\n"
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
                                         "#addMethButton::hover{\n"
                                         "background: rgb(0, 134, 229);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "#addMethButton::pressed{\n"
                                         "\n"
                                         "border: 4px solid rgb(0, 101, 173);\n"
                                         "}")
        self.addMethButton.setObjectName("addMethButton")
        self.horizontalLayout.addWidget(self.addMethButton)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(sysMethWindow)
        QtCore.QMetaObject.connectSlotsByName(sysMethWindow)

    def retranslateUi(self, sysMethWindow):
        _translate = QtCore.QCoreApplication.translate
        sysMethWindow.setWindowTitle(_translate("sysMethWindow", "Установка режима работы"))
        self.header_label.setText(_translate("sysMethWindow", "Установка режима работы"))
        self.mode_label.setText(_translate("sysMethWindow", "Режим работы"))
        self.Startup_rButton.setText(_translate("sysMethWindow", "Рабочий режим"))
        self.Standby_rButton.setText(_translate("sysMethWindow", "Ожидание"))
        self.Shutdown_rButton.setText(_translate("sysMethWindow", "Отключение"))
        self.shakerTemp_label.setText(_translate("sysMethWindow", "Температура мешалки (С):"))
        self.shakerTemp_lineEdit.setText(_translate("sysMethWindow", "20"))
        self.injectionSpeed_label.setText(_translate("sysMethWindow", "Скорость ввода проб:"))
        self.injectionSpeed_lineEdit.setText(_translate("sysMethWindow", "5"))
        self.outerTemp_label.setText(_translate("sysMethWindow", "Температура внешней трубки (С):"))
        self.outerTemp_lineEdit.setText(_translate("sysMethWindow", "1000"))
        self.innerTemp_label.setText(_translate("sysMethWindow", "Температура внутренней трубки (С):"))
        self.innerTemp_lineEdit.setPlaceholderText(_translate("sysMethWindow", "от 300 до 500"))
        self.transpLineTemp_label.setText(_translate("sysMethWindow", "Температура транспортной линии (С):"))
        self.transpLineTemp_lineEdit.setText(_translate("sysMethWindow", "200"))
        self.cancelMethButton.setText(_translate("sysMethWindow", "Отмена"))
        self.addMethButton.setText(_translate("sysMethWindow", "Добавить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    sysMethWindow = QtWidgets.QDialog()
    ui = Ui_sysMethWindow()
    ui.setupUi(sysMethWindow)
    sysMethWindow.show()
    sys.exit(app.exec_())
