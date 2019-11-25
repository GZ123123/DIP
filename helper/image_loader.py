import cv2
from PyQt5 import QtCore, QtGui

def __load_image__(path):
    return cv2.imread(path)

def __convert_to_QtImage__(image):
    return QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()

def __convert_to_QtWidget__(image):
    return QtGui.QPixmap.fromImage(image)

def __resize_image__(image,width_percent=None,height_percent=None):
    image_size = image.size()
    if(width_percent is not None):
        new_width = image_size.width() * width_percent / 100 
    else: 
        new_width = image_size.width() * height_percent / 100
    if(height_percent is not None):
        new_height = image_size.height() * height_percent / 100
    else:
        new_height = image_size.height() * width_percent / 100

    return image.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio)