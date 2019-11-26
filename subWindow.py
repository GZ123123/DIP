from PyQt5 import QtCore, QtGui, QtWidgets , uic

import sys
import cv2
import numpy as np
from helper import image_loader as il
from pathlib import Path

class SubWindow(QtWidgets.QWidget):
    def __init__(self,parent,image,text = "Original"):
        super(SubWindow,self).__init__()
        __dir__ = (Path(__file__).resolve().parent) 
        __dir__ = str(__dir__) + '/ui/subWindow.ui'
        uic.loadUi(__dir__,self)
        self.parent = parent 

        image = il.__convert_to_QtImage__(image)
        self.widget = il.__convert_to_QtWidget__(image)

        self.__contruct(text)
        self.__connect__()

    def __reset__(self,image):
        image = il.__convert_to_QtImage__(image)
        self.widget = il.__convert_to_QtWidget__(image)
        self.__real_scale__()
        
    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)
        
        # _old_size = event.oldSize() 
        # _new_size = event.size()
        # width_percent = None
        # height_percent = None

        # # created
        # if(_old_size.width() == -1): 
        #     if(self.widget.size().width() >= self.widget.size().height()):
        #         width_percent = _new_size.width() / self.widget.size().width() * 100
        #     else :
        #         height_percent = _new_size.height() /  self.widget.size().height() * 100

        #     self.__set_label_widget(self.label,width_percent,height_percent)
        #     self.label.resize(self.widget.size())
        #     return
        
        # width_percent = _new_size.width() / _old_size.width()
        # height_percent = _new_size.height() / _old_size.height()

    def __contruct(self,text):
        self.currentZoom = 100

        self.Image_Label.setText(text)
        # self.__set_label_widget(self.label,self.image)
        self.__set_label_widget(self.label,100,100)
    
    def __connect__(self):
        self.zoom_in.clicked.connect(self.__zoom_in__)
        self.zoom_out.clicked.connect(self.__zoom_out__)
        self.Fix_Window.clicked.connect(self.__fix_window__)
        self.Real_scale.clicked.connect(self.__real_scale__)

    def __set_label_image(self,label,Cv2Image,width_percent,height_percent):
        image = il.__convert_to_QtImage__(Cv2Image)
        widge = il.__convert_to_QtWidge__(image)
        widge = (il.__resize_image__(widge,width_percent,height_percent))
        label.setPixmap(widge)
        # return

    def __set_label_widget(self,label,width_percent,height_percent):
        widget = self.widget
        widget = (il.__resize_image__(widget,width_percent,height_percent))
        label.setPixmap(widget)
        return widget.size()
    
    def __zoom_in__(self):
        self.currentZoom += 10
        new_size = self.__set_label_widget(self.label,self.currentZoom,None)
        self.label.resize(new_size)
        return
    
    def __zoom_out__(self):
        self.currentZoom -= 10
        new_size = self.__set_label_widget(self.label,self.currentZoom,None)
        self.label.resize(new_size)
        return

    def __fix_window__(self):
        # print(self.size())
        _new_size = self.size()
        width_percent = None
        height_percent = None

        if(self.widget.size().width() >= self.widget.size().height()):
            width_percent = _new_size.width() / self.widget.size().width() * 100
            self.__set_label_widget(self.label,width_percent,None)
            self.currentZoom = width_percent

        else :
            height_percent = _new_size.height() /  self.widget.size().height() * 100
            self.__set_label_widget(self.label,None,height_percent)
            self.currentZoom = height_percent

    
    def __real_scale__(self):
        self.currentZoom = 100
        self.__set_label_widget(self.label,100,100)
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     windown = SubWindow()
#     windown.show()
#     sys.exit(app.exec_())
