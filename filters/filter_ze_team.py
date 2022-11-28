import cv2

def ze_team(matrice):
    f"""
    Put the team member names on an image 

    :param matrice: The matrix of the image
    :return image_filter: the version of the {matrice} with the names on it.
    """
    team_member = ["Valdo","Matteo","Ben Youcef"]
    font = cv2.FONT_HERSHEY_DUPLEX
    font_size = 1
    font_weight = 2
    x_pos = 50
    y_pos = 20
    color = (255, 255, 255)
    y_plus = 0
    for member in team_member:
        image_filter = cv2.putText(matrice, member,(x_pos, y_pos + y_plus),font,font_size,color,font_weight )
        y_plus = y_plus + 50
    return image_filter