from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Analyzer")
    window.setGeometry(0,0,1440,1024)

    username_text = QtWidgets.QLabel(window)
    username_text.setText("Имя пользователя")
    username_text.move(6,808)
    username_text.adjustSize()
    username_text





    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()
