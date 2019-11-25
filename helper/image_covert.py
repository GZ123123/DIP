import cv2

def _MainWindow__transform_to_gray(image):
    return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
def _MainWindow__transform_to_blur(image):
    return cv2.blur(image,(5,5))
def _MainWindow__transform_to_gaussian_blur(image):
    return cv2.GaussianBlur(image,(5,5),0)
def _MainWindow__transform_to_median_blur(image):
    return cv2.medianBlur(image,5)
def _MainWindow__transform_to_box_filter(image):
    return cv2.boxFilter(image, 0, (7,7))
def _MainWindow__transform_to_bilateral_filter(image):
    return cv2.bilateralFilter(image, 9, 75, 75)

