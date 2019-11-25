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
def _MainWindow__apply_histogram(image):
    channels = cv2.split(image)
    eq_channels = []
    for ch, color in zip(channels, ['B', 'G', 'R']):
        eq_channels.append(cv2.equalizeHist(ch))
    eq_image = cv2.merge(eq_channels)
    return eq_image

def _MainWindow__median_threshold(image,size_n, thresh):
    height, width, channels = image.shape
    new = cv2.blur(image,(5,5))
    for i in range(0,width):
        for j in range(0,height):
            if(abs(image[i:i,j:j] - new[i:i,j:j]) <= thresh):
                new[i:i,j:j] = image[i:i,j:j]
    return new

