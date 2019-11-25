from PyQt5 import QtWidgets
import sys
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windown = MainWindow()
    windown.show()
    sys.exit(app.exec_())
