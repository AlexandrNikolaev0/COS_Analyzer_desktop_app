# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(object):
    """Класс окна авторизации"""
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.setEnabled(True)
        AuthWindow.resize(1440, 838)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthWindow.sizePolicy().hasHeightForWidth())
        AuthWindow.setSizePolicy(sizePolicy)
        AuthWindow.setMinimumSize(QtCore.QSize(1440, 838))
        AuthWindow.setMaximumSize(QtCore.QSize(1440, 838))
        AuthWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        AuthWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        AuthWindow.setStyleSheet("background-image: url(:/imgs/authBackground.png);")
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
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
                                  "height: 516px;\n"
                                  "left: 80px;\n"
                                  "top: 60px;\n"
                                  "\n"
                                  "background: #FFFFFF;\n"
                                  "border-radius: 6px; }")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(70, 24, 70, 50)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(149)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(149, 81))
        self.label.setMaximumSize(QtCore.QSize(149, 81))
        self.label.setStyleSheet("image: url(:/imgs/logo-gazprom-neft.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setStyleSheet("font-family: \'Segoe UI\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 18px;\n"
                                      "line-height: 150%;\n"
                                      "color: rgba(0, 32, 51, 0.6);\n"
                                      "")
        self.name_label.setTextFormat(QtCore.Qt.PlainText)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.name_label.setIndent(0)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_2.addWidget(self.name_label)
        self.name_comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_comboBox.sizePolicy().hasHeightForWidth())
        self.name_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name_comboBox.setFont(font)
        self.name_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_comboBox.setStyleSheet("\n"
                                         "\n"
                                         "#name_comboBox{\n"
                                         "height: 48px;\n"
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
                                         "#name_comboBox::drop-down{\n"
                                         "border: 0px;\n"
                                         "width: 48px;\n"
                                         "}\n"
                                         "\n"
                                         "#name_comboBox::down-arrow {\n"
                                         "    image: url(:/imgs/arrowComboBox.png);\n"
                                         "width: 48px;\n"
                                         "}\n"
                                         "\n"
                                         "#name_comboBox::on {\n"
                                         "border: 1px solid #0091FF;\n"
                                         "outline: 0px;\n"
                                         "}\n"
                                         "\n"
                                         "#name_comboBox QListView {\n"
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
                                         "padding-top:10px;\n"
                                         "padding-bottom:10px;\n"
                                         "padding-left:12px;\n"
                                         "padding-right:12px;\n"
                                         "}\n"
                                         "\n"
                                         "#name_comboBox QAbstractItemView::text {\n"
                                         "\n"
                                         "padding:10px;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.name_comboBox.setEditable(False)
        self.name_comboBox.setMaxVisibleItems(10)
        self.name_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.name_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.name_comboBox.setIconSize(QtCore.QSize(48, 48))
        self.name_comboBox.setDuplicatesEnabled(False)
        self.name_comboBox.setFrame(False)
        self.name_comboBox.setObjectName("name_comboBox")
        self.name_comboBox.addItem("")
        self.name_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.name_comboBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.password_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        self.password_label.setStyleSheet("font-family: \'Segoe UI\';\n"
                                          "font-style: normal;\n"
                                          "font-weight: 400;\n"
                                          "font-size: 18px;\n"
                                          "line-height: 150%;\n"
                                          "color: rgba(0, 32, 51, 0.6);")
        self.password_label.setTextFormat(QtCore.Qt.PlainText)
        self.password_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.password_label.setIndent(0)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_3.addWidget(self.password_label)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 48))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(16777215, 48))
        self.password_lineEdit.setStyleSheet("width: 442px;\n"
                                             "height: 48px;\n"
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
                                             "font-size: 18px;\n"
                                             "padding-left: 13px;\n"
                                             "color: black;")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.eyeBtn = QtWidgets.QPushButton(self.widget_3)
        self.eyeBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.eyeBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.eyeBtn.setStyleSheet("#eyeBtn{\n"
                                  "box-sizing: border-box;\n"
                                  "\n"
                                  "align: top;\n"
                                  "\n"
                                  "/* control-default/bg */\n"
                                  "\n"
                                  "background: #FFFFFF;\n"
                                  "/* control-default/typo-placeholder */\n"
                                  "\n"
                                  "border: 1px solid rgba(0, 66, 105, 0.28);\n"
                                  "\n"
                                  "border-radius: 4px;\n"
                                  "}\n"
                                  "\n"
                                  "#eyeBtn::hover {\n"
                                  "border: 1px solid rgba(0, 66, 105, 0.15);\n"
                                  "\n"
                                  "}\n"
                                  "\n"
                                  "#eyeBtn::pressed {\n"
                                  "border: 2px solid rgba(0, 66, 105, 0.28);\n"
                                  "}")
        self.eyeBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/eyePassIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eyeBtn.setIcon(icon)
        self.eyeBtn.setIconSize(QtCore.QSize(20, 20))
        self.eyeBtn.setObjectName("eyeBtn")
        self.horizontalLayout.addWidget(self.eyeBtn)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.signin_statusLabel = QtWidgets.QLabel(self.widget_2)
        self.signin_statusLabel.setStyleSheet("#signin_statusLabel{\n"
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
        self.signin_statusLabel.setText("")
        self.signin_statusLabel.setObjectName("signin_statusLabel")
        self.verticalLayout_4.addWidget(self.signin_statusLabel)
        self.signin_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.signin_pushButton.setStyleSheet("#signin_pushButton{\n"
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
                                             "#signin_pushButton::hover{\n"
                                             "background: rgb(0, 134, 229);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "#signin_pushButton::pressed{\n"
                                             "\n"
                                             "border: 4px solid rgb(0, 101, 173);\n"
                                             "}")
        self.signin_pushButton.setAutoDefault(False)
        self.signin_pushButton.setDefault(False)
        self.signin_pushButton.setFlat(False)
        self.signin_pushButton.setObjectName("signin_pushButton")
        self.verticalLayout_4.addWidget(self.signin_pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        AuthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AuthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        AuthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AuthWindow)
        self.statusbar.setObjectName("statusbar")
        AuthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Окно авторизации"))
        self.name_label.setText(_translate("AuthWindow", "Имя"))
        self.name_comboBox.setCurrentText(_translate("AuthWindow", "Analyst"))
        self.name_comboBox.setItemText(0, _translate("AuthWindow", "Analyst"))
        self.name_comboBox.setItemText(1, _translate("AuthWindow", "Lab Manager"))
        self.password_label.setText(_translate("AuthWindow", "Пароль"))
        self.password_lineEdit.setPlaceholderText(_translate("AuthWindow", "Введите пароль..."))
        self.signin_pushButton.setText(_translate("AuthWindow", "Войти"))


import resources

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AuthWindow = QtWidgets.QMainWindow()
    ui = Ui_AuthWindow()
    ui.setupUi(AuthWindow)
    AuthWindow.show()
    sys.exit(app.exec_())