import cv2
import numpy as np

def dilate_filter(matrice, dilate_intensity):

    f"""
    Convert a non filtered image matrix into a dilated image matrix.
    
    :param matrice: The matrix of the image
    :param dilate_intensity: The power of the dilation.
    :return image_filter: the dilated matrix version of the {matrice}
    """

    kernel = np.ones((dilate_intensity, dilate_intensity), np.uint8)
    image_filter = cv2.dilate(matrice, kernel)
    return image_filter
