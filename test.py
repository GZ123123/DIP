from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel,QScrollArea
from PyQt5.QtGui import QImage, QPixmap, QPalette
import cv2
import sys

class DisplayImageWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(DisplayImageWidget, self).__init__(parent)

        imageLabel = QLabel()
        image = QImage("testImage.jpg")
        widget = QPixmap.fromImage(image)
        widget = widget.scaled(700,700)
        imageLabel.setPixmap(widget)

        scrollArea = QScrollArea()
        scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidget(imageLabel)
        
        self.setCentralWidget(scrollArea)
    # @QtCore.pyqtSlot()
    # def show_image(self):
    #     self.image = cv2.imread('testImage.jpg')
    #     self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
    #     self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = DisplayImageWidget()
    display_image_widget.show()
    sys.exit(app.exec_())