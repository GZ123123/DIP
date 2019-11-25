from PyQt5 import QtCore, QtGui, QtWidgets , uic
from PyQt5.QtWidgets import QSizePolicy

import sys
import cv2
import numpy as np
from helper import image_loader as il
from helper import image_covert as ic
from helper import path as PATH
from subWindow import SubWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        uic.loadUi('./ui/mainWindow.ui',self)

        self.__contruct()
        
        self.__connect_function__()

    def __contruct(self):
        
        self.subIndex = 0
        self.image = None
        self.imageList = []
        return     
        
    def __connect_function__(self):
        self.actionOpen.triggered.connect(self.__choose_image__)
        self.actionSave.triggered.connect(self.__save_image__)
        self.actionExit.triggered.connect(self.__exit)
        self.actionBlur.triggered.connect(self.__add_blurwindow__)
        self.actionGaussian_Blur.triggered.connect(self.__add_gaussian_blur__)
        self.actionMedian_Filter.triggered.connect(self.__add_median_blur__)
        self.actionBox_Filter.triggered.connect(self.__add_box_filter__)
        self.actionBilateral_Filter.triggered.connect(self.__add__bilateral_filter__)

    def __add_subwindow__(self,_image,_type="original"):
        if( self.image is not None ):
            # self.imageList.append(_image)
            _subWindow = SubWindow(self,_image,_type)
            self.gridLayout.addWidget(_subWindow,(self.subIndex)/3,(self.subIndex) % 3)
            self.subIndex+=1
        else: 
            self.__choose_image__()

    def __add_blurwindow__(self):
        if(self.image is None): 
            self.__choose_image__() 
        blur_image = ic.__transform_to_blur(self.image)
        self.add_filtering_image("blur",blur_image)
        self.__add_subwindow__(blur_image,"Blur")
    
    def __add_gaussian_blur__(self):
        if(self.image is None): 
            self.__choose_image__() 
        blur_image = ic.__transform_to_gaussian_blur(self.image)
        self.add_filtering_image("gaussian_blur",blur_image)
        self.__add_subwindow__(blur_image,"Gaussian Blur")

    def __add_median_blur__(self):
        if(self.image is None): 
            self.__choose_image__() 
        blur_image = ic.__transform_to_median_blur(self.image)
        self.add_filtering_image("median_blur",blur_image)
        self.__add_subwindow__(blur_image,"Median Blur")

    def __add_box_filter__(self):
        if(self.image is None): 
            self.__choose_image__() 
        blur_image = ic.__transform_to_box_filter(self.image)
        self.add_filtering_image("box_filter",blur_image)
        self.__add_subwindow__(blur_image,"Box Filter")

    def __add__bilateral_filter__(self):
        if(self.image is None): 
            self.__choose_image__() 
        blur_image = ic.__transform_to_bilateral_filter(self.image)
        self.add_filtering_image("bilateral_filter",blur_image)
        self.__add_subwindow__(blur_image,"Bilateral Filter")

    def __choose_image__(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                             "Open Image...", filter="Image formats: *.png; *.jpg; *.tif")

        currentImage = False
        if(self.image is not None):
            currentImage = True
        if (self.file_path):
            self.image = il.__load_image__(self.file_path)
        if(currentImage is False):
            self.__add_subwindow__(self.image)
        else : 
            return
            # self.__add_subwindow__(self.image)
    
    def __save_image__(self):
        if len(self.imageList) > 0:
            file_name = PATH.get_filename(self.file_path)
            file_extension = PATH.get_extension(self.file_path)

            for _type,_image in self.imageList:
                _dir = "output/{0}_{1}.{2}".format(file_name,_type,file_extension)
                cv2.imwrite(_dir,_image)

    def __exit(self):
        sys.exit()

    def add_filtering_image(self,_type,_image):
        self.imageList.append((_type,_image))

    def __set_label_image(self,label,Cv2Image):
        image = il.__convert_to_QtImage__(Cv2Image)
        widge = il.__convert_to_QtWidge__(image)
        widge = (il.__resize_image__(widge,100))
        label.setPixmap(widge)
        return widge

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windown = MainWindow()
    windown.show()
    sys.exit(app.exec_())
