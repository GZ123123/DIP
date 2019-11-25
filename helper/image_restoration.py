from scipy import signal
import numpy as np
from scipy.stats import rayleigh,erlang,uniform,exponweib,gamma
import cv2

def __rayleigh__(image):
    image = image / 255
    return image + rayleigh.pdf(image).reshape(image.shape)