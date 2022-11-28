import cv2
import utils

def blur_filter(matrice, blur_intensity):
    f"""
    Convert a non filtered image matrix into a blured image matrix.

    :param matrice: The matrix of the image
    :param blur_intensity: The power of the blur.
    :return image_filter: the dilated matrix version of the {matrice}
    """
    kernel = (blur_intensity, blur_intensity)
    image_filter = cv2.blur(matrice,kernel)
    return image_filter

