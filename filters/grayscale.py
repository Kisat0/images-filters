import cv2

input_dir = 'images/'
output_dir = 'test/'

def gray_filter(matrice):
    f"""
    Convert a non filtered image matrix into a grayscale image matrix.

    :param matrice: The matrix of the image
    :return image_filter: the grayscaled matrix version of the {matrice}
    """
    image_filter = cv2.cvtColor(matrice, cv2.COLOR_BGR2GRAY)
    return image_filter

